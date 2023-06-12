
from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.repositories.atividades_conta_interface import AtividadesContaInterface
import sqlite3

class AtividadeContaImpl(AtividadesContaInterface):
    def db_init(self):
        self.con = sqlite3.connect("banco.db")
        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE pessoa(nome TEXT, cpf TEXT, data_nascimento DATE, telefone TEXT, endereco TEXT, cep TEXT)")

        self.cur.execute("CREATE TABLE movimento(tipo TEXT, data_movimento DATE, valor REAL, conta_corrente_origem INTEGER, \
                         conta_corrente_destino INTEGER, observacao TEXT, FOREIGN KEY(conta_corrente_origem) \
                         REFERENCES contaCorrente(numero), FOREIGN KEY(conta_corrente_destino) REFERENCES contaCorrente(numero))")
        
        self.cur.execute("CREATE TABLE contaCorrente(numero INTEGER PRIMARY KEY, nome TEXT, data_abertura DATE, saldo REAL)")

        self.cur.execute("CREATE TABLE usuario(email TEXT, pessoa INTEGER, FOREIGN KEY(pessoa) REFERENCES pessoa(rowid))")

    def cadastrar_conta_corrente(self, conta_corrente: ContaCorrente):

        conta_corrente_numero = conta_corrente.numero
        conta_corrente_nome = conta_corrente.nome
        conta_corrente_data_abertura = conta_corrente.data_abertura
        conta_corrente_saldo = conta_corrente.saldo

        try:
            self.cur.execute("""
                                    INSERT INTO contaCorrente VALUES
                                    ({conta_corrente_numero}, {conta_corrente_nome}, {conta_corrente_data_abertura}, {conta_corrente_saldo})
                            """.format(conta_corrente_numero=conta_corrente_numero, conta_corrente_nome=conta_corrente_nome, 
                                       conta_corrente_data_abertura=conta_corrente_data_abertura,
                                       conta_corrente_saldo = conta_corrente_saldo))
            return True
        except:
            return False



    