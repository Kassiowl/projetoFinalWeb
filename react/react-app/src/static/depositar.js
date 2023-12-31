import React, { useState } from "react";

async function depositar(credentials) {
  return fetch('http://localhost:8000/depositar', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => {
      if(!data.ok){
        throw new Error(data.status)
      }
      return data
    })
 }


function Depositar() {

  const [deposito, setDeposito] = useState();
  const [errorMessage, setErrorMessage] = useState()

  const [numero_conta_corrente, setNumero] = useState();
  const [valor, setValor] = useState();

  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const cadastro_req = await depositar({
        numero_conta_corrente,
        valor
      })

      setDeposito("Deposito realizado com sucesso")
    }
    catch(error)
    {
      setErrorMessage("Algo deu errado")
    }
  }
  return (
        <div className="container text-white">
          <form onSubmit={handleSubmit}>
          <div class="form-group ">
            <label for="numero">Numero da conta corrente</label>
            <input type="text" class="form-control" id="numero" placeholder="Numero" onChange={ e => setNumero(e.target.value)}/>
          </div>
          <div class="form-group mt-4">
            <label for="deposito">Valor</label>
            <input type="number" step="0.01" class="form-control" id="deposito" placeholder="Valor" onChange={ e => setValor(e.target.value)}/>
          </div>
          <button type="submit" class="btn btn-primary">Depositar</button>
          </form>
          <p className="text-danger">{    errorMessage   }</p>
          <p className="text-success">{ deposito  }</p>
        </div>
   
  );
}

export default Depositar;