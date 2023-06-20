from pydantic import BaseModel


class ContaCadastroParams(BaseModel):
    nome: str
    senha: str

class PessoaCadastroParams(BaseModel):
    nome : str
    cpf : int
    data_nascimento: str
    telefone : int
    endereco : str
    cep : str
    

class UsuarioCadastroParams(BaseModel):
    email: str
    senha: str
    nome : str
    cpf : int
    data_nascimento: str
    telefone : int
    endereco : str
    cep : str


class LoginParams(BaseModel):
    email: str
    senha: str

class ConsultarHistoricoOrSaldoParams(BaseModel):
    numero_conta_corrente: int

class DepositarParams(BaseModel):
    numero_conta_corrente: int
    valor: float

class TransferenciaParams(BaseModel):
    valor: float
    observacao: str
    conta_corrente_origem_num: int
    conta_corrente_destino_num: int


class SelecionarContaCorrenteParams(BaseModel):
    conta_num: int