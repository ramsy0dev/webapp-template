/**
 * Login Page
 */

import { useState } from "react";
import { useNavigate, Link } from "react-router";
import type { Route } from "./+types/login";
import { Button } from "../components/common";
import { Input } from "../components/common";
import { Alert } from "../components/common";
import { useForm } from "../lib/hooks";
import { apiClient } from "../lib/api";
import { setAuthToken } from "../lib/auth";
import { formatError } from "../lib/utils";

export const meta: Route.MetaArgs = () => [
  { title: "Login - webapp-template" },
  { name: "description", content: "Login to your account" },
];

interface LoginData {
  email: string;
  password: string;
}

export default function LoginPage() {
  const navigate = useNavigate();
  const [serverError, setServerError] = useState<string | null>(null);

  const form = useForm<LoginData>(
    {
      email: "",
      password: "",
    },
    async (values) => {
      setServerError(null);

      try {
        const response = await apiClient.post<{ access_token: string }>(
          "/auth/login",
          values
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
        <h2 className="text-3xl font-bold text-center mb-8">Login</h2>

        {serverError && (
          <Alert type="error" className="mb-6">
            {serverError}
          </Alert>
        )}

        <form onSubmit={form.handleSubmit} className="space-y-4">
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

          <Button
            type="submit"
            isLoading={form.isSubmitting}
            className="w-full"
          >
            Login
          </Button>
        </form>

        <p className="text-center text-sm text-gray-600 mt-6">
          Don't have an account?{" "}
          <Link to="/register" className="text-blue-600 hover:text-blue-700">
            Register here
          </Link>
        </p>
      </div>
    </div>
  );
}
