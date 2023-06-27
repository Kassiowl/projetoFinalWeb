import React, { useState } from "react";

async function consultarHistorico(numero_conta_corrente) {

   return fetch(`http://localhost:8000/consultar_historico_movimento/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(numero_conta_corrente)
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

  const [consulta, setConsulta] = useState();
  const [errorMessage, setErrorMessage] = useState()
  const [tipoHistorico, setTipoHistorico] = useState()
  const [contaCorrenteOrigem, setContaCorrenteOrigem] = useState()
  const [contaCorrenteDestino, setContaCorrenteDestino] = useState()
  const [observacao, setObservacao] = useState()
  const [dataMovimento, setDataMovimento] = useState()
  const [valor, setValor] = useState()

  const[numero_conta_corrente, setNumeroContaCorrente] = useState([])

  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const consultarhistorico = await consultarHistorico({
        numero_conta_corrente
      });
      setConsulta("Consulta realizada com sucesso")
      console.log(consultarhistorico.historico)
      setTipoHistorico(consultarhistorico.historico[0].tipo)
      setContaCorrenteOrigem(consultarhistorico.historico[0].conta_corrente_origem)
      setContaCorrenteDestino(consultarhistorico.historico[0].conta_corrente_destino)
      setObservacao(consultarhistorico.historico[0].observacao)
      setValor(consultarhistorico.historico[0].valor)
      setDataMovimento(consultarhistorico.historico[0].data_movimento)
      
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
          <button className="btn btn-primary" type="submit">Consultar Historico</button>
          </form>
          <p className="text-success">{consulta}</p>
          <h4>Historico:</h4>
          <p>data movimento:    {dataMovimento}</p>
          <p>tipo historico:    {tipoHistorico}</p>
          <p>conta corrente origem: {contaCorrenteOrigem}</p>
          <p>conta corrente destino:    {contaCorrenteDestino}</p>
          <p>Valor{valor}</p>
          <p>Observação{observacao}</p>
          <h2 className="text-danger">{errorMessage}</h2>
        </div>
   
  );
}

export default ConsultarHistorico;