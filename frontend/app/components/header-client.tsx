/**
 * Client-side Header Navigation
 * This component handles client-only auth checks using hooks
 */

"use client";

import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router";
import { clearAuthToken, getAuthToken } from "~/lib/auth";
import { Button } from "./common";

export function HeaderClient() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    // Check authentication status on client mount
    setIsAuthenticated(!!getAuthToken());
  }, []);

  const handleLogout = () => {
    clearAuthToken();
    setIsAuthenticated(false);
    navigate("/login");
  };

  return (
    <div className="flex gap-4">
      {isAuthenticated ? (
        <>
          <Link
            to="/dashboard"
            className="text-gray-700 hover:text-gray-900 font-medium"
          >
            Dashboard
          </Link>
          <Button onClick={handleLogout} variant="secondary" size="sm">
            Logout
          </Button>
        </>
      ) : (
        <>
          <Link
            to="/login"
            className="text-gray-700 hover:text-gray-900 font-medium"
          >
            Login
          </Link>
          <Link
            to="/register"
            className="text-gray-700 hover:text-gray-900 font-medium"
          >
            Register
          </Link>
        </>
      )}
    </div>
  );
}
