
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, FastAPI

from core.application.use_cases.conta_use_cases.cadastrar_conta_corrente import CadastrarContaCorrente
from core.application.use_cases.conta_use_cases.cadastrar_conta_pessoa_use_case import CadastrarContaPessoaUseCase
from core.application.use_cases.conta_use_cases.cadastrar_usuario_use_case import CadastrarUsuarioUseCase
from core.application.use_cases.conta_use_cases.logar_use_case import LogarUseCase
from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.entities.pessoa import Pessoa
from core.domain.entities.usuario import Usuario
from core.infraestructure.conta_impl import ContaImpl

from fast_api.utils.create_token import create_access_token
from fast_api.utils.params_models import ContaCadastroParams, PessoaCadastroParams, UsuarioCadastroParams, LoginParams

import random
from datetime import datetime, timedelta

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@app.get("/")
async def root():
    return {"Projeto Web": "Api"}

@app.post("/cadastrar_conta_corrente/", status_code=status.HTTP_201_CREATED)
async def cadastrar_conta_corrente(conta: ContaCadastroParams):
    conta_corrente_random_number = random.randint(1, 5000000000)
    conta_corrente = ContaCorrente(
                    conta_corrente_random_number, conta.nome, datetime.date.today(), 0, conta.senha)
    conta_impl = ContaImpl('contaDb.db',True)
    cadastrar_conta_corrente_use_case = CadastrarContaCorrente(conta_impl)
    conta_foi_cadastrada = cadastrar_conta_corrente_use_case.run(conta_corrente)
    if(conta_foi_cadastrada is False):
        raise HTTPException(status_code=500, detail="Falha ao cadastrar a conta corrente")
    return{"cadastro":conta_foi_cadastrada}


@app.post("/cadastrar_conta_pessoa", status_code=status.HTTP_201_CREATED)
async def cadastrar_conta_pessoa(conta_pessoa: PessoaCadastroParams):
    nome = conta_pessoa.nome
    cpf = conta_pessoa.cpf
    data_nascimento = conta_pessoa.data_nascimento
    telefone = conta_pessoa.telefone
    endereco = conta_pessoa.endereco
    cep = conta_pessoa.cep
    pessoa = Pessoa(nome, cpf, data_nascimento, telefone, endereco, cep)

    conta_impl = ContaImpl('contaDb.db',True)
    cadastrar_conta_pessoa_use_case = CadastrarContaPessoaUseCase(conta_impl)
    pessoa_foi_cadastrada = cadastrar_conta_pessoa_use_case.run(pessoa)
    if(pessoa_foi_cadastrada is False):
        raise HTTPException(status_code=500, detail="Falha ao cadastrar pessoa")
    return {"pessoa_cadastrada": pessoa_foi_cadastrada}


@app.post("/cadastrar_usuario", status_code=status.HTTP_201_CREATED)
async def cadastrar_usuario(usuario: UsuarioCadastroParams):

    nome = usuario.nome
    cpf = usuario.cpf
    data_nascimento = usuario.data_nascimento
    telefone = usuario.telefone
    endereco = usuario.endereco
    cep = usuario.cep
    senha = usuario.senha
    pessoa = Pessoa(nome, cpf, data_nascimento, telefone, endereco, cep)  

    email = usuario.email
    usuario = Usuario(email, pessoa)

    conta_impl = ContaImpl('contaDb.db',True)
    cadastrar_usuario_use_case = CadastrarUsuarioUseCase(conta_impl)
    usuario_foi_cadastrado = cadastrar_usuario_use_case.run(usuario, senha)
    if(usuario_foi_cadastrado is False):
        raise HTTPException(status_code=500, detail="Falha ao cadastrar usuario")
    return {"usuario_cadastrado", usuario_foi_cadastrado}


@app.post("/logar",status_code=status.HTTP_200_OK)
async def logar(login_data: LoginParams):
    conta_impl = ContaImpl("contaDb.db", True)

    
    usuario = login_data.email
    senha = login_data.senha

    logar_use_case = LogarUseCase(conta_impl)
    user_login = logar_use_case.run(usuario, senha)
    print("user login",user_login)
    if(user_login is False):
        raise HTTPException(status_code=401, detail="Nao autenticado")
    
    access_token_expires = timedelta(minutes=300)
    token = create_access_token(
        data={"sub": usuario}, expires_delta=access_token_expires
    )
    return{"token": token}



@app.get("/consultar_historico_movimento")
async def root():
    return {"Projeto Web": "Api"}


@app.get("/consultar_saldo_conta_corrente")
async def root():
    return {"Projeto Web": "Api"}

@app.get("/depositar")
async def root():
    return {"Projeto Web": "Api"}

@app.get("/realizar_transferencia")
async def root():
    return {"Projeto Web": "Api"}

@app.get("/selecionar_conta_corrente")
async def root():
    return {"Projeto Web": "Api"}






