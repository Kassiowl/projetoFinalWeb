
from core.domain.entities.pessoa import Pessoa
from core.domain.repositories.conta_interface import ContaInterface


class CadastrarContaPessoaUseCase():
    def __init__(self, conta_impl: ContaInterface):
        self.conta_impl = conta_impl
    
    def run(self, pessoa: Pessoa):
        return self.conta_impl.cadastrar_pessoa(pessoa)