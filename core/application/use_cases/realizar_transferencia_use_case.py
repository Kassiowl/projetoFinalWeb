
from core.domain.repositories.atividades_conta_interface import AtividadesContaInterface
from core.domain.entities.conta_corrente import ContaCorrente

class RealizarTransferenciaUseCase():
    def __init__(self, atividade_conta_impl: AtividadesContaInterface):
        self.atividade_conta_impl = atividade_conta_impl
    
    def run(self, conta_corrente_origem: ContaCorrente, conta_corrente_destino: ContaCorrente, valor: float):
        return self.atividade_conta_impl.realizar_transferencia(conta_corrente_origem, conta_corrente_destino, valor)
    
