import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext";
import { Box, Typography } from "@mui/material";
import type { ReactNode } from "react";

export default function RequireAdmin({
  children,
}: {
  children: ReactNode;
}) {
  const { user, loading } = useAuth();

  if (loading) {
    return null; // aquí NO es crítico, ya pasó PrivateRoute
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (user.role !== "admin") {
    return (
      <Box sx={{ p: 4 }}>
        <Typography variant="h5" color="error">
          Acceso denegado
        </Typography>
        <Typography>
          No tienes permisos de administrador.
        </Typography>
      </Box>
    );
  }

  return children;
}
