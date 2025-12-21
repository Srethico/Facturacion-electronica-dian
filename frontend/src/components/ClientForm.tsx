import { useState } from "react";
import { Paper, TextField, Button, Box } from "@mui/material";
import { createClient } from "../api/clients.api";

export default function ClientForm({
  onCreated,
}: {
  onCreated: () => void;
}) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [identification, setIdentification] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    await createClient({
      name,
      email,
      identification,
    });

    setName("");
    setEmail("");
    setIdentification("");
    onCreated();
  };

  return (
    <Paper sx={{ p: 3, mb: 3 }}>
      <Box component="form" onSubmit={handleSubmit}>
        <TextField
          label="Nombre"
          fullWidth
          margin="normal"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <TextField
          label="Email"
          fullWidth
          margin="normal"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <TextField
          label="Identificación"
          fullWidth
          margin="normal"
          value={identification}
          onChange={(e) => setIdentification(e.target.value)}
        />

        <Button type="submit" variant="contained">
          Crear Cliente
        </Button>
      </Box>
    </Paper>
  );
}
