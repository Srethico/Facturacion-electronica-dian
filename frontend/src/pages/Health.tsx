import { useEffect, useState } from "react"
import { http } from "../api/http"

function Health() {
  const [status, setStatus] = useState("cargando...")

  useEffect(() => {
    http.get("/health")
      .then(res => setStatus(res.data.status))
      .catch(() => setStatus("error"))
  }, [])

  return <h2>Backend status: {status}</h2>
}

export default Health
