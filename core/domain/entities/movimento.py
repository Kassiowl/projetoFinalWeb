from dataclasses import dataclass
from .conta_corrente import ContaCorrente

@dataclass
class Movimento:
    tipo : str
    data_movimento: str
    valor: float
    conta_corrente_origem: ContaCorrente
    conta_corrente_destino: ContaCorrente
    observacao: str
    