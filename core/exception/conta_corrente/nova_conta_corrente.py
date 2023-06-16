class NovaContaCorrenteNaoPodeTerSaldoMaiorQueZero(Exception):
    def __init__(self, saldo):
        self.saldo = saldo
        self.message = f"O saldo de uma nova conta nao pode ser maior que 0, atualmente:{self.saldo}"
        super().__init__(self.message)