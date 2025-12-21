import type { Product } from "./product";

export interface InvoiceItem {
  product: Product;
  quantity: number;
  base_price: number;
  tax_rate: number;
}

export interface InvoiceTotals {
  subtotal: number;
  iva: number;
  total: number;
}
