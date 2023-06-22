import React, { useState } from "react";

async function cadastrarContaUsuario(credentials) {
  return fetch('http://localhost:8000/cadastrar_usuario', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(credentials)
  })
    .then(data => data.json())
 }


function CadastrarContaUsuario() {

  const [cadastro, setCadastro] = useState();
  const [errorMessage, setErrorMessage] = useState()

  
 
  const [email, setEmail] = useState();
  const [senha, setSenha] = useState();
  const [data_nascimento, setDataNascimento] = useState();
  const [telefone, setTelefone] = useState();
  const [endereco, setEndereco] = useState();
  const [cep, setCep] = useState();
  const [nome, setNome] = useState();
  const[cpf, setCPF] = useState()

  const handleSubmit = async e => {
    e.preventDefault();
    try
    {
      const cadastro = await cadastrarContaUsuario({
        email,
        senha,
        data_nascimento,
        telefone,
        endereco,
        cep,
        cpf,
        nome
      });
      if(cadastro.stauts == 200){
        setCadastro("Cadastro realizado com sucesso")
      }
      else{
        setErrorMessage("Algo deu errado no servidor, tente novamente mais tarde")
      }
    }
    catch(error)
    {
      setErrorMessage("Algo deu errado")
    }
  }

  return (
        <div className="container">
            <h3>Cadastre-se</h3>
          <form onSubmit={handleSubmit}>
          <div class="form-group ">
            <label for="email">Email</label>
            <input type="text" class="form-control" id="email" aria-describedby="Nome" placeholder="Email" onChange={ e => setEmail(e.target.value)}/>
          </div>
          <div class="form-group ">
            <label for="nome">Nome</label>
            <input type="text" class="form-control" id="nome" aria-describedby="Nome" placeholder="Nome" onChange={ e => setNome(e.target.value)}/>
          </div>
          <div class="form-group ">
            <label for="CPF">CPF</label>
            <input type="number" class="form-control" id="CPF" aria-describedby="Nome" placeholder="CPF" onChange={ e => setCPF(e.target.value)}/>
          </div>
          <div class="form-group mt-4">
            <label for="senha">senha</label>
            <input type="password" class="form-control" id="senha" placeholder="senha" onChange={ e => setSenha(e.target.value)}/>
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

export default CadastrarContaUsuario;