import "./App.css";
import Persona1 from "./components/Persona1";
import TarjetaPelicula from "./components/TarjetaPelicula";
import Contador from "./components/Contador";
import { useState } from "react";
function App() {
  const peliculas = [
    { id: 1, titulo: "Interstellar", año: 2014, vista: false },
    { id: 2, titulo: "The Dark Knight", año: 2008, vista: true },
    { id: 3, titulo: "Inception", año: 2010, vista: false },
    { id: 4, titulo: "Oppenheimer", año: 2023, vista: true },
  ];
  return (
    <>
      <div>
        <Persona1
          nombre="Mary"
          rol="DESARROLLADORA"
          lenguajes={["Css", "Java"]}
        />
      </div>

      <div>
        {peliculas.map((item, index) => (
          <TarjetaPelicula
            key={item.id}
            titulo={item.titulo}
            año={item.año}
            vistas={item.vista}
          />
        ))}

      </div>
       
      


      <div>

        <Contador
       
         
         />
      </div>
    
        
    </>
  );
}

export default App;
