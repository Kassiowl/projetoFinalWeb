
from core.domain.repositories.atividades_conta_interface import AtividadesContaInterface

class SelecionarContaCorrenteUseCase():
    def __init__(self, atividade_conta_impl: AtividadesContaInterface):
        self.atividade_conta_impl = atividade_conta_impl
    
    def run(self, nome_conta: str):
        return self.atividade_conta_impl.selecionar_conta_corrente(nome_conta)
    
    