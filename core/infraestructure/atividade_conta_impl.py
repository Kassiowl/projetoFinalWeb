
from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.entities.movimento import Movimento
from core.domain.repositories.atividades_conta_interface import AtividadesContaInterface
import sqlite3
from datetime import date

class AtividadeContaImpl(AtividadesContaInterface):
    def __init__(self, nome_banco):
        self.con = sqlite3.connect(nome_banco)
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()

    def consultar_saldo(self, conta_corrente: ContaCorrente):
        try:
            query = f'SELECT saldo from contaCorrente WHERE numero = {conta_corrente.numero}'
            self.cur.execute(query)
            saldo = self.cur.fetchone()
            saldo = saldo[0]
            if conta_corrente:
                return float(saldo)
            return None
        except:
            return None
    def consultar_historico_movimento(self,conta_corrente: ContaCorrente) -> list[Movimento]:
        try:
            query = f"SELECT * FROM movimento WHERE conta_corrente_origem = '{conta_corrente.numero}'"
            self.cur.execute(query)
            rows = self.cur.fetchall()
            if rows is not None:
                list_of_rows = []
                for row in rows:
                    movimento = Movimento(row[0], row[1], row[2], row[3], row[4], row[5])
                    list_of_rows.append(movimento)
                return list_of_rows
            
            return ["Nao foi encontrado nenhum historico"]
        except Exception as e:
            print(e)
            return ["Algo deu errado na consulta de historico"]


    def realizar_transferencia(self,conta_corrente_origem: ContaCorrente,conta_corrente_destino: ContaCorrente, 
                               quantidade: float, observacao="Nenhuma"):
        try:
            self.con.execute("BEGIN TRANSACTION")
            query1 = f"UPDATE contaCorrente SET saldo = saldo - {quantidade} WHERE numero = {conta_corrente_origem.numero}"
            query2 = f"UPDATE contaCorrente SET saldo = saldo + {quantidade} WHERE numero = {conta_corrente_destino.numero}"
            hoje = date.today()
            query3 = f"INSERT INTO movimento VALUES('transferencia', '{hoje}', '{quantidade}', \
                    '{conta_corrente_origem.numero}', '{conta_corrente_destino.numero}', '{observacao}')"
            self.cur.execute(query1)
            self.cur.execute(query2)
            self.cur.execute(query3)
            self.con.commit()
            return True
        except:
            return False
    def depositar(self,conta_corrente: ContaCorrente, valor: float):
        try:
            query =  f"UPDATE contaCorrente SET saldo = saldo + {valor} WHERE numero = {conta_corrente.numero}"
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False
    def selecionar_conta_corrente(self,nome_conta: str):
        try:
            query = f"SELECT * FROM contaCorrente WHERE nome = '{nome_conta}'"
            self.cur.execute(query)
            row = self.cur.fetchone()
            if row is not None:
                numero = row[0]
                nome = row[1]
                data_abertura = row[2]
                saldo = row[3]
                senha = row[4]
                conta = ContaCorrente(numero, nome, data_abertura, saldo,senha)
                return conta
            return None
        except:
            return None
    



    