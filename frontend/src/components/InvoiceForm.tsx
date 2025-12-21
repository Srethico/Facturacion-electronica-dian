import { useEffect, useState } from "react";
import { Paper, Button, TextField } from "@mui/material";
import { createInvoice } from "../api/invoices.api";
import { getClients } from "../api/clients.api";
import { getProducts } from "../api/products.api";
import type { Client } from "../types/client";
import type { Product } from "../types/product";
import  InvoiceItemsTable from "./InvoiceItemsTable";

export default function InvoiceForm() {
  const [clients, setClients] = useState<Client[]>([]);
  const [products, setProducts] = useState<Product[]>([]);
  const [clientId, setClientId] = useState<number | null>(null);
  const [items, setItems] = useState<any[]>([]);

  useEffect(() => {
    getClients().then(setClients);
    getProducts().then(setProducts);
  }, []);

  const handleSubmit = async () => {
    if (!clientId || items.length === 0) return;

    await createInvoice({
      client_id: clientId,
      items,
    });

    alert("Factura creada");
  };

  return (
    <Paper sx={{ p: 3 }}>
      <h3>Nueva Factura</h3>

      <TextField
        select
        fullWidth
        label="Cliente"
        SelectProps={{ native: true }}
        onChange={(e) => setClientId(Number(e.target.value))}
      >
        <option />
        {clients.map((c) => (
          <option key={c.id} value={c.id}>
            {c.name}
          </option>
        ))}
      </TextField>

      <InvoiceItemsTable
        products={products}
        items={items}
        setItems={setItems}
      />

      <Button
        sx={{ mt: 2 }}
        variant="contained"
        onClick={handleSubmit}
      >
        Crear Factura
      </Button>
    </Paper>
  );
}
