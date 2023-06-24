from abc import ABC, abstractmethod

from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.entities.movimento import Movimento

class AtividadesContaInterface(ABC):
    @abstractmethod
    def consultar_saldo(conta_corrente: ContaCorrente) -> float:
        pass
    @abstractmethod
    def consultar_historico_movimento(conta_corrente: ContaCorrente) -> list[Movimento]:
        pass
    @abstractmethod
    def realizar_transferencia(conta_corrente_origem: ContaCorrente,conta_corrente_destino: ContaCorrente, quantidade: float, observacao: str) -> bool:
        pass
    @abstractmethod
    def depositar(conta_corrente: ContaCorrente, valor: float) -> bool:
        pass
    @abstractmethod
    def selecionar_conta_corrente(numero_conta: int) -> ContaCorrente:
        pass