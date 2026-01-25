# Frontend Boilerplate - Quick Summary

## What's Been Created

A complete, production-ready React frontend with:

### 📁 Core Structure
- **routes/** - Page components (home, login, register, dashboard)
- **components/** - Reusable UI components (Button, Input, Card, etc.)
- **lib/** - Utilities and helpers (API client, auth, hooks, utils)
- **services/** - API service classes (example structure)

### 🔐 Authentication
- Login page with form validation
- Registration with password strength checking
- Token-based authentication
- Protected routes with `useAuthRequired()` hook
- Auth utilities: `getAuthToken()`, `setAuthToken()`, `clearAuthToken()`, `isAuthenticated()`

### 🎨 Components
Pre-built, styled components ready to use:
- `Button` - Primary, secondary, danger variants with loading state
- `Input` - With label and error support
- `Card` - Reusable card container
- `Alert` - Success, error, warning, info types
- `Loader` - Spinning loader animation
- `Header` - Navigation bar with auth-aware links
- `Footer` - Footer component

### 🪝 Custom Hooks
- `useApi(method, endpoint)` - API calls with loading/error states
- `useAuth()` - Check authentication status
- `useAuthRequired()` - Protect routes automatically
- `useForm(initialValues, onSubmit)` - Complete form handling

### 🛠️ Utilities
- `formatError()` - Convert errors to readable strings
- `debounce()` - Debounce function calls
- `throttle()` - Throttle function calls
- `delay()` - Promise-based delay
- `formatDate()` & `formatDateTime()` - Date formatting
- `isValidEmail()` - Email validation
- `validatePasswordStrength()` - Password strength checking
- `toQueryString()` - Build query strings
- `cn()` - Class name utility (like classnames)

### ⚙️ Services
Example API services to follow:
- `AuthService` - Login, register, logout, refresh token
- `UserService` - CRUD operations for users

### 📋 Configuration
- Environment variables (.env.example)
- Tailwind CSS with custom colors
- TypeScript with path aliases (~/* → app/*)
- React Router v7 with proper route structure

## Pages Ready to Use

| Route | Purpose |
|-------|---------|
| `/` | Home/welcome page with navigation |
| `/login` | Login form with email/password |
| `/register` | Registration with password strength |
| `/dashboard` | Protected route (requires login) |

## Quick Start

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment:**
   ```bash
   cp .env.example .env.local
   # Update VITE_API_URL to match your backend
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

4. **Access the app:**
   - Navigate to http://localhost:5173
   - Try logging in or registering
   - Check out the dashboard (protected route)

## API Integration

The frontend expects a backend at `http://localhost:8000` (configurable).

**Expected endpoints:**
- `POST /auth/login` - Login
- `POST /auth/register` - Register
- `GET /auth/me` - Get current user
- `POST /auth/logout` - Logout

## Example: Making an API Call

```typescript
import { useApi } from "~/lib/hooks";

export function MyComponent() {
  const { data, loading, error, execute } = useApi(
    "GET",
    "/api/users",
    { autoFetch: true }
  );

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return <div>{JSON.stringify(data)}</div>;
}
```

## Example: Protecting Routes

```typescript
import { useAuthRequired } from "~/lib/hooks";

export default function ProtectedPage() {
  const { isAuthenticated, isChecking } = useAuthRequired();

  if (isChecking) return <Loader />;
  if (!isAuthenticated) return null;

  return <div>This is a protected page</div>;
}
```

## Next Steps

1. **Customize styling** - Update `tailwind.config.ts` and components
2. **Add more routes** - Create new pages in `routes/` folder
3. **Implement backend endpoints** - Match the expected API structure
4. **Add more services** - Create service classes for each resource
5. **Add tests** - Set up testing with Vitest
6. **Deploy** - Build and deploy to production

## File Structure at a Glance

```
frontend/
├── app/
│   ├── routes/              # Pages
│   │   ├── home.tsx
│   │   ├── login.tsx
│   │   ├── register.tsx
│   │   └── dashboard.tsx
│   ├── components/          # Reusable components
│   │   ├── common.tsx      # UI components
│   │   └── layout.tsx      # Header & Footer
│   ├── lib/                # Utilities
│   │   ├── api.ts          # API client
│   │   ├── auth.ts         # Auth utilities
│   │   ├── hooks.ts        # Custom hooks
│   │   ├── utils.ts        # Helpers
│   │   └── constants.ts    # App constants
│   ├── services/           # API services
│   │   ├── auth.service.ts
│   │   └── user.service.ts
│   ├── root.tsx            # Root layout
│   ├── routes.ts           # Route config
│   └── app.css             # Global styles
├── .env.example            # Environment template
├── tailwind.config.ts      # Tailwind config
├── vite.config.ts          # Vite config
├── tsconfig.json           # TypeScript config
└── package.json            # Dependencies
```

---

**Everything is ready to go!** Start the development server and build your app on top of this solid foundation.
