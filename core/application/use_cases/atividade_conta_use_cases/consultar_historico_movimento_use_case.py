
from core.domain.repositories.atividades_conta_interface import AtividadesContaInterface
from core.domain.entities.conta_corrente import ContaCorrente

class ConsultarHistoricoMovimentoUseCase():
    def __init__(self, atividade_conta_impl: AtividadesContaInterface):
        self.atividade_conta_impl = atividade_conta_impl
    
    def run(self, conta_corrente: ContaCorrente):
        return self.atividade_conta_impl.consultar_historico_movimento(conta_corrente)