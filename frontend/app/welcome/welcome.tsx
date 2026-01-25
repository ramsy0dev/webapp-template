import { Link } from "react-router";
import { Button } from "~/components/common";
import { WelcomeClient } from "./welcome-client";

export function Welcome() {
  return (
    <main className="flex flex-col items-center justify-center pt-24 pb-12 px-4">
      <h1 className="text-5xl md:text-7xl font-extrabold leading-tight tracking-tight text-gray-900 mb-6">
        webapp-template
      </h1>

      <p className="text-xl text-gray-600 mb-12 max-w-2xl text-center">
        A modern full-stack web application template with authentication, API integration, and a professional UI.
      </p>

      <WelcomeClient />

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16 max-w-5xl w-full">
        <div className="text-center">
          <div className="text-4xl mb-4">⚡</div>
          <h3 className="text-lg font-semibold mb-2">Fast & Modern</h3>
          <p className="text-gray-600">Built with React, TypeScript, and Vite for optimal performance</p>
        </div>

        <div className="text-center">
          <div className="text-4xl mb-4">🔒</div>
          <h3 className="text-lg font-semibold mb-2">Secure</h3>
          <p className="text-gray-600">Authentication and authorization built-in with protected routes</p>
        </div>

        <div className="text-center">
          <div className="text-4xl mb-4">📦</div>
          <h3 className="text-lg font-semibold mb-2">Complete</h3>
          <p className="text-gray-600">Full-stack template with frontend, backend, and database setup</p>
        </div>
      </div>
    </main>
  );
}

