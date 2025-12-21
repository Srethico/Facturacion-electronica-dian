import { Link } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

export default function Navbar() {
  const { logout } = useAuth();

  return (
    <nav>
      <Link to="/">Dashboard</Link> |{" "}
      <Link to="/products">Productos</Link> |{" "}
      <button onClick={logout}>Salir</button>
    </nav>
  );
}
