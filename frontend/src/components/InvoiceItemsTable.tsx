import {
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  TextField,
  Typography,
} from "@mui/material";
import type { InvoiceItem } from "../types/invoice";

interface Props {
  items: InvoiceItem[];
  onChange: (items: InvoiceItem[]) => void;
}

export default function InvoiceItemsTable({
  items,
  onChange,
}: Props) {
  const handleQuantityChange = (
    index: number,
    quantity: number
  ) => {
    const updated = [...items];
    updated[index].quantity = quantity;
    onChange(updated);
  };

  return (
    <Table>
      <TableHead>
        <TableRow>
          <TableCell>Producto</TableCell>
          <TableCell>Precio base</TableCell>
          <TableCell>Cantidad</TableCell>
          <TableCell>IVA</TableCell>
          <TableCell>Total</TableCell>
        </TableRow>
      </TableHead>

      <TableBody>
        {items.map((item, index) => {
          const subtotal =
            item.base_price * item.quantity;

          const iva =
            subtotal * item.tax_rate / 100;

          const total = subtotal + iva;

          return (
            <TableRow key={item.product.id}>
              <TableCell>{item.product.name}</TableCell>

              <TableCell>
                ${item.base_price.toLocaleString("es-CO")}
              </TableCell>

              <TableCell>
                <TextField
                  type="number"
                  size="small"
                  value={item.quantity}
                  onChange={(e) =>
                    handleQuantityChange(
                      index,
                      Number(e.target.value)
                    )
                  }
                  inputProps={{ min: 1 }}
                />
              </TableCell>

              <TableCell>
                {item.tax_rate}% (
                ${iva.toLocaleString("es-CO")})
              </TableCell>

              <TableCell>
                <Typography fontWeight="bold">
                  ${total.toLocaleString("es-CO")}
                </Typography>
              </TableCell>
            </TableRow>
          );
        })}
      </TableBody>
    </Table>
  );
}
