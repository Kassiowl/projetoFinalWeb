import React, { useState } from "react";

async function realizartransferencia(body) {

   return fetch(`http://localhost:8000/realizar_transferencia/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
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


function RealizarTransferencia() {

  const [transferencia, setTransferencia] = useState();
  const [errorMessage, setErrorMessage] = useState()
 
  const[conta_corrente_origem_num, setNumeroContaCorrenteOrigem] = useState()
  const[conta_corrente_destino_num, setNumeroContaCorrenteDestino] = useState()
  const [valor, setValor] = useState()
  const [observacao, setObservacao] = useState()

  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const consultarsaldocontacorrente = await realizartransferencia({
        conta_corrente_origem_num,
        conta_corrente_destino_num,
        valor,
        observacao
      });

      setTransferencia("Transferencia realizada com sucesso")

    }
    catch(error)
    {
      setErrorMessage("Algo deu errado")
    }
  }

  return (
        <div className="container text-white">
            <h3>Realizar transferencia</h3>
          <form onSubmit={handleSubmit}>
          <div class="form-group ">
            <label for="numerocontaorigem">Numero da sua conta corrente</label>
            <input type="text" class="form-control" id="numerocontaorigem" aria-describedby="Numero conta corrente"
             placeholder="Numero da conta corrente Origem" onChange={ e => setNumeroContaCorrenteOrigem(e.target.value)}/>
          </div>
          <div class="form-group ">
            <label for="numerocontacorrentedestino">Numero da conta corrente destino</label>
            <input type="text" class="form-control" id="numerocontacorrentedestino" aria-describedby="Numero conta corrente destino"
             placeholder="Numero da conta corrente Destino" onChange={ e => setNumeroContaCorrenteDestino(e.target.value)}/>
          </div>
          <div class="form-group ">
            <label for="numerocontacorrentedestino">Valor</label>
            <input type="valor" class="form-control" step="0.01" id="valor" aria-describedby="Numero conta corrente destino"
             placeholder="Valor" onChange={ e => setValor(e.target.value)}/>
          </div>
          <div class="form-group ">
            <label for="observação">Observação</label>
            <input type="text" class="form-control" id="observação" aria-describedby="Observação"
             placeholder="Observação" onChange={ e => setObservacao(e.target.value)}/>
          </div>
          <button className="btn btn-primary" type="submit">Realizar transferencia</button>
          </form>
          <h4 className="text-success">{transferencia}</h4>
          <h2 className="text-danger">{errorMessage}</h2>
        </div>
   
  );
}

export default RealizarTransferencia;