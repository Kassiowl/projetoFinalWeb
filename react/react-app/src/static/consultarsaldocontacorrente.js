import React, { useState } from "react";

async function consultarcontacorrente(numero_conta_corrente) {

   return fetch(`http://localhost:8000/consultar_saldo_conta_corrente/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(numero_conta_corrente)
  })
    .then(data => {
      if(data.ok){
        console.log("data")
        console.log(data)
        return data.json()
      }
      else{
        throw new Error(data.status)
      }
    })
 }


function ConsultarSaldoContaCorrente() {

  const [consulta, setConsulta] = useState();
  const [errorMessage, setErrorMessage] = useState()
 
  const[numero_conta_corrente, setNumeroContaCorrente] = useState([])

  const [saldo, setSaldoAtual] = useState()

  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const consultarsaldocontacorrente = await consultarcontacorrente({
        numero_conta_corrente
      });

      setSaldoAtual(consultarsaldocontacorrente.Saldo)
      setConsulta("Consulta realizada com sucesso")

    }
    catch(error)
    {
      setErrorMessage("Algo deu errado")
    }
  }

  return (
        <div className="container text-white">
            <h3>Consultar conta corrente</h3>
          <form onSubmit={handleSubmit}>
          <div class="form-group ">
            <label for="numeroconta">Numero da conta corrente</label>
            <input type="text" class="form-control" id="numeroconta" aria-describedby="Numero conta corrente"
             placeholder="Numero da conta corrente" onChange={ e => setNumeroContaCorrente(e.target.value)}/>
          </div>
          <button className="btn btn-primary" type="submit">Consultar saldo</button>
          </form>
          <h4 className="text-success">{consulta}</h4>
          <h2>Saldo atual: {saldo}</h2>
          <h2 className="text-danger">{errorMessage}</h2>
        </div>
   
  );
}

export default ConsultarSaldoContaCorrente;