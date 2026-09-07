import { useState } from 'react'
import './App.css'
import Contador from "./components/Reloj" // Ruta corregida
import Contadora  from "./components/muestrados"
import Fichas from "./components/ficha"
import Contadorcafe from './components/contadorcafe'
import Contadordevisitas from './components/contadordevisitas'

function App() {
  return (

    <> 
      <div>
        <Contador />
      </div>

       <div>
        <Contadora />
      </div>

      <div>
        <Fichas
        titulo ="Spiderman"
        rol ="Superheroe"
        
        />
      </div>
      <div>
        <Contadorcafe/>
      </div>

        <div>
        <Contadordevisitas/>
      </div>
    </>

  )
}

export default App