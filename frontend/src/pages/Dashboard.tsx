import Navbar from "../components/Navbar";
import { Container, Typography } from "@mui/material";

export default function Dashboard() {
  return (
    <>
      <Navbar />
      <Container sx={{ mt: 4 }}>
        <Typography variant="h4">
          Dashboard Administrativo
        </Typography>
      </Container>
    </>
  );
}
