from core.domain.entities.usuario import Usuario
from core.domain.repositories.conta_interface import ContaInterface


class LogarUseCase():
    def __init__(self, conta_impl: ContaInterface):
        self.conta_impl = conta_impl
    
    def run(self, usuario: Usuario, senha: str):
        return self.conta_impl.logar(usuario, senha)