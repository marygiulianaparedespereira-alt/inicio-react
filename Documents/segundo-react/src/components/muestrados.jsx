import { useState, useRef } from "react";

function ClicksRenders() {

  const [clicks, setClicks] = useState(0);

 
  const contadorRenders = useRef(0);

  contadorRenders.current = contadorRenders.current + 1;

  return (
    <div>
      <h2>Clicks vs Renders</h2>
      <p>Clicks en el boton: <strong>{clicks}</strong></p>
      <p>Cantidad de renders: <strong>{contadorRenders.current}</strong></p>

      <button onClick={() => setClicks(clicks + 1)}>
        Hacer Click
      </button>
    </div>
  );
}

export default ClicksRenders;