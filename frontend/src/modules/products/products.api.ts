import api from "../../api/api";
import type { Product, ProductCreate } from "./product.types";

/**
 * Obtener lista de productos activos
 */
export const getProducts = async (): Promise<Product[]> => {
  const res = await api.get("/products/");
  return res.data;
};

/**
 * Crear producto
 */
export const createProduct = async (
  data: ProductCreate
): Promise<Product> => {
  const res = await api.post("/products/", data);
  return res.data;
};

/**
 * Actualizar producto
 * (usamos PATCH porque normalmente es actualización parcial)
 */
export const updateProduct = async (
  id: number,
  data: Partial<ProductCreate>
): Promise<Product> => {
  const res = await api.patch(`/products/${id}`, data);
  return res.data;
};

/**
 * Desactivar producto (soft delete)
 */
export const deactivateProduct = async (id: number): Promise<void> => {
  await api.delete(`/products/${id}`);
};
