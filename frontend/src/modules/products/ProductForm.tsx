import { useEffect, useState } from "react";
import {
  TextField,
  Button,
  Grid,
  Typography,
  Stack,
} from "@mui/material";
import type { Product, ProductCreate } from "./product.types";

interface Props {
  onSubmit: (data: ProductCreate) => void;
  onCancel?: () => void;
  initialData?: Product;
}

export function ProductForm({ onSubmit, onCancel, initialData }: Props) {
  const [form, setForm] = useState<ProductCreate>({
    sku: "",
    name: "",
    base_price: 0,
    tax_code: "01",
    tax_rate: 19,
  });

  useEffect(() => {
    if (initialData) {
      setForm({
        sku: initialData.sku,
        name: initialData.name,
        base_price: Number(initialData.base_price),
        tax_code: initialData.tax_code,
        tax_rate: Number(initialData.tax_rate),
      });
    }
  }, [initialData]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setForm({
      ...form,
      [name]:
        name === "base_price" || name === "tax_rate"
          ? Number(value)
          : value,
    });
  };

  return (
    <>
      <Typography variant="h6" mb={2}>
        {initialData ? "Editar Producto" : "Nuevo Producto"}
      </Typography>

      <form
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit(form);
        }}
      >
        <Grid container spacing={2}>
          <Grid item xs={12} md={3}>
            <TextField
              label="SKU"
              name="sku"
              fullWidth
              value={form.sku}
              onChange={handleChange}
              required
            />
          </Grid>

          <Grid item xs={12} md={3}>
            <TextField
              label="Nombre"
              name="name"
              fullWidth
              value={form.name}
              onChange={handleChange}
              required
            />
          </Grid>

          <Grid item xs={12} md={3}>
            <TextField
              label="Precio"
              name="base_price"
              type="number"
              fullWidth
              value={form.base_price}
              onChange={handleChange}
            />
          </Grid>

          <Grid item xs={12} md={3}>
            <TextField
              label="IVA %"
              name="tax_rate"
              type="number"
              fullWidth
              value={form.tax_rate}
              onChange={handleChange}
            />
          </Grid>
        </Grid>

        <Stack direction="row" spacing={2} mt={3}>
          <Button type="submit" variant="contained">
            {initialData ? "Actualizar" : "Guardar"}
          </Button>

          {onCancel && initialData && (
            <Button variant="outlined" onClick={onCancel}>
              Cancelar
            </Button>
          )}
        </Stack>
      </form>
    </>
  );
}
