/**
 * Register Page
 */

import { useState } from "react";
import { useNavigate, Link } from "react-router";
import type { Route } from "./+types/register";
import { Button } from "../components/common";
import { Input } from "../components/common";
import { Alert } from "../components/common";
import { useForm } from "../lib/hooks";
import { apiClient } from "../lib/api";
import { setAuthToken } from "../lib/auth";
import { formatError, validatePasswordStrength } from "../lib/utils";

export const meta: Route.MetaArgs = ({ location }) => [
  { title: "Register - webapp-template" },
  { name: "description", content: "Create a new account" },
];

interface RegisterData {
  name: string;
  email: string;
  password: string;
  confirmPassword: string;
}

export default function RegisterPage() {
  const navigate = useNavigate();
  const [serverError, setServerError] = useState<string | null>(null);

  const form = useForm<RegisterData>(
    {
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
    },
    async (values) => {
      setServerError(null);

      // Validate passwords match
      if (values.password !== values.confirmPassword) {
        setServerError("Passwords do not match");
        return;
      }

      // Validate password strength
      const passwordValidation = validatePasswordStrength(values.password);
      if (!passwordValidation.isStrong) {
        setServerError(
          `Password is too weak. ${passwordValidation.feedback.join(". ")}`
        );
        return;
      }

      try {
        const response = await apiClient.post<{ access_token: string }>(
          "/auth/register",
          {
            name: values.name,
            email: values.email,
            password: values.password,
          }
        );

        if (response.access_token) {
          setAuthToken(response.access_token);
          navigate("/dashboard");
        }
      } catch (error) {
        setServerError(formatError(error));
      }
    }
  );

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full bg-white rounded-lg shadow-md p-8">
        <h2 className="text-3xl font-bold text-center mb-8">Register</h2>

        {serverError && (
          <Alert type="error" className="mb-6">
            {serverError}
          </Alert>
        )}

        <form onSubmit={form.handleSubmit} className="space-y-4">
          <Input
            label="Name"
            type="text"
            name="name"
            placeholder="John Doe"
            value={form.values.name}
            onChange={form.handleChange}
            onBlur={form.handleBlur}
            required
          />

          <Input
            label="Email"
            type="email"
            name="email"
            placeholder="you@example.com"
            value={form.values.email}
            onChange={form.handleChange}
            onBlur={form.handleBlur}
            required
          />

          <Input
            label="Password"
            type="password"
            name="password"
            placeholder="••••••••"
            value={form.values.password}
            onChange={form.handleChange}
            onBlur={form.handleBlur}
            required
          />

          <Input
            label="Confirm Password"
            type="password"
            name="confirmPassword"
            placeholder="••••••••"
            value={form.values.confirmPassword}
            onChange={form.handleChange}
            onBlur={form.handleBlur}
            required
          />

          <Button
            type="submit"
            isLoading={form.isSubmitting}
            className="w-full"
          >
            Register
          </Button>
        </form>

        <p className="text-center text-sm text-gray-600 mt-6">
          Already have an account?{" "}
          <Link to="/login" className="text-blue-600 hover:text-blue-700">
            Login here
          </Link>
        </p>
      </div>
    </div>
  );
}
