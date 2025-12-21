import { useEffect, useState } from "react";
import {
  Container,
  Typography,
  Button,
  Stack,
} from "@mui/material";

import ProductTable from "../components/ProductTable";
import ProductForm from "../components/ProductForm";
import ConfirmDialog from "../components/ConfirmDialog";

import {
  getProducts,
  createProduct,
  updateProduct,
  deleteProduct,
} from "../api/products.api";

import type { Product } from "../types/product";
import { useAuth } from "../auth/AuthContext";

export default function Products() {
  const { user } = useAuth();

  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  const [selectedProduct, setSelectedProduct] =
    useState<Product | null>(null);

  const [formOpen, setFormOpen] = useState(false);
  const [editingProduct, setEditingProduct] =
    useState<Product | null>(null);

  const loadProducts = async () => {
    setLoading(true);
    const data = await getProducts();
    setProducts(data);
    setLoading(false);
  };

  useEffect(() => {
    loadProducts();
  }, []);

  const handleCreate = async (data: Omit<Product, "id">) => {
    await createProduct(data);
    loadProducts();
  };

  const handleEdit = async (data: Omit<Product, "id">) => {
    if (!editingProduct) return;
    await updateProduct(editingProduct.id, data);
    setEditingProduct(null);
    loadProducts();
  };

  const handleDelete = async () => {
    if (!selectedProduct) return;
    await deleteProduct(selectedProduct.id);
    setSelectedProduct(null);
    loadProducts();
  };

  return (
    <Container sx={{ mt: 4 }}>
      <Stack
        direction="row"
        justifyContent="space-between"
        alignItems="center"
        mb={2}
      >
        <Typography variant="h4">Productos</Typography>

        {user?.role === "admin" && (
          <Button
            variant="contained"
            onClick={() => setFormOpen(true)}
          >
            Nuevo producto
          </Button>
        )}
      </Stack>

      <ProductTable
        products={products}
        loading={loading}
        onDelete={setSelectedProduct}
        onEdit={(product) => {
          setEditingProduct(product);
          setFormOpen(true);
        }}
      />

      <ProductForm
        open={formOpen}
        initialData={editingProduct}
        onClose={() => {
          setFormOpen(false);
          setEditingProduct(null);
        }}
        onSubmit={editingProduct ? handleEdit : handleCreate}
      />

      <ConfirmDialog
        open={!!selectedProduct}
        title="Eliminar producto"
        description={`¿Eliminar "${selectedProduct?.name}"?`}
        onConfirm={handleDelete}
        onClose={() => setSelectedProduct(null)}
      />
    </Container>
  );
}
