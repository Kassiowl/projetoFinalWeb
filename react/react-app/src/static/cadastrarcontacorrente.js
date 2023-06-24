import React, { useState } from "react";

async function cadastrarContaCorrente(credentials) {
  return fetch('http://localhost:8000/cadastrar_conta_corrente', {
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


function CadastrarContaCorrente() {

  const [cadastro, setCadastro] = useState();
  const [errorMessage, setErrorMessage] = useState()

  const [nome, setNome] = useState();
  const [senha, setSenha] = useState();
  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const cadastro_req = await cadastrarContaCorrente({
        nome,
        senha
      })

      setCadastro("Cadastro realizado com sucesso")
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
            <label for="nomedaconta">Nome da conta</label>
            <input type="text" class="form-control" id="nomedaconta" aria-describedby="emailHelp" placeholder="Nome da conta" onChange={ e => setNome(e.target.value)}/>
          </div>
          <div class="form-group mt-4">
            <label for="senha">Senha</label>
            <input type="password" class="form-control" id="senha" placeholder="Password" onChange={ e => setSenha(e.target.value)}/>
          </div>
          <button type="submit" class="btn btn-primary">Cadastrar</button>
          </form>
          <p className="text-danger">{    errorMessage   }</p>
          <p className="text-success">{ cadastro  }</p>
        </div>
   
  );
}

export default CadastrarContaCorrente;