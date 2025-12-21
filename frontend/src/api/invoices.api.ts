import api from "./axios";
import type { Invoice } from "../types/invoice";

export const getInvoices = async (): Promise<Invoice[]> => {
  const { data } = await api.get("/invoices");
  return data;
};

export const createInvoice = async (
  invoice: Omit<Invoice, "id" | "status" | "total">
): Promise<Invoice> => {
  const { data } = await api.post("/invoices", invoice);
  return data;
};
