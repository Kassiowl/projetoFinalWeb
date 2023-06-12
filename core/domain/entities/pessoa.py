from dataclasses import dataclass


@dataclass
class Pessoa:
    nome : str
    cpf: int
    data_nascimento: str
    telefone : int
    endereco: str
    cep: str
    
    