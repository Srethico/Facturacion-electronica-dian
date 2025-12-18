import { useEffect, useState } from "react";
import type { Product, ProductCreate } from "./product.types";
import {
  getProducts,
  createProduct as apiCreateProduct,
  deactivateProduct as apiDeactivateProduct,
} from "./products.api";

export function useProducts() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(false);

  const loadProducts = async () => {
    setLoading(true);
    try {
      const data = await getProducts();
      setProducts(data);
    } finally {
      setLoading(false);
    }
  };

  const createProduct = async (data: ProductCreate) => {
    const product = await apiCreateProduct(data);
    setProducts((prev) => [product, ...prev]);
  };

  const deactivateProduct = async (id: number) => {
    await apiDeactivateProduct(id);
    setProducts((prev) => prev.filter((p) => p.id !== id));
  };

  useEffect(() => {
    loadProducts();
  }, []);

  return {
    products,
    loading,
    createProduct,
    deactivateProduct,
  };
}
