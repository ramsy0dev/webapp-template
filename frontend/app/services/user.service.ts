/**
 * User Service
 */

import { apiClient } from "../lib/api";
import { API_ENDPOINTS } from "../lib/constants";

export interface UserProfile {
  id: string;
  name: string;
  email: string;
  roles?: string[];
  createdAt?: string;
  updatedAt?: string;
}

export interface UpdateUserRequest {
  name?: string;
  email?: string;
}

export class UserService {
  static async getUsers(page = 1, limit = 20) {
    return apiClient.get(
      `${API_ENDPOINTS.USERS.LIST}?page=${page}&limit=${limit}`
    );
  }

  static async getUser(id: string): Promise<UserProfile> {
    return apiClient.get<UserProfile>(API_ENDPOINTS.USERS.GET(id));
  }

  static async updateUser(
    id: string,
    data: UpdateUserRequest
  ): Promise<UserProfile> {
    return apiClient.put<UserProfile>(
      API_ENDPOINTS.USERS.UPDATE(id),
      data
    );
  }

  static async deleteUser(id: string): Promise<void> {
    return apiClient.delete<void>(API_ENDPOINTS.USERS.DELETE(id));
  }
}
