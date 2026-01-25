# Frontend - Modern React Web Application

A production-ready React frontend built with TypeScript, Vite, React Router v7, and Tailwind CSS. Includes complete authentication, API integration, and a comprehensive component library.

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm

### Installation & Development

```bash
# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Start development server
npm run dev
```

The app will be available at `http://localhost:5173`

### Build for Production

```bash
npm run build
npm run start  # Start production server
```

### Type Checking

```bash
npm run typecheck
```

## 📚 Documentation

- **[Boilerplate Summary](./BOILERPLATE_SUMMARY.md)** - Overview of what's been created
- **[Frontend Guide](./FRONTEND.md)** - Comprehensive frontend documentation
- **[Development Guide](./DEVELOPMENT_GUIDE.md)** - Best practices and conventions
- **[Style Manager](./STYLE_MANAGER.md)** - Centralized theme and style system

## 🎯 Features

### Authentication
- ✅ Login & Registration pages with validation
- ✅ Token-based authentication (JWT)
- ✅ Protected routes with automatic redirects
- ✅ Password strength validation
- ✅ Auth state management

### UI Components
- ✅ Button (primary, secondary, danger) with loading state
- ✅ Input with label and error display
- ✅ Card containers
- ✅ Alert boxes (success, error, warning, info)
- ✅ Loader spinner
- ✅ Header with navigation
- ✅ Footer component

### Custom Hooks
- ✅ `useApi()` - Handle API requests with loading/error states
- ✅ `useAuth()` - Check authentication status
- ✅ `useAuthRequired()` - Protect routes automatically
- ✅ `useForm()` - Complete form state management

### Utilities
- ✅ Email validation
- ✅ Password strength checking
- ✅ Date formatting
- ✅ Error handling
- ✅ Debounce & throttle functions
- ✅ Query string building
- ✅ Class name utility

### API Integration
- ✅ Centralized API client
- ✅ Automatic error handling
- ✅ Support for GET, POST, PUT, PATCH, DELETE
- ✅ Request/response interceptors ready
- ✅ Example service implementations

## 📁 Project Structure

```
app/
├── routes/                 # Page components
│   ├── home.tsx           # Home page
│   ├── login.tsx          # Login page
│   ├── register.tsx       # Registration page
│   ├── dashboard.tsx      # Protected dashboard
│   └── +types/            # Auto-generated types
├── components/            # Reusable components
│   ├── common.tsx         # Button, Input, Card, Alert, Loader
│   └── layout.tsx         # Header, Footer
├── lib/                   # Utilities
│   ├── api.ts            # API client
│   ├── auth.ts           # Auth utilities
│   ├── hooks.ts          # Custom React hooks
│   ├── utils.ts          # General utilities
│   └── constants.ts      # App constants
├── services/             # API service classes
│   ├── auth.service.ts   # Auth API
│   └── user.service.ts   # User API
├── root.tsx              # Root layout
├── routes.ts             # Route configuration
└── app.css               # Global styles
```

## 🛣️ Routes

| Route | Description | Protected |
|-------|-------------|-----------|
| `/` | Home/welcome page | No |
| `/login` | Login form | No |
| `/register` | Registration form | No |
| `/dashboard` | Dashboard | Yes |

## 🔐 Authentication Flow

1. User visits `/login` or `/register`
2. Enters credentials and submits form
3. Frontend sends request to backend API
4. Backend validates and returns access token
5. Token is stored in localStorage
6. Token is sent with subsequent API requests
7. Protected routes check authentication status
8. Unauthenticated users are redirected to login

## 📦 Dependencies

### Core
- **react** ^19.2.3 - UI library
- **react-router** 7.12.0 - Routing and data loading
- **@react-router/node** 7.12.0 - Server runtime
- **typescript** ^5.9.2 - Type safety

### Styling
- **tailwindcss** ^4.1.13 - Utility-first CSS
- **@tailwindcss/vite** ^4.1.13 - Vite integration

### Build Tools
- **vite** ^7.1.7 - Build tool and dev server
- **vite-tsconfig-paths** ^5.1.4 - TypeScript path aliases
- **esbuild** ^0.27.2 - JavaScript bundler

## ⚙️ Configuration

### Environment Variables

Create `.env.local`:
```
VITE_API_URL=http://localhost:8000
```

### TypeScript

Path aliases for cleaner imports:
```typescript
// Instead of: import { Button } from "../../../components/common"
import { Button } from "~/components/common";
```

### Tailwind CSS

Custom configuration in `tailwind.config.ts`:
- Custom color palette
- Font family (Inter)
- Responsive breakpoints
- Extended utilities

## 🎨 Styling Guide

### Using Tailwind

```typescript
<div className="flex flex-col md:flex-row gap-4 p-4 md:p-8">
  <p className="text-lg font-semibold text-gray-900">
    Hello World
  </p>
</div>
```

### Custom Colors

Primary colors are configured and ready to use:
```typescript
<div className="text-primary-600">Primary text</div>
<button className="bg-primary-500 hover:bg-primary-600">Button</button>
```

## 🔗 API Integration

### Basic Usage

```typescript
import { apiClient } from "~/lib/api";

// GET request
const users = await apiClient.get("/users");

// POST request
const user = await apiClient.post("/users", { name: "John" });

// PUT request
await apiClient.put("/users/1", { name: "Jane" });

// DELETE request
await apiClient.delete("/users/1");
```

### Using the useApi Hook

```typescript
import { useApi } from "~/lib/hooks";

function UserList() {
  const { data: users, loading, error } = useApi(
    "GET",
    "/users",
    { autoFetch: true }
  );

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <ul>
      {users?.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### Service Classes

Use service classes for organized API calls:

```typescript
import { AuthService } from "~/services/auth.service";

// Login
const response = await AuthService.login({
  email: "user@example.com",
  password: "password123"
});
```

## 🔒 Protected Routes

Routes that require authentication:

```typescript
import { useAuthRequired } from "~/lib/hooks";

export default function DashboardPage() {
  const { isAuthenticated, isChecking } = useAuthRequired();

  if (isChecking) return <Loader />;
  if (!isAuthenticated) return null;

  return <div>Dashboard content</div>;
}
```

The `useAuthRequired()` hook automatically:
- Checks if user is authenticated
- Redirects to login if not
- Prevents rendering until check is complete

## 📝 Forms

Complete form handling with state management:

```typescript
import { useForm } from "~/lib/hooks";
import { Input, Button } from "~/components/common";

function LoginForm() {
  const form = useForm(
    { email: "", password: "" },
    async (values) => {
      const result = await apiClient.post("/auth/login", values);
      setAuthToken(result.access_token);
      navigate("/dashboard");
    }
  );

  return (
    <form onSubmit={form.handleSubmit}>
      <Input
        label="Email"
        name="email"
        value={form.values.email}
        onChange={form.handleChange}
        onBlur={form.handleBlur}
      />
      <Input
        label="Password"
        type="password"
        name="password"
        value={form.values.password}
        onChange={form.handleChange}
        onBlur={form.handleBlur}
      />
      <Button type="submit" isLoading={form.isSubmitting}>
        Login
      </Button>
    </form>
  );
}
```

The `useForm` hook provides:
- `values` - Form field values
- `errors` - Field errors
- `touched` - Which fields have been interacted with
- `isSubmitting` - Whether form is currently submitting
- `handleChange` - Handle input changes
- `handleBlur` - Mark field as touched
- `handleSubmit` - Handle form submission
- `reset` - Reset form to initial state

## 🧪 Testing

### Run Tests

```bash
npm run test
```

### Example Test

```typescript
import { render, screen } from "@testing-library/react";
import { Button } from "~/components/common";

describe("Button", () => {
  it("renders button with text", () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText("Click me")).toBeInTheDocument();
  });
});
```

## 🚀 Deployment

### Build
```bash
npm run build
```

This creates an optimized production build in the `build/` directory.

### Environment Variables for Production
```
VITE_API_URL=https://api.example.com
```

### Hosting Options
- Vercel (recommended for React Router)
- Netlify
- AWS S3 + CloudFront
- Docker (included)

## 🐳 Docker

A Dockerfile is included for containerized deployment.

```bash
# Build image
docker build -t webapp-frontend .

# Run container
docker run -p 3000:3000 webapp-frontend
```

## 🛠️ Development Tools

### TypeScript Check
```bash
npm run typecheck
```

### Format Code (if prettier is set up)
```bash
npm run format
```

### Lint Code (if eslint is set up)
```bash
npm run lint
```

## 🤝 Contributing

When adding new features:

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Follow the [Development Guide](./DEVELOPMENT_GUIDE.md)
3. Make your changes and test them
4. Commit with clear messages: `git commit -m "Add my feature"`
5. Push and create a Pull Request

## 🐛 Troubleshooting

### CORS Errors
- Ensure backend is running at the URL in `VITE_API_URL`
- Check backend CORS configuration

### Authentication Issues
- Verify tokens are being stored in localStorage
- Check that tokens are sent in API requests
- Review browser Network tab for API responses

### Build Errors
```bash
npm run typecheck  # Check for type errors
npm install        # Reinstall dependencies
npm run build      # Try building again
```

### Port Already in Use
```bash
# Kill process on port 5173
lsof -ti:5173 | xargs kill -9

# Or use a different port
npm run dev -- --port 3000
```

## 📚 Learn More

- [React Router Documentation](https://reactrouter.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Vite Guide](https://vitejs.dev/guide/)

## 📄 License

This project is part of the webapp-template. See LICENSE file for details.

---

**Ready to build?** Check out the [Boilerplate Summary](./BOILERPLATE_SUMMARY.md) for an overview of what's been created!
