/**
 * Example API Service
 * 
 * This demonstrates how to structure API calls for different resources.
 * Copy this pattern for other resources.
 */

import { apiClient } from "../lib/api";
import { API_ENDPOINTS } from "../lib/constants";

export interface AuthResponse {
  access_token: string;
  token_type?: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  name: string;
  email: string;
  password: string;
}

export class AuthService {
  static async login(credentials: LoginRequest): Promise<AuthResponse> {
    return apiClient.post<AuthResponse>(
      API_ENDPOINTS.AUTH.LOGIN,
      credentials
    );
  }

  static async register(data: RegisterRequest): Promise<AuthResponse> {
    return apiClient.post<AuthResponse>(
      API_ENDPOINTS.AUTH.REGISTER,
      data
    );
  }

  static async logout(): Promise<void> {
    return apiClient.post<void>(API_ENDPOINTS.AUTH.LOGOUT);
  }

  static async getMe() {
    return apiClient.get(API_ENDPOINTS.AUTH.ME);
  }

  static async refreshToken(): Promise<AuthResponse> {
    return apiClient.post<AuthResponse>(API_ENDPOINTS.AUTH.REFRESH);
  }
}
