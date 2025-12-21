import api from "./axios";
import type { LoginResponse, User } from "../types/auth";

export const login = async (
  email: string,
  password: string
): Promise<LoginResponse> => {
  const { data } = await api.post("/auth/login", {
    email,
    password,
  });

  return data;
};

export const getCurrentUser = async (): Promise<User> => {
  const { data } = await api.get("/users/me");
  return data;
};
