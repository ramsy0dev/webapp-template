# webapp-template

A modern full-stack web application template with FastAPI backend, React frontend, and integrated development workflow using procmux.

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Development](#development)
- [Project Features](#project-features)
- [Building for Production](#building-for-production)
- [Documentation](#documentation)

## 🎯 Overview

This is a production-ready template for building modern web applications with:
- **Backend**: FastAPI with authentication, rate limiting, and caching
- **Frontend**: React with React Router v7 and Tailwind CSS
- **Process Management**: procmux for easy local development
- **Database**: PostgreSQL support with SQLAlchemy ORM

Perfect for starting new projects quickly with best practices already in place.

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI 0.128.0
- **Server**: Uvicorn
- **Database**: PostgreSQL + SQLAlchemy ORM
- **Authentication**: JWT with refresh token rotation
- **Caching**: In-memory TTL cache with cachetools
- **Rate Limiting**: Cache-based rate limiter
- **Logging**: Python logging with file and stdout handlers

### Frontend
- **Framework**: React 19.2.3
- **Router**: React Router 7.12.0
- **Styling**: Tailwind CSS 4.1.13
- **Build Tool**: Vite 7.1.7
- **Type Safety**: TypeScript

### Development Tools
- **Process Manager**: procmux - TUI for managing multiple processes
- **Documentation**: Sphinx with Book Theme
- **Package Manager**: Poetry (backend), npm (frontend)

## 📁 Project Structure

```
webapp-template/
├── backend/                          # FastAPI backend
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── api.py                   # Main FastAPI app
│   │   ├── logger.py                # Logging configuration
│   │   ├── middleware.py            # Middleware utilities
│   │   ├── auth/                    # Authentication module
│   │   │   ├── auth.py
│   │   │   └── models.py
│   │   ├── cache/                   # Caching module
│   │   │   ├── __init__.py
│   │   │   └── cache_manager.py
│   │   ├── database/                # Database module
│   │   │   ├── __init__.py
│   │   │   ├── conn.py
│   │   │   ├── handler.py
│   │   │   └── tables/
│   │   │       ├── __init__.py
│   │   │       └── base.py
│   │   ├── rate_limiter/            # Rate limiting module
│   │   │   ├── __init__.py
│   │   │   └── depends.py
│   │   ├── routes/                  # API routes
│   │   │   ├── __init__.py
│   │   │   └── home_route.py
│   │   └── encrypt/                 # Encryption utilities
│   ├── docs/                        # Sphinx documentation
│   ├── tests/                       # Backend tests
│   ├── uvicorn.ini                  # Uvicorn configuration
│   └── pyproject.toml              # Poetry dependencies
├── frontend/                         # React frontend
│   ├── app/
│   │   ├── app.css
│   │   ├── root.tsx                # Root layout
│   │   ├── routes.ts               # Route configuration
│   │   ├── routes/
│   │   │   └── home.tsx
│   │   └── welcome/
│   │       └── welcome.tsx
│   ├── public/                     # Static assets
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── Dockerfile
│   └── README.md
├── scripts/                         # Utility scripts
│   └── build_backend_docs.py
├── procmux.yaml                    # Process manager configuration
├── README.md                       # This file
└── .gitignore

```

## 📦 Prerequisites

- **Python**: 3.12+
- **Node.js**: 20+
- **PostgreSQL**: 12+ (optional, for production database)
- **Poetry**: Latest version (for Python dependency management)
- **npm**: Latest version (comes with Node.js)

### Installation

1. **Install Poetry** (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. **Install Node dependencies**:
```bash
cd frontend
npm install
cd ..
```

3. **Install Python dependencies**:
```bash
cd backend
poetry install
cd ..
```

4. **Install procmux**:
```bash
# Using pip
pip install procmux

# Or using brew (on macOS)
brew tap napisani/procmux
brew install procmux
```

## 🚀 Quick Start

### 1. Start Development Environment

```bash
procmux --config procmux.yaml
```

This opens a **TUI (Terminal User Interface)** with multiple terminal panes for each process:
- **Backend**: FastAPI on `http://localhost:8000` 
- **Frontend**: React development server on `http://localhost:5173`

Each process runs in its own switchable terminal pane within procmux.

### 2. Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (Swagger UI)

### 3. Control Processes in procmux

**Keyboard Shortcuts**:
- `↑/↓` or `j/k`: Navigate between processes in the sidebar
- `→/←` or `h/l`: Switch between sidebar and terminal pane
- `s`: Start the selected process
- `x`: Stop the selected process
- `/`: Search/filter processes by name
- `c-w`: Switch focus between process list and terminal
- `?`: Show help and all keybindings
- `q`: Quit procmux

**Mouse Support**: Click on processes to select, and click on the terminal pane to interact with it

### 3. Stop Development Environment

```bash
# Press 'q' in the procmux window to quit
```

## 💻 Development

### Backend Development

```bash
cd backend
poetry shell
poetry install  # Install dependencies
poetry run uvicorn backend.api:api --reload
```

**Key Backend Modules**:
- **Authentication** (`backend/auth/`): JWT-based auth with refresh tokens
- **Rate Limiter** (`backend/rate_limiter/`): Cache-based rate limiting for endpoints
- **Cache Manager** (`backend/cache/`): Thread-safe in-memory caching
- **Database** (`backend/database/`): SQLAlchemy ORM setup
- **Routes** (`backend/routes/`): API endpoint definitions

**Add a New Route**:
```python
# In backend/backend/routes/my_route.py
from fastapi import APIRouter

my_router = APIRouter(prefix="/api/v1", tags=["my-route"])

@my_router.get("/hello")
async def hello():
    return {"message": "Hello!"}
```

Then register in `backend/backend/routes/__init__.py`:
```python
from .my_route import my_router

routes = [
    home_router,
    my_router,  # Add your router
]
```

### Frontend Development

```bash
cd frontend
npm run dev
```

**Key Frontend Features**:
- React Router v7 for client-side routing
- Tailwind CSS for styling
- TypeScript for type safety
- Server-side rendering by default (configurable)

**Add a New Route**:
```typescript
// In frontend/app/routes/new-page.tsx
import type { Route } from "./+types/new-page";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "New Page" },
    { name: "description", content: "My new page" },
  ];
}

export default function NewPage() {
  return <div>New Page Content</div>;
}
```

### Logging

The backend has comprehensive logging configured in `backend/backend/logger.py`:
- **Console output**: Real-time logs in terminal
- **File output**: Persistent logs in `webapp-template-backend.log`
- **Log levels**: DEBUG, INFO, WARNING, ERROR

**Using Logger**:
```python
from backend.logger import logger

logger.info("Information message")
logger.debug("Debug information")
logger.warning("Warning message")
logger.error("Error occurred", exc_info=True)
```

### Rate Limiting

Add rate limiting to any endpoint:

```python
from fastapi import Depends
from backend.rate_limiter.depends import RateLimiter

@app.get("/api/limited")
async def limited_endpoint(_=Depends(RateLimiter(times=10, seconds=60))):
    return {"message": "Success"}
```

Parameters:
- `times`: Number of requests allowed
- `seconds`, `minutes`, `hours`: Time window
- `milliseconds`: Fine-grained control

### Caching

Use the cache manager across your application:

```python
from backend.cache import get_cache_manager

cache = get_cache_manager()

# Set a value
cache.set("user:123", {"name": "John", "email": "john@example.com"})

# Get a value
user = cache.get("user:123")

# Increment counter
cache.increment("page_views", 1)

# Delete
cache.delete("user:123")

# Check existence
if cache.exists("user:123"):
    print("User found")
```

## 🎨 Project Features

### Authentication System
- JWT-based token authentication
- Refresh token rotation
- Password hashing with bcrypt
- Token revocation and session management
- Rate-limited login endpoints

### Rate Limiting
- Per-endpoint rate limits
- IP-based and custom identifiers
- Configurable time windows
- WebSocket support
- Detailed logging

### Caching
- TTL-based in-memory caching
- LRU cache support
- Thread-safe operations
- Automatic expiration
- Comprehensive API

### Logging
- Structured logging throughout
- File and console output
- Multiple log levels
- Request/response tracking
- Error logging with stack traces

## 🏗️ Building for Production

### Backend

```bash
cd backend

# Build Docker image
docker build -t webapp-backend .

# Run with production settings
poetry run uvicorn backend.api:api --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend

# Build production bundle
npm run build

# Output is in ./build directory
# Serve with Node.js
npm run start

# Or with Docker
docker build -t webapp-frontend .
docker run -p 3000:3000 webapp-frontend
```

### Environment Variables

**Backend** (`backend/.env`):
```env
DATABASE_URL=postgresql://user:password@localhost:5432/webapp
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
```

**Frontend** (`.env`):
```env
VITE_API_URL=https://api.example.com
```

## 📚 Documentation

### Build Documentation

```bash
poetry run python scripts/build_backend_docs.py build
```

### Serve Documentation

```bash
poetry run python scripts/build_backend_docs.py serve --port 9000
```

Then visit `http://localhost:9000` to view the docs.

### API Documentation

FastAPI automatically generates interactive documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing

### Backend Tests

```bash
cd backend
poetry run pytest tests/
```

### Frontend Tests

```bash
cd frontend
npm run test
```

## 📝 Best Practices

1. **Database Migrations**: Use Alembic for schema changes (set up separately)
2. **Environment Variables**: Never commit `.env` files, use `.env.example`
3. **Logging**: Use the provided logger for all important operations
4. **Rate Limiting**: Protect sensitive endpoints with rate limiting
5. **Caching**: Cache expensive database queries
6. **API Versioning**: Use `/api/v1` prefix for future compatibility
7. **Frontend Optimization**: Use code splitting and lazy loading

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Follow the existing code style
3. Add appropriate logging
4. Test your changes
5. Commit with clear messages: `git commit -m "Add feature description"`
6. Push and create a Pull Request

## 📄 License

This project is provided as a template. Customize the license as needed.

## 🆘 Troubleshooting

### Backend won't start
- Check Python version: `python --version` (should be 3.12+)
- Verify Poetry installation: `poetry --version`
- Reinstall dependencies: `cd backend && poetry install`

### Frontend won't start
- Check Node version: `node --version` (should be 20+)
- Clear npm cache: `npm cache clean --force`
- Reinstall dependencies: `cd frontend && rm -rf node_modules && npm install`

### procmux not working
- Install via pip: `pip install procmux` or brew: `brew install procmux`
- Check `procmux.yaml` syntax and file exists
- Verify `procs` section is defined in config
- Run with default config: `procmux` (looks for `procmux.yaml` in current directory)
- Check process logs in the terminal pane for errors
- Ensure commands work individually before adding to procmux

### Database connection issues
- Ensure PostgreSQL is running
- Check DATABASE_URL in environment
- Verify credentials and host


# License

GNU General Public License v3.0

