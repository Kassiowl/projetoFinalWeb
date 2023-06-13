
from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.entities.movimento import Movimento
from core.domain.repositories.atividades_conta_interface import AtividadesContaInterface
import sqlite3

class AtividadeContaImpl(AtividadesContaInterface):
    def db_init(self):
        self.con = sqlite3.connect("banco.db")
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def consultar_saldo(self, conta_corrente: ContaCorrente):
        try:
            query = f'SELECT saldo from contaCorrente WHERE numero = {conta_corrente.numero}'
            self.cur.execute(query)
            saldo = self.cur.fetchone()

            if conta_corrente:
                return saldo
            return None
        except:
            return None
    def consultar_historico_movimento(conta_corrente: ContaCorrente) -> list[Movimento]:
        pass
    def realizar_transferencia(self,conta_corrente_origem: ContaCorrente,conta_corrente_destino: ContaCorrente, quantidade: float):
        try:
            self.con.execute("BEGIN TRANSACTION")
            query1 = f"UPDATE contaCorrente SET saldo = saldo - {quantidade} WHERE numero = {conta_corrente_origem.numero}"
            query2 = f"UPDATE contaCorrente SET saldo = saldo + {quantidade} WHERE numero = {conta_corrente_destino.numero}"
            self.cur.execute(query1)
            self.cur.execute(query2)
            self.con.commit()
            return True
        except:
            return False
    def depositar(self,conta_corrente: ContaCorrente, valor: float):
        try:
            query =  f"UPDATE contaCorrente SET saldo = saldo + {valor} WHERE numero = {conta_corrente.numero}"
            self.cur.execute(query)
            return True
        except:
            return False
    def selecionar_conta_corrente(self,nome_conta: str):
        try:
            query = f"SELECT * from contaCorrente WHERE nome = {nome_conta}"
            self.cur.execute(query)
            row = self.cur.fetchone()

            if row is not None:
                numero = row[0]
                nome = row[1]
                data_abertura = row[2]
                saldo = row[3]
                conta = ContaCorrente(numero, nome, data_abertura, saldo)
                return conta
            
            return None

        except:
            return None
    



    