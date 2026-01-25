/**
 * Development Guidelines
 * 
 * Best practices and conventions for this project
 */

# Frontend Development Guidelines

## Code Organization

### Components
- Keep components in `app/components/`
- One component per file (except for very small related components)
- Use descriptive names
- Export as default for page components, named export for reusable components

```typescript
// ✅ Good
// app/components/UserCard.tsx
export function UserCard({ user }: Props) {
  return <div>...</div>;
}

// app/routes/users.tsx
import { UserCard } from "~/components/UserCard";
```

### Routes
- Create route files in `app/routes/`
- Register routes in `app/routes.ts`
- Use `export const meta` for page titles and metadata
- Protect routes with `useAuthRequired()` hook

```typescript
// ✅ Good
export const meta: Route.MetaArgs = () => [
  { title: "Users - App" },
  { name: "description", content: "User management page" },
];

export default function UsersPage() {
  const { isAuthenticated, isChecking } = useAuthRequired();
  // ...
}
```

### Services
- Create services in `app/services/`
- Group related API calls by resource
- Use static methods for simplicity
- Type request and response data

```typescript
// ✅ Good
export class UserService {
  static async getUsers(): Promise<User[]> {
    return apiClient.get<User[]>("/users");
  }

  static async getUser(id: string): Promise<User> {
    return apiClient.get<User>(`/users/${id}`);
  }
}
```

### Utilities
- Place utility functions in `app/lib/utils.ts`
- Keep functions pure (no side effects)
- Write JSDoc comments
- Add unit tests

```typescript
// ✅ Good
/**
 * Format a date to MM/DD/YYYY format
 * @param date - The date to format
 * @returns Formatted date string
 */
export function formatDate(date: Date | string): string {
  const d = new Date(date);
  return d.toLocaleDateString("en-US");
}
```

## TypeScript Conventions

### Type Definitions
- Use interfaces for objects
- Use type for unions and primitives
- Keep types in the same file or create `types.ts` files

```typescript
// ✅ Good
interface User {
  id: string;
  name: string;
  email: string;
}

type Status = "active" | "inactive" | "pending";
```

### Imports
- Use path aliases: `~/` → `./app/`
- Group imports: external, internal, types
- Sort alphabetically within groups

```typescript
// ✅ Good
import { useState } from "react";
import { Link } from "react-router";

import { Button } from "~/components/common";
import { useAuth } from "~/lib/hooks";

import type { User } from "~/lib/auth";
```

## State Management

### useState
- Use for local component state
- Keep state close to where it's used
- Combine related state into objects

```typescript
// ✅ Good
const [user, setUser] = useState<User | null>(null);
const [isLoading, setIsLoading] = useState(false);

// ❌ Avoid
const [userLoading, setUserLoading] = useState(false);
const [userError, setUserError] = useState("");
```

### useApi Hook
- Use for API calls with automatic loading/error handling
- Set `autoFetch: false` if you need manual control

```typescript
// ✅ Good
const { data: users, loading, error } = useApi(
  "GET",
  "/users",
  { autoFetch: true }
);
```

## Error Handling

### API Errors
- Use `try-catch` with `useApi()`
- Format errors with `formatError()` utility
- Show user-friendly error messages

```typescript
// ✅ Good
try {
  await apiClient.post("/login", credentials);
} catch (error) {
  setError(formatError(error));
}
```

### Component Errors
- Use React error boundaries for critical errors
- Log errors to console in development
- Show graceful fallback UI

## Forms

### useForm Hook
- Use for all forms to get: values, errors, touched, isSubmitting
- Handle submission with async function
- Validate before submission

```typescript
// ✅ Good
const form = useForm(
  { email: "", password: "" },
  async (values) => {
    try {
      await authService.login(values);
      navigate("/dashboard");
    } catch (error) {
      // Handle error
    }
  }
);

return (
  <form onSubmit={form.handleSubmit}>
    <Input
      name="email"
      value={form.values.email}
      onChange={form.handleChange}
      onBlur={form.handleBlur}
    />
  </form>
);
```

## Styling

### Tailwind CSS
- Use utility classes for styling
- Avoid inline styles
- Create components for repeated patterns
- Use responsive prefixes: sm:, md:, lg:, xl:

```typescript
// ✅ Good
<div className="flex flex-col md:flex-row gap-4 p-4 md:p-8">
  {children}
</div>

// ❌ Avoid
<div style={{ display: "flex", gap: "1rem", padding: "1rem" }}>
  {children}
</div>
```

### Custom CSS
- Use CSS modules only when necessary
- Keep styles close to components
- Use semantic class names

## Performance

### Memoization
- Use `useMemo` for expensive computations
- Use `useCallback` for handler functions passed to children
- Don't over-optimize prematurely

```typescript
// ✅ Good
const filteredUsers = useMemo(
  () => users.filter(user => user.active),
  [users]
);
```

### Code Splitting
- React Router handles route-based code splitting automatically
- Use lazy imports for heavy components if needed

```typescript
// ✅ Good
const HeavyComponent = lazy(() => import("~/components/HeavyComponent"));
```

## Testing

### Unit Tests
- Test utility functions thoroughly
- Test component behavior, not implementation
- Use descriptive test names

```typescript
// ✅ Good
describe("formatDate", () => {
  it("should format date as MM/DD/YYYY", () => {
    const result = formatDate(new Date("2024-01-15"));
    expect(result).toBe("01/15/2024");
  });
});
```

### Component Tests
- Test user interactions
- Test conditional rendering
- Test error states

## Accessibility

### HTML
- Use semantic HTML: `<button>`, `<nav>`, `<main>`, etc.
- Always use `<label>` with form inputs
- Include `alt` text for images

```typescript
// ✅ Good
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// ❌ Avoid
<input type="email" placeholder="Email" />
```

### Keyboard Navigation
- All interactive elements should be keyboard accessible
- Use tab order wisely
- Support Enter and Space keys

### Color & Contrast
- Ensure sufficient color contrast
- Don't rely solely on color to convey information
- Test with accessibility tools

## Naming Conventions

### Files
- Use PascalCase for components: `UserCard.tsx`
- Use camelCase for utilities: `formatDate.ts`
- Use kebab-case for routes: `user-profile.tsx`

### Functions/Variables
- Use camelCase: `getUserList`, `isActive`
- Use PascalCase for components: `UserCard`
- Use ALL_CAPS for constants: `MAX_USERS`

### Event Handlers
- Prefix with `handle`: `handleClick`, `handleSubmit`
- Use specific names: `handleDeleteUser` not `handleClick`

## Comments

### JSDoc
- Document public functions with JSDoc
- Include parameter types and return types
- Add examples for complex functions

```typescript
/**
 * Fetch a user by ID
 * @param userId - The user's unique identifier
 * @returns The user object or null if not found
 * @example
 * const user = await getUser("123");
 */
async function getUser(userId: string): Promise<User | null> {
  // ...
}
```

### Inline Comments
- Explain "why", not "what"
- Keep comments up-to-date with code
- Use sparingly; code should be self-documenting

```typescript
// ✅ Good
// Cache user data to reduce API calls
const cachedUser = useMemo(() => getUserData(), [userId]);

// ❌ Avoid
// Set user to cachedUser
const cachedUser = useMemo(() => getUserData(), [userId]);
```

## Git Workflow

### Commit Messages
- Use imperative mood: "Add feature" not "Added feature"
- Be descriptive but concise
- Reference issue numbers when applicable

```
✅ Good
- Add login page with email validation
- Fix header navigation on mobile
- Update user profile form

❌ Avoid
- fix bugs
- update
- changes
```

### Branch Names
- Use kebab-case: `feature/login-page`, `fix/header-mobile`
- Start with type: `feature/`, `fix/`, `refactor/`, `docs/`

## Environment Variables

### Usage
- Prefix with `VITE_` for frontend variables
- Keep sensitive data on backend
- Document all variables in `.env.example`

```typescript
// ✅ Good in frontend
const apiUrl = import.meta.env.VITE_API_URL;

// ❌ Never do this
const apiKey = import.meta.env.VITE_SECRET_KEY;
```

## Debugging

### Console
- Remove debug logs before committing
- Use appropriate log levels: log, warn, error
- Use descriptive messages

```typescript
// ✅ Good
console.error("Failed to fetch user:", error);

// ❌ Avoid
console.log("error");
console.log(data);
```

### DevTools
- Use React Developer Tools extension
- Use Network tab to inspect API calls
- Check console for errors and warnings

## Common Patterns

### Fetching Data on Mount
```typescript
const { data } = useApi("GET", "/users", { autoFetch: true });
```

### Handling Form Submission
```typescript
const form = useForm(initialValues, async (values) => {
  await service.save(values);
});
```

### Protected Routes
```typescript
const { isAuthenticated, isChecking } = useAuthRequired();
if (isChecking) return <Loader />;
if (!isAuthenticated) return null;
```

### Conditional Rendering
```typescript
{isLoading && <Loader />}
{error && <Alert type="error">{error}</Alert>}
{data && <UserList users={data} />}
```

---

Follow these guidelines to maintain code quality and consistency throughout the project!
