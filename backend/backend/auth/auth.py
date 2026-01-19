"""
This file handles authentification.


file: backend/backend/auth/auth.py
"""

import uuid

from typing import (
    Optional,
    List
)
from datetime import (
    datetime,
    timedelta,
    timezone
)
from pydantic import (
    BaseModel,
    Field
)
from jose import (
    jwt,
    JWTError
)
from passlib.context import CryptContext
from fastapi import (
    HTTPException,
    status,
    Request
)

# Models
from backend.backend.auth.models import (
    TokenPayload,
    RefreshTokenData
)

# --------------------
# Configuration
# --------------------

SECRET_KEY = "CHANGE_ME"  # load from env
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Auth(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    db: any  # inject your DB/session/repo abstraction here

    # ----------------
    # Passwords
    # ----------------
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain: str, hashed: str) -> bool:
        return pwd_context.verify(plain, hashed)

    # ----------------
    # Token creation
    # ----------------
    def create_access_token(
        self,
        user_id: str,
        scopes: List[str],
        expires: Optional[timedelta] = None,
    ) -> str:

        expire = datetime.now(timezone.utc) + (
            expires or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )


        payload = {
            "sub": user_id,
            "scopes": scopes,
            "exp": expire,
            "jti": str(uuid.uuid4()),
        }

        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def create_refresh_token(self, user_id: str, device_id: str) -> str:
        token_id = str(uuid.uuid4())
        expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)


        payload = {
            "sub": user_id,
            "jti": token_id,
            "exp": expire,
            "type": "refresh",
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        self.store_refresh_token(user_id, token_id, device_id, expire)
        return token

    # ----------------
    # Token verification
    # ----------------
    def verify_access_token(self, token: str) -> TokenPayload:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return TokenPayload(**payload)
        except JWTError:
            raise HTTPException(

                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
            )

    def verify_refresh_token(self, token: str) -> RefreshTokenData:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid refresh token")


        token_id = payload["jti"]
        user_id = payload["sub"]


        record = self.db.get_refresh_token(token_id)

        if not record or record.revoked:
            raise HTTPException(status_code=401, detail="Refresh token revoked")

        return record

    # ----------------
    # Refresh token lifecycle
    # ----------------
    def store_refresh_token(
        self,
        user_id: str,
        token_id: str,
        device_id: str,
        expires_at: datetime,

    ) -> None:
        self.db.insert_refresh_token(

            RefreshTokenData(
                user_id=user_id,
                token_id=token_id,
                device_id=device_id,
                expires_at=expires_at,
            )
        )

    def rotate_refresh_token(self, old_token: str) -> str:
        old = self.verify_refresh_token(old_token)
        self.revoke_refresh_token(old.token_id)
        return self.create_refresh_token(old.user_id, old.device_id)

    def revoke_refresh_token(self, token_id: str) -> None:
        self.db.revoke_refresh_token(token_id)

    def revoke_all_user_tokens(self, user_id: str) -> None:
        self.db.revoke_all_refresh_tokens(user_id)

    # ----------------
    # FastAPI helpers
    # ----------------
    def get_current_user(self, request: Request):
        token = request.cookies.get("access_token")
        if not token:
            raise HTTPException(status_code=401, detail="Missing access token")


        payload = self.verify_access_token(token)
        user = self.db.get_user(payload.sub)


        if not user:

            raise HTTPException(status_code=401, detail="User not found")

        return user

    def require_user(self):
        def dependency(request: Request):
            return self.get_current_user(request)
        return dependency

    def require_active_user(self):
        def dependency(request: Request):
            user = self.get_current_user(request)

            if not user.is_active:
                raise HTTPException(status_code=403, detail="Inactive user")
            return user
        return dependency

    def require_scope(self, scope: str):
        def dependency(request: Request):
            token = request.cookies.get("access_token")
            payload = self.verify_access_token(token)
            if scope not in payload.scopes:
                raise HTTPException(status_code=403, detail="Insufficient scope")
        return dependency

    # ----------------
    # Authentication
    # ----------------
    def authenticate_user(self, email: str, password: str):
        user = self.db.get_user_by_email(email)
        if not user:
            return None

        if not self.verify_password(password, user.password_hash):
            return None

        return user

    def change_password(self, user_id: str, old_password: str, new_password: str):
        user = self.db.get_user(user_id)
        if not self.verify_password(old_password, user.password_hash):
            raise HTTPException(status_code=403, detail="Invalid password")

        user.password_hash = self.hash_password(new_password)
        self.db.save_user(user)


        self.invalidate_sessions_on_password_change(user_id)

    def invalidate_sessions_on_password_change(self, user_id: str):
        self.revoke_all_user_tokens(user_id)

    # ----------------
    # Security intelligence
    # ----------------
    def is_token_revoked(self, token_id: str) -> bool:
        return self.db.is_refresh_token_revoked(token_id)


    def detect_refresh_token_reuse(self, token_id: str, user_id: str):
        if self.is_token_revoked(token_id):
            self.revoke_all_user_tokens(user_id)

            raise HTTPException(status_code=401, detail="Token reuse detected")

    def log_auth_event(
        self,
        user_id: str,
        event_type: str,
        ip: str,

        user_agent: str,
    ):
        self.db.insert_auth_log(
            user_id=user_id,
            event_type=event_type,
            ip=ip,
            user_agent=user_agent,
            timestamp=datetime.now(timezone.utc),

        )
