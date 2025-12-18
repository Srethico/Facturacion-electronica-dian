import {
  Box,
  Card,
  CardContent,
  Typography,
  Button,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Stack,
} from "@mui/material";
import { useProducts } from "./useProducts";
import { ProductForm } from "./ProductForm";

export function ProductsPage() {
  const {
    products,
    createProduct,
    deactivateProduct,
  } = useProducts();

  return (
    <Box p={3}>
      <Typography variant="h4" mb={3}>
        Productos
      </Typography>

      {/* FORM */}
      <Card sx={{ mb: 4 }}>
        <CardContent>
          <ProductForm onSubmit={createProduct} />
        </CardContent>
      </Card>

      {/* TABLE */}
      <Card>
        <CardContent>
          <Typography variant="h6" mb={2}>
            Lista de Productos
          </Typography>

          <Table>
            <TableHead>
              <TableRow>
                <TableCell>SKU</TableCell>
                <TableCell>Nombre</TableCell>
                <TableCell>Precio</TableCell>
                <TableCell>IVA</TableCell>
                <TableCell align="right">Acciones</TableCell>
              </TableRow>
            </TableHead>

            <TableBody>
              {products.map((p) => (
                <TableRow key={p.id}>
                  <TableCell>{p.sku}</TableCell>
                  <TableCell>{p.name}</TableCell>
                  <TableCell>
                    ${Number(p.base_price).toFixed(2)}
                  </TableCell>
                  <TableCell>
                    {Number(p.tax_rate).toFixed(2)}%
                  </TableCell>
                  <TableCell align="right">
                    <Stack direction="row" spacing={1} justifyContent="flex-end">
                      <Button size="small" variant="outlined">
                        Editar
                      </Button>
                      <Button
                        size="small"
                        color="error"
                        variant="outlined"
                        onClick={() => deactivateProduct(p.id)}
                      >
                        Desactivar
                      </Button>
                    </Stack>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </Box>
  );
}
