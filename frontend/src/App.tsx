import { AppRouter } from "./routes/AppRouter";
import { AuthProvider } from "./auth/AuthProvider";

export default function App() {
  return (
    <AuthProvider>
      <AppRouter />
    </AuthProvider>
  );
}
