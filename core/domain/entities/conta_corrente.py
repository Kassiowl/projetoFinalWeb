from dataclasses import dataclass


@dataclass
class ContaCorrente:
    numero : int
    nome: str
    data_abertura: str
    saldo: float