import React, { useState } from "react";

async function selecionartodascontascorrentes() {

   return fetch(`http://localhost:8000/selecionar_todas_contas_correntes/`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
    .then(data => {
      if(data.ok){
        return data.json()
      }
      else{
        throw new Error(data.status)
      }
    })
 }


function ConsultarHistorico() {


  const[numero_conta_corrente, setNumeroContaCorrente] = useState([])

  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const selecionarcontascorrente = await selecionartodascontascorrentes({});
      
    }
    catch(error)
    {
      setErrorMessage("Algo deu errado")
    }
  }

  return (
        <div className="container text-white">
            <h3>Todas as contas correntes</h3>
          
        </div>
   
  );
}

export default ConsultarHistorico;