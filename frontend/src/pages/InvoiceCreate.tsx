import { useEffect, useState } from "react";
import {
  Container,
  Typography,
  Box,
  Divider,
} from "@mui/material";

import InvoiceItemsTable from "../components/InvoiceItemsTable";
import type { Product } from "../types/product";
import type { InvoiceItem } from "../types/invoice";
import { getProducts } from "../api/products.api";

export default function InvoiceCreate() {
  const [products, setProducts] = useState<Product[]>([]);
  const [items, setItems] = useState<InvoiceItem[]>([]);

  useEffect(() => {
    getProducts().then((data) => {
      setProducts(data);

      // 👉 ejemplo: agregar primer producto
      if (data.length) {
        setItems([
          {
            product: data[0],
            quantity: 1,
            base_price: data[0].base_price,
            tax_rate: data[0].tax_rate,
          },
        ]);
      }
    });
  }, []);

  const subtotal = items.reduce(
    (acc, item) =>
      acc + item.base_price * item.quantity,
    0
  );

  const iva = items.reduce(
    (acc, item) =>
      acc +
      (item.base_price *
        item.quantity *
        item.tax_rate) /
        100,
    0
  );

  const total = subtotal + iva;

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Crear Factura
      </Typography>

      <InvoiceItemsTable
        items={items}
        onChange={setItems}
      />

      <Divider sx={{ my: 3 }} />

      <Box textAlign="right">
        <Typography>
          Subtotal: $
          {subtotal.toLocaleString("es-CO")}
        </Typography>

        <Typography>
          IVA: ${iva.toLocaleString("es-CO")}
        </Typography>

        <Typography variant="h6">
          Total: ${total.toLocaleString("es-CO")}
        </Typography>
      </Box>
    </Container>
  );
}
