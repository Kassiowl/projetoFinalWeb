import React, { useState } from "react";

async function cadastrarContaPessoa(credentials) {
  return fetch('http://localhost:8000/cadastrar_conta_pessoa', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => data.json())
 }


function CadastrarContaPessoa() {

  const [cadastro, setCadastro] = useState();
  const [errorMessage, setErrorMessage] = useState()

  const [nome, setNome] = useState();
  const [cpf, setCPF] = useState();
  const [data_nascimento, setDataNascimento] = useState();
  const [telefone, setTelefone] = useState();
  const [endereco, setEndereco] = useState();
  const [cep, setCep] = useState();

  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const cadastro = await cadastrarContaPessoa({
        nome,
        cpf,
        data_nascimento,
        telefone,
        endereco,
        cep
      });
      if(cadastro){
        setCadastro("Cadastro realizado com sucesso")
      }
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
            <label for="Nome">Nome</label>
            <input type="text" class="form-control" id="Nome" aria-describedby="Nome" placeholder="Enter email" onChange={ e => setNome(e.target.value)}/>
          </div>
          <div class="form-group mt-4">
            <label for="CPF">CPF</label>
            <input type="number" class="form-control" id="CPF" placeholder="CPF" onChange={ e => setCPF(e.target.value)}/>
          </div>
          <div class="form-group mt-4">
            <label for="DataNascimento">Data de nascimento</label>
            <input type="date" class="form-control" id="DataNascimento" placeholder="Data de nascimento" onChange={ e => setDataNascimento(e.target.value)}/>
          </div>
          <div class="form-group mt-4">
            <label for="endereco">endereco</label>
            <input type="text" class="form-control" id="endereco" placeholder="endereço" onChange={ e => setEndereco(e.target.value)}/>
          </div>
          <div class="form-group mt-4">
            <label for="CEP">CEP</label>
            <input type="text" class="form-control" id="CEP" placeholder="CEP" onChange={ e => setCep(e.target.value)}/>
          </div>
          <div class="form-group mt-4">
            <label for="telefone">Telefone</label>
            <input type="number" class="form-control" id="telefone" placeholder="telefone" onChange={ e => setTelefone(e.target.value)}/>
          </div>
          <button type="submit" class="btn btn-primary">Cadastrar</button>
          </form>
          <p className="text-danger">{    errorMessage   }</p>
          <p className="text-success">{ cadastro  }</p>
        </div>
   
  );
}

export default CadastrarContaPessoa;