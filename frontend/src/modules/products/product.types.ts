export interface Product {
  id: number;
  sku: string;
  name: string;
  base_price: number;
  tax_code: string;
  tax_rate: number;
  is_active: boolean;
}

export interface ProductCreate {
  sku: string;
  name: string;
  base_price: number;
  tax_code: string;
  tax_rate: number;
}
