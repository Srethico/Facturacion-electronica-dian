import api from "./axios";
import type { Product } from "../types/product";

type ProductPayload = Omit<Product, "id" | "is_active">;

export const getProducts = async (): Promise<Product[]> => {
  const { data } = await api.get("/products/");
  return data;
};

export const createProduct = async (
  product: ProductPayload
): Promise<Product> => {
  const { data } = await api.post("/products/", product);
  return data;
};

export const updateProduct = async (
  id: number,
  product: ProductPayload
): Promise<Product> => {
  const { data } = await api.put(`/products/${id}`, product);
  return data;
};

// ✅ ESTA FUNCIÓN FALTABA
export const deleteProduct = async (id: number): Promise<void> => {
  await api.delete(`/products/${id}`);
};
