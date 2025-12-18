import { useEffect, useState } from "react";
import { AuthContext } from "./AuthContext";
import type { User } from "./auth.types";
import api from "../api/axios";

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  const login = async (email: string, password: string) => {
    const res = await api.post("/auth/login", { email, password });
    localStorage.setItem("access_token", res.data.access_token);

    const me = await api.get<User>("/users/me");
    setUser(me.data);
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setUser(null);
  };

  // 👇 CARGA AUTOMÁTICA DE SESIÓN
  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      setLoading(false);
      return;
    }

    api
      .get<User>("/users/me")
      .then((res) => setUser(res.data))
      .catch(() => localStorage.removeItem("access_token"))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Cargando sesión...</p>;

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
