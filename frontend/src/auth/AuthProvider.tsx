import { useEffect, useState } from "react";
import { AuthContext } from "./AuthContext";
import type { User } from "./auth.types";
import api from "../api/api";

interface Props {
  children: React.ReactNode;
}

export function AuthProvider({ children }: Props) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // =========================
  // LOGIN REAL (JWT)
  // =========================
  const login = async (email: string, password: string) => {
    try {
      const res = await api.post("/auth/login", { email, password });

      localStorage.setItem("access_token", res.data.access_token);

      const me = await api.get<User>("/users/me");
      setUser(me.data);
    } catch (error) {
      localStorage.removeItem("access_token");
      throw error; // 👈 importante para mostrar error en UI
    }
  };

  // =========================
  // LOGOUT
  // =========================
  const logout = () => {
    localStorage.removeItem("access_token");
    setUser(null);
  };

  // =========================
  // CARGA AUTOMÁTICA DE SESIÓN
  // =========================
  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      setLoading(false);
      return;
    }

    api
      .get<User>("/users/me")
      .then((res) => setUser(res.data))
      .catch(() => {
        localStorage.removeItem("access_token");
        setUser(null);
      })
      .finally(() => setLoading(false));
  }, []);

  // =========================
  // RENDER
  // =========================
  if (loading) return null; // 👈 limpio y profesional

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
