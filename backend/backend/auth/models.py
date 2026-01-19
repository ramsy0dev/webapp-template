"""
This file contains models used in the Auth class.


file: backend/backend/auth/models.py
"""

from typing import List
from pydantic import BaseModel 

from datetime import (
    datetime,
)

class TokenPayload(BaseModel):
    sub: str
    exp: datetime
    scopes: List[str] = []
    jti: str


class RefreshTokenData(BaseModel):
    user_id: str
    token_id: str
    device_id: str
    expires_at: datetime
    revoked: bool = False
