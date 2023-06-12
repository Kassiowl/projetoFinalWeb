from abc import ABC, abstractmethod

from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.entities.movimento import Movimento

class AtividadesContaInterface(ABC):
    @abstractmethod
    def consultar_saldo(conta_corrente: ContaCorrente) -> float:
        pass
    @abstractmethod
    def consultar_historico_movimento(conta_corrente: ContaCorrente) -> list:
        pass
    @abstractmethod
    def realizar_transferencia(conta_corrente_origem: ContaCorrente,conta_corrente_destino: ContaCorrente) -> bool:
        pass
    @abstractmethod
    def depositar(conta_corrente: ContaCorrente, valor: float) -> Movimento:
        pass
    def selecionar_conta_corrente(nome_conta: str) -> ContaCorrente:
        pass