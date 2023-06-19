
from core.domain.repositories.atividades_conta_interface import AtividadesContaInterface
from core.domain.entities.conta_corrente import ContaCorrente
from core.exception.conta_corrente.transferencia import ContaNaoPossuiOValorNecessarioParaFazerATransferencia

class RealizarTransferenciaUseCase():
    def __init__(self, atividade_conta_impl: AtividadesContaInterface):
        self.atividade_conta_impl = atividade_conta_impl
    
    def run(self, conta_corrente_origem: ContaCorrente, conta_corrente_destino: ContaCorrente, valor: float, observacao: str = "Nenhuma"):
        if(valor > conta_corrente_origem.saldo):
            raise ContaNaoPossuiOValorNecessarioParaFazerATransferencia(conta_corrente_origem.saldo, valor)
        return self.atividade_conta_impl.realizar_transferencia(conta_corrente_origem, conta_corrente_destino, valor, observacao)
    
