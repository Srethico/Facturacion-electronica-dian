import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Products from "./pages/Products";
import Invoices from "./pages/Invoices";
import InvoiceCreate from"./pages/InvoiceCreate";
import { AuthProvider } from "./auth/AuthContext";
import PrivateRoute from "./auth/PrivateRoute";
import RequireAdmin from "./auth/RequireAdmin";

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* PUBLIC */}
          <Route path="/login" element={<Login />} />

          {/* DEFAULT */}
          <Route
            path="/"
            element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            }
          />

          {/* ADMIN */}
          <Route
            path="/products"
            element={
              <RequireAdmin>
                <Products />
              </RequireAdmin>
            }
          />

          <Route
            path="/invoices"
            element={
              <RequireAdmin>
                <Invoices />
              </RequireAdmin>
            }
          />

          <Route
            path="/invoices/new"
            element={
              <RequireAdmin>
                <InvoiceCreate />
              </RequireAdmin>
            }
          />

          {/* FALLBACK */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
