import { useAuth } from "../auth/useAuth";

export function MainLayout({ children }: { children: React.ReactNode }) {
  const { user, logout } = useAuth();

  return (
    <div>
      <header>
        <span>{user?.email}</span>
        <button onClick={logout}>Salir</button>
      </header>

      <main>{children}</main>
    </div>
  );
}
