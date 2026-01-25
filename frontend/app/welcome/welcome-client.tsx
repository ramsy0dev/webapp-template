/**
 * Client-side Welcome Component
 * Handles auth-dependent button display
 */

"use client";

import { useEffect, useState } from "react";
import { Link } from "react-router";
import { Button } from "~/components/common";
import { getAuthToken } from "~/lib/auth";

export function WelcomeClient() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsAuthenticated(!!getAuthToken());
    setIsLoading(false);
  }, []);

  if (isLoading) {
    return <div className="h-12" />; // Placeholder while checking auth
  }

  return (
    <div className="flex gap-4">
      {isAuthenticated ? (
        <Link to="/dashboard">
          <Button size="lg">Go to Dashboard</Button>
        </Link>
      ) : (
        <>
          <Link to="/login">
            <Button size="lg">Login</Button>
          </Link>
          <Link to="/register">
            <Button size="lg" variant="secondary">
              Register
            </Button>
          </Link>
        </>
      )}
    </div>
  );
}
