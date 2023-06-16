class ContaNaoPossuiOValorNecessarioParaFazerATransferencia(Exception):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        self.message = f"A Conta atualmente não possui o valor necessário para fazer a transferencia de: {self.valor}, saldo\
        atual da conta e de:{self.saldo}"
        super().__init__(self.message)