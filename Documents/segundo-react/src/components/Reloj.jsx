import { useState, useEffect } from "react";

function Contador() {
  const [contador, setContador] = useState(0);
  const [abierto, setAbierto] = useState(false);

  useEffect(() => {

    if (!abierto) return;

   
    const intervalo = setInterval(() => {
      console.log("tic");
      setContador((antes) => antes+ 1); 
    }, 1000);

    return () => {
      clearInterval(intervalo);
    };
  }, [abierto]);

  return (
    <div>
      <button onClick={() => setAbierto(!abierto)}>
        {abierto ? '▲' : '▼'}
      </button>

      {abierto && (
        <div className="contador">
          <p>{contador}</p>
        </div>
      )}
    </div>
  );
}

export default Contador;