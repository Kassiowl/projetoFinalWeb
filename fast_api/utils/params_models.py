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