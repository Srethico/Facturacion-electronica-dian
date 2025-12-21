import api from "./axios";
import type { Client } from "../types/client";

export const getClients = async (): Promise<Client[]> => {
  const { data } = await api.get("/clients");
  return data;
};

export const createClient = async (
  client: Omit<Client, "id">
): Promise<Client> => {
  const { data } = await api.post("/clients", client);
  return data;
};
