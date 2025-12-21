import { useEffect, useState } from "react";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Button,
  Stack,
} from "@mui/material";
import type { Product } from "../types/product";

type ProductPayload = Omit<Product, "id" | "is_active">;

interface Props {
  open: boolean;
  initialData?: Product | null;
  onClose: () => void;
  onSubmit: (data: ProductPayload) => Promise<void>;
}

export default function ProductForm({
  open,
  initialData,
  onClose,
  onSubmit,
}: Props) {
  const [form, setForm] = useState<ProductPayload>({
    sku: "",
    name: "",
    base_price: 0,
    tax_code: "",
    tax_rate: 0,
    dian_product_code: "",
  });

  useEffect(() => {
    if (initialData) {
      const { id, is_active, ...rest } = initialData;
      setForm(rest);
    }
  }, [initialData]);

  const handleChange = (
    field: keyof ProductPayload,
    value: string | number
  ) => {
    setForm({ ...form, [field]: value });
  };

  const handleSubmit = async () => {
    await onSubmit(form);
    onClose();
  };

  return (
    <Dialog open={open} onClose={onClose} fullWidth>
      <DialogTitle>
        {initialData ? "Editar producto" : "Crear producto"}
      </DialogTitle>

      <DialogContent>
        <Stack spacing={2} mt={1}>
          <TextField
            label="SKU"
            value={form.sku}
            onChange={(e) =>
              handleChange("sku", e.target.value)
            }
          />

          <TextField
            label="Nombre"
            value={form.name}
            onChange={(e) =>
              handleChange("name", e.target.value)
            }
          />

          <TextField
            label="Precio base"
            type="number"
            value={form.base_price}
            onChange={(e) =>
              handleChange("base_price", Number(e.target.value))
            }
          />

          <TextField
            label="Código IVA"
            value={form.tax_code}
            onChange={(e) =>
              handleChange("tax_code", e.target.value)
            }
          />

          <TextField
            label="IVA (%)"
            type="number"
            value={form.tax_rate}
            onChange={(e) =>
              handleChange("tax_rate", Number(e.target.value))
            }
          />

          <TextField
            label="Código DIAN"
            value={form.dian_product_code}
            onChange={(e) =>
              handleChange(
                "dian_product_code",
                e.target.value
              )
            }
          />
        </Stack>
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose}>Cancelar</Button>
        <Button variant="contained" onClick={handleSubmit}>
          Guardar
        </Button>
      </DialogActions>
    </Dialog>
  );
}
