import sqlite3
from core.domain.entities.conta_corrente import ContaCorrente
from core.domain.entities.pessoa import Pessoa
from core.domain.entities.usuario import Usuario
from core.domain.repositories.conta_interface import ContaInterface

class ContaImpl(ContaInterface):
    def __init__(self, db_name, already_created=False):
        self.db_name = db_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        if(not already_created):
            self.cur.execute("CREATE TABLE pessoa(cpf TEXT PRIMARY KEY, nome TEXT, data_nascimento DATE, telefone TEXT, endereco TEXT, cep TEXT)")

            self.cur.execute("CREATE TABLE movimento(tipo TEXT, data_movimento DATE, valor REAL, conta_corrente_origem INTEGER, \
                            conta_corrente_destino INTEGER, observacao TEXT, FOREIGN KEY(conta_corrente_origem) \
                            REFERENCES contaCorrente(numero), FOREIGN KEY(conta_corrente_destino) REFERENCES contaCorrente(numero))")
            
            self.cur.execute("CREATE TABLE contaCorrente(numero INTEGER PRIMARY KEY, nome TEXT, data_abertura DATE, saldo REAL, senha TEXT)")

            self.cur.execute("CREATE TABLE usuario(email TEXT, pessoa TEXT, senha TEXT, FOREIGN KEY(pessoa) REFERENCES pessoa(cpf))")

            self.con.commit()

    def __del__(self):
        if(self.db_name is None):
            return
        self.con.close()


    def cadastrar_conta_corrente(self, conta_corrente: ContaCorrente):
        conta_corrente_numero = conta_corrente.numero
        conta_corrente_nome = conta_corrente.nome
        conta_corrente_data_abertura = conta_corrente.data_abertura
        conta_corrente_saldo = conta_corrente.saldo
        try:
            self.cur.execute("""
                INSERT INTO contaCorrente VALUES
                ({}, '{}', '{}', {}, {})
            """.format(conta_corrente_numero, conta_corrente_nome, conta_corrente_data_abertura, conta_corrente_saldo, conta_corrente.senha))
            self.con.commit()
            return True
        except Exception as e:
            print("Exception___")
            print(e)
            return False

    def cadastrar_pessoa(self, pessoa: Pessoa):
        pessoa_cpf = pessoa.cpf
        pessoa_nome = pessoa.nome
        pessoa_data_nascimento = pessoa.data_nascimento
        pessoa_telefone = pessoa.telefone
        pessoa_endereco = pessoa.endereco
        pessoa_cep = pessoa.cep
        try:
            self.cur.execute("""
                INSERT INTO pessoa VALUES
                ('{}', '{}', '{}', '{}', '{}', '{}')
            """.format(pessoa_cpf, pessoa_nome, pessoa_data_nascimento, pessoa_telefone, pessoa_endereco, pessoa_cep))
            self.con.commit()
            return True
        except:
            return False

    def cadastrar_usuario(self, usuario: Usuario, senha):
        usuario_email = usuario.email
        usuario_pessoa_fk = usuario.pessoa.cpf
        try:
            self.cur.execute("""
                INSERT INTO usuario VALUES
                ('{}', '{}', '{}')
            """.format(usuario_email, usuario_pessoa_fk, senha))
            self.con.commit()
            return True
        except:
            return False
        
    def logar(self, email: str,senha: str):
        print("email:",email),
        print("senha:",senha)
        query = f"SELECT email, senha FROM usuario WHERE email = '{email}' AND senha = '{senha}'"
        self.cur.execute(query)
        user = self.cur.fetchone()
        if user:
            return True
        
        return False
