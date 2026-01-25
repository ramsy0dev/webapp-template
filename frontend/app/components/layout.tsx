/**
 * Header/Navigation Component
 */

import { Link } from "react-router";
import { HeaderClient } from "./header-client";

export function Header() {
  return (
    <header className="bg-white shadow-sm">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
        <Link to="/" className="text-2xl font-bold text-blue-600">
          webapp-template
        </Link>

        <HeaderClient />
      </nav>
    </header>
  );
}

export function Footer() {
  return (
    <footer className="bg-gray-100 py-8 mt-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <p className="text-gray-600 text-sm">
            © {new Date().getFullYear()} webapp-template. All rights reserved.
          </p>
          <div className="flex gap-6 mt-4 md:mt-0">
            <a href="#" className="text-gray-600 hover:text-gray-900 text-sm">
              Privacy
            </a>
            <a href="#" className="text-gray-600 hover:text-gray-900 text-sm">
              Terms
            </a>
            <a href="#" className="text-gray-600 hover:text-gray-900 text-sm">
              Contact
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}
