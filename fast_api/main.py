
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi import Depends, FastAPI
from core.application.use_cases.atividade_conta_use_cases.consultar_historico_movimento_use_case import ConsultarHistoricoMovimentoUseCase
from core.application.use_cases.atividade_conta_use_cases.consultar_saldo_conta_corrente_use_case import ConsultarSaldoContaCorrenteUseCase
from core.application.use_cases.atividade_conta_use_cases.depositar_use_case_ import DepositarUseCase
from core.application.use_cases.atividade_conta_use_cases.realizar_transferencia_use_case import RealizarTransferenciaUseCase
from core.application.use_cases.atividade_conta_use_cases.selecionar_conta_corrente_use_case import SelecionarContaCorrenteUseCase

from core.application.use_cases.conta_use_cases.cadastrar_conta_corrente import CadastrarContaCorrente
from core.application.use_cases.conta_use_cases.cadastrar_conta_pessoa_use_case import CadastrarContaPessoaUseCase
from core.application.use_cases.conta_use_cases.cadastrar_usuario_use_case import CadastrarUsuarioUseCase
from core.application.use_cases.conta_use_cases.logar_use_case import LogarUseCase
from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.entities.pessoa import Pessoa
from core.domain.entities.usuario import Usuario
from core.infraestructure.atividade_conta_impl import AtividadeContaImpl
from core.infraestructure.conta_impl import ContaImpl

from fast_api.utils.create_token import create_access_token
from fast_api.utils.params_models import ConsultarHistoricoOrSaldoParams, ContaCadastroParams, DepositarParams, PessoaCadastroParams, SelecionarContaCorrenteParams, TransferenciaParams, UsuarioCadastroParams, LoginParams

import random
from datetime import datetime, timedelta
import datetime

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"Projeto Web": "Api"}

@app.post("/cadastrar_conta_corrente/", status_code=status.HTTP_201_CREATED)
async def cadastrar_conta_corrente(conta: ContaCadastroParams):
    try:
        conta_corrente_random_number = random.randint(1, 5000000000)
        conta_corrente = ContaCorrente(
                        conta_corrente_random_number, conta.nome, datetime.date.today(), 0, conta.senha)
        conta_impl = ContaImpl('contaDb.db',True)
        cadastrar_conta_corrente_use_case = CadastrarContaCorrente(conta_impl)
        conta_foi_cadastrada = cadastrar_conta_corrente_use_case.run(conta_corrente)
        if(conta_foi_cadastrada is False):
            raise HTTPException(status_code=500, detail="Falha ao cadastrar a conta corrente")
        return{"cadastro":conta_foi_cadastrada}
    except:
        raise HTTPException(status_code=500, detail="Falha ao cadastrar a conta corrente")


@app.post("/cadastrar_conta_pessoa", status_code=status.HTTP_201_CREATED)
async def cadastrar_conta_pessoa(conta_pessoa: PessoaCadastroParams):
    try:
        nome = conta_pessoa.nome
        cpf = int(conta_pessoa.cpf)
        data_nascimento = conta_pessoa.data_nascimento
        telefone = int(conta_pessoa.telefone)
        endereco = conta_pessoa.endereco
        cep = conta_pessoa.cep
        pessoa = Pessoa(nome, cpf, data_nascimento, telefone, endereco, cep)

        conta_impl = ContaImpl('contaDb.db',True)
        cadastrar_conta_pessoa_use_case = CadastrarContaPessoaUseCase(conta_impl)
        pessoa_foi_cadastrada = cadastrar_conta_pessoa_use_case.run(pessoa)
        if(pessoa_foi_cadastrada is False):
            raise HTTPException(status_code=500, detail="Falha ao cadastrar pessoa")
        return {"pessoa_cadastrada": pessoa_foi_cadastrada}
    except:
        raise HTTPException(status_code=500, detail="Falha ao cadastrar pessoa")


@app.post("/cadastrar_usuario", status_code=status.HTTP_201_CREATED)
async def cadastrar_usuario(usuario: UsuarioCadastroParams):
    try:
        nome = usuario.nome
        cpf = int(usuario.cpf)
        data_nascimento = usuario.data_nascimento
        telefone = int(usuario.telefone)
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
    except:
        raise HTTPException(status_code=500, detail="Falha ao cadastrar usuario")


@app.post("/logar",status_code=status.HTTP_200_OK)
async def logar(login_data: LoginParams):
    try:
        conta_impl = ContaImpl("contaDb.db", True)
        
        usuario = login_data.email
        senha = login_data.senha

        logar_use_case = LogarUseCase(conta_impl)
        user_login = logar_use_case.run(usuario, senha)
        if(user_login is False):
            raise HTTPException(status_code=401, detail="Nao autenticado")
        
        access_token_expires = timedelta(minutes=300)
        token = create_access_token(
            data={"sub": usuario}, expires_delta=access_token_expires
        )
        return{"token": token}
    except:
        raise HTTPException(status_code=500, detail="Erro interno ao logar")

@app.get("/consultar_historico_movimento")
async def consultar_historico_movimento(conta: ConsultarHistoricoOrSaldoParams):
    try:
        numero = conta.numero_conta_corrente
        conta_corrente = ContaCorrente(numero, None, None, None, None)
        atividade_conta_impl = AtividadeContaImpl('contaDb.db')
        consultar_historico_movimento_use_case = ConsultarHistoricoMovimentoUseCase(atividade_conta_impl)
        historico = consultar_historico_movimento_use_case.run(conta_corrente)
        if(historico == ["Algo deu errado na consulta de historico"]):
            raise HTTPException(status_code=500, detail="Algo deu errado na consulta de historico")
        return{"historico": historico}
    except:
        raise HTTPException(status_code=500, detail="Algo deu errado na consulta de historico")

@app.get("/consultar_saldo_conta_corrente")
async def consultar_saldo_conta_corrente(conta: ConsultarHistoricoOrSaldoParams):
    try:
        atividade_conta_impl = AtividadeContaImpl('contaDb.db')
        conta_corrente_numero = conta.numero_conta_corrente
        conta_corrente = ContaCorrente(conta_corrente_numero, None, None, None, None)
        consultar_saldo_use_case = ConsultarSaldoContaCorrenteUseCase(atividade_conta_impl)
        saldo = consultar_saldo_use_case.run(conta_corrente)
        if(saldo is None):
            raise HTTPException(status_code=500, detail="Algo deu errado na consulta de saldo")        
        return {"Saldo": saldo}
    except:
        raise HTTPException(status_code=500, detail="Algo deu errado na consulta de saldo")    

@app.post("/depositar")
async def depositar(deposito: DepositarParams):

    try:
        atividade_conta_impl = AtividadeContaImpl('contaDb.db')
        depositar_use_case = DepositarUseCase(atividade_conta_impl)
        conta_corrente = ContaCorrente(deposito.numero_conta_corrente, None, None, None, None)
        valor = deposito.valor
        depositar = depositar_use_case.run(conta_corrente,valor)
        if(depositar is None):
            raise HTTPException(status_code=500, detail="Algo deu errado no deposito")
        return {"Depositar": depositar}
    except:
        raise HTTPException(status_code=500, detail="Algo deu errado no deposito")


@app.post("/realizar_transferencia")
async def realizar_transferencia(transferencia: TransferenciaParams):

    try:
        atividade_conta_impl = AtividadeContaImpl('contaDb.db')
        realizar_transferencia_use_case = RealizarTransferenciaUseCase(atividade_conta_impl)

        selecionar_conta_corrente_use_case = SelecionarContaCorrenteUseCase(atividade_conta_impl)

        conta_corrente_origem = selecionar_conta_corrente_use_case.run(transferencia.conta_corrente_origem_num)
        conta_corrente_destino = selecionar_conta_corrente_use_case.run(transferencia.conta_corrente_destino_num)

        valor = float(transferencia.valor)

        observacao = transferencia.observacao
        transferencia = realizar_transferencia_use_case.run(conta_corrente_origem, conta_corrente_destino, valor, observacao)

        if(transferencia is False):
            raise HTTPException(status_code=500, detail="Algo deu errado na transferência")
        
        return {"Transferencia": transferencia}
    except:
        raise HTTPException(status_code=500, detail="Algo deu errado na transferência")

@app.get("/selecionar_conta_corrente")
async def selecionar_conta_corrente(selecionar: SelecionarContaCorrenteParams):
    try:
        atividade_conta_impl = AtividadeContaImpl('contaDb.db')
        selecionar_conta_corrente_use_case = SelecionarContaCorrenteUseCase(atividade_conta_impl)
        conta_corrente = selecionar_conta_corrente_use_case.run(selecionar.conta_num)

        if(conta_corrente is None):
            raise HTTPException(status_code=500, detail="Algo deu errado na seleção de conta")
        
        return {"conta_corrente": conta_corrente}
    except:
        raise HTTPException(status_code=500, detail="Algo deu errado na seleção de conta")






