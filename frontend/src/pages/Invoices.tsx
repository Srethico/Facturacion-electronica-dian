import { useEffect, useState } from "react";
import { Container, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import { getInvoices } from "../api/invoices.api";
import type { Invoice } from "../types/invoice";

export default function Invoices() {
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    getInvoices().then(setInvoices);
  }, []);

  return (
    <>
      <Navbar />
      <Container sx={{ mt: 4 }}>
        <Button
          variant="contained"
          onClick={() => navigate("/invoices/new")}
          sx={{ mb: 2 }}
        >
          Nueva Factura
        </Button>

        {invoices.map((inv) => (
          <div key={inv.id}>
            Factura #{inv.id} — Estado: {inv.status}
          </div>
        ))}
      </Container>
    </>
  );
}
