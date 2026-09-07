
import { useState } from "react"
function Contadorcafe(){
const[conteo,setContador]=useState(0)
  const sumar = () => {
    setContador(conteo+1);
  };


return(
         <div>
        <h1>Contadorcafe: {conteo}</h1>
        <button onClick={sumar}>Sumar café</button>
       
        
   </div>
 
);
}
export default Contadorcafe;
 