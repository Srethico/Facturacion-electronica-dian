import { useEffect, useState } from "react";
import { Container } from "@mui/material";
import Navbar from "../components/Navbar";
import { getClients } from "../api/clients.api";
import type { Client } from "../types/client";
import ClientForm from "../components/ClientForm";
import ClientTable from "../components/ClientTable";


export default function Clients() {
  const [clients, setClients] = useState<Client[]>([]);

  const loadClients = async () => {
    const data = await getClients();
    setClients(data);
  };

  useEffect(() => {
    loadClients();
  }, []);

  return (
    <>
      <Navbar />
      <Container sx={{ mt: 4 }}>
        <ClientForm onCreated={loadClients} />
        <ClientTable clients={clients} />
      </Container>
    </>
  );
}
