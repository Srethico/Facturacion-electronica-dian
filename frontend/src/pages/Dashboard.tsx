import { useAuth } from "../auth/useAuth";

export function Dashboard() {
  const { user, logout } = useAuth();

  return (
    <div>
      <h1 className="text-3xl font-bold text-blue-600">
  Dashboard
</h1>

      <p>Bienvenido {user?.email}</p>
      <button onClick={logout}>Cerrar sesión</button>
    </div>
  );
}
