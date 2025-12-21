import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  IconButton,
  CircularProgress,
  Box,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import type { Product } from "../types/product";
import { useAuth } from "../auth/AuthContext";

interface Props {
  products: Product[];
  loading: boolean;
  onDelete: (product: Product) => void;
  onEdit: (product: Product) => void; // 👈 OBLIGATORIO
}

export default function ProductTable({
  products,
  loading,
  onDelete,
  onEdit,
}: Props) {
  const { user } = useAuth();

  if (loading) {
    return (
      <Box sx={{ textAlign: "center", mt: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Table>
      <TableHead>
        <TableRow>
            <TableCell>Nombre</TableCell>
            <TableCell>Precio base</TableCell>
            <TableCell>IVA</TableCell>
            <TableCell>Total</TableCell>
            <TableCell align="right">Acciones</TableCell>
        </TableRow>
        </TableHead>

      <TableBody>
        {products.map((product) => (
          <TableRow key={product.id}>
            <TableCell>{product.name}</TableCell>

            <TableCell>
              ${product.base_price.toLocaleString("es-CO")}
            </TableCell>

            <TableCell align="right">
              {user?.role === "admin" && (
                <>
                  <IconButton onClick={() => onEdit(product)}>
                    <EditIcon />
                  </IconButton>

                  <IconButton
                    color="error"
                    onClick={() => onDelete(product)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </>
              )}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
