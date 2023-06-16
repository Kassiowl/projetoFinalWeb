
from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.repositories.conta_interface import ContaInterface
from core.exception.conta_corrente.nova_conta_corrente import NovaContaCorrenteNaoPodeTerSaldoMaiorQueZero


class CadastrarContaCorrente():
    def __init__(self, conta_impl: ContaInterface):
        self.conta_impl = conta_impl
    
    def run(self, conta_corrente: ContaCorrente):
        if(conta_corrente.saldo > 0):
            raise NovaContaCorrenteNaoPodeTerSaldoMaiorQueZero(conta_corrente.saldo)
        return self.conta_impl.cadastrar_conta_corrente(conta_corrente)