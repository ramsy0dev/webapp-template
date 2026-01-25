/**
 * Frontend Project Documentation
 * 
 * This is a modern React + TypeScript frontend built with Vite and React Router v7.
 */

# Frontend Boilerplate

A modern, production-ready React frontend with authentication, API integration, and TypeScript support.

## Quick Start

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### Build

```bash
npm run build
```

### Type Checking

```bash
npm run typecheck
```

## Project Structure

```
app/
├── routes/                 # Page components and routes
│   ├── home.tsx           # Home/welcome page
│   ├── login.tsx          # Login page
│   ├── register.tsx       # Registration page
│   ├── dashboard.tsx      # Protected dashboard
│   └── +types/            # Route-specific types (auto-generated)
├── components/            # Reusable UI components
│   ├── common.tsx         # Button, Input, Card, etc.
│   └── layout.tsx         # Header and Footer
├── lib/                   # Utilities and helpers
│   ├── api.ts            # API client setup
│   ├── auth.ts           # Authentication utilities
│   ├── hooks.ts          # Custom React hooks
│   └── utils.ts          # General utilities
├── welcome/              # Welcome component
├── root.tsx              # Root layout
├── app.css               # Global styles
└── routes.ts             # Route configuration
```

## Key Features

### Authentication
- Login and registration flows
- Token-based authentication
- Protected routes with `useAuthRequired()` hook
- Automatic redirect to login for unauthenticated users

### API Client
- Centralized API client with `apiClient`
- Support for GET, POST, PUT, PATCH, DELETE
- Automatic error handling
- Request/response interceptors ready

### Components
- Pre-built UI components: Button, Input, Card, Alert, Loader
- Consistent styling with Tailwind CSS
- Loading states and error handling

### Hooks
- `useApi()` - Handle API requests with loading and error states
- `useAuth()` - Check authentication status
- `useAuthRequired()` - Protect routes
- `useForm()` - Handle form state and submissions

### Utilities
- Password validation and strength checking
- Email validation
- Date formatting
- Debounce and throttle functions
- Query string builder
- Class name utility (similar to classnames)

## Configuration

### Environment Variables

Create a `.env.local` file based on `.env.example`:

```
VITE_API_URL=http://localhost:8000
```

### Tailwind CSS

Tailwind CSS is pre-configured with custom colors and fonts. Customize in `tailwind.config.ts`.

### TypeScript

TypeScript configuration is in `tsconfig.json` with path aliases for cleaner imports:
- `~/*` → `./app/*`

## Styling

- **Framework**: Tailwind CSS 4.x
- **CSS-in-JS**: Not used (Tailwind utilities + CSS modules)
- **Responsive**: Mobile-first responsive design

## Available Routes

- `/` - Home/welcome page
- `/login` - Login page
- `/register` - Registration page
- `/dashboard` - Protected dashboard (requires authentication)

## API Integration

The frontend connects to the backend API at `http://localhost:8000` by default.

Example API call:

```typescript
import { apiClient } from "~/lib/api";

const data = await apiClient.get("/api/endpoint");
const result = await apiClient.post("/api/endpoint", { key: "value" });
```

## Authentication Flow

1. User registers or logs in
2. Backend returns access token
3. Token is stored in localStorage
4. Token is sent with subsequent API requests
5. Protected routes check authentication status
6. User is redirected to login if not authenticated

## Development Tips

### Adding New Pages

1. Create a new route file in `app/routes/`
2. Update `app/routes.ts` to include the new route
3. Use React Router's `<Link>` for navigation

### Adding New Components

1. Create component in `app/components/`
2. Export from component file
3. Import and use in routes or other components

### Making API Calls

Use the `useApi()` hook for automatic loading and error states:

```typescript
const { data, loading, error, execute } = useApi(
  "GET",
  "/api/users",
  { autoFetch: true }
);
```

### Protected Routes

Use `useAuthRequired()` to protect routes:

```typescript
export default function ProtectedPage() {
  const { isAuthenticated, isChecking } = useAuthRequired();
  
  if (isChecking) return <Loader />;
  if (!isAuthenticated) return null;
  
  return <div>Protected content</div>;
}
```

## Troubleshooting

### CORS Errors
Make sure the backend is running and `VITE_API_URL` points to the correct server.

### Authentication Issues
Check that tokens are being stored in localStorage and sent with requests.

### Build Errors
Run `npm run typecheck` to identify TypeScript issues.

## Next Steps

- Add more components to `app/components/`
- Integrate with backend API endpoints
- Add form validation
- Implement error boundaries
- Add logging
- Set up testing with Vitest

## Resources

- [React Router v7 Documentation](https://reactrouter.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)
- [TypeScript Documentation](https://www.typescriptlang.org/)
- [Vite Documentation](https://vitejs.dev/)
