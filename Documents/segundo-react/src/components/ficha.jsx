import { useState, useEffect } from "react";

function Fichas(props) {
  const { titulo, rol } = props;


  const [abierto, setAbierto] = useState(() => {
    const guardado = localStorage.getItem("estadoBoton");
    return guardado === "true";
  });

  useEffect(() => {
    localStorage.setItem("estadoBoton", abierto);
  }, [abierto]);

  return (
    <div>
      <p>{titulo} {rol}</p>
      <button onClick={() => setAbierto(!abierto)}>
        {abierto ? "apagado" : "encendido"}
      </button>
    </div>
  );
}

export default Fichas;