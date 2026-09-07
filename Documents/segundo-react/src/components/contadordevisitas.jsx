import { useState } from "react"
function Contadordevisitas(){
const[conteo,setContador]=useState(0)
  const sumar = () => {
    setContador(conteo+1);
  };


return(
         <div>
        <h1>Contadordevisitas: {conteo}</h1>
        <button onClick={sumar}>Sumar café</button>
       
        
   </div>
 
);
}
export default Contadordevisitas;