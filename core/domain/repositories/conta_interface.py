
from abc import ABC, abstractmethod

from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.entities.pessoa import Pessoa
from core.domain.entities.usuario import Usuario


class ContaInterface(ABC):
    @abstractmethod
    def cadastrar_conta_corrente(conta_corrente: ContaCorrente) -> bool:
        pass
    @abstractmethod
    def cadastrar_pessoa(pessoa: Pessoa) -> bool:
        pass
    @abstractmethod
    def cadastrar_usuario(usuario: Usuario) -> bool:
        pass
    @abstractmethod
    def logar(usuario: Usuario, senha) -> bool:
        pass

    