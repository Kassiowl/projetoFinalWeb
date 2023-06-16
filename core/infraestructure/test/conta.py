from core.application.use_cases.conta_use_cases.cadastrar_conta_pessoa_use_case import CadastrarContaPessoaUseCase
from core.application.use_cases.conta_use_cases.cadastrar_usuario_use_case import CadastrarUsuarioUseCase
from core.application.use_cases.conta_use_cases.logar_use_case import LogarUseCase
from core.domain.entities.pessoa import Pessoa
from core.domain.entities.usuario import Usuario
from core.infraestructure.conta_impl import ContaImpl



def test_conta():
    conta_impl = ContaImpl("test.db", False)
    pessoa = Pessoa("Nome", 1234542, "12/12/1995", 6193332, "Brasília-DF", "321312-344")
    usuario = Usuario('Email@emailteste.com', pessoa)

    cadastrar_conta_pessoa__use_case = CadastrarContaPessoaUseCase(conta_impl)
    assert(cadastrar_conta_pessoa__use_case.run(pessoa) == True)

    cadastrar_usuario_use_case = CadastrarUsuarioUseCase(conta_impl)

    assert(cadastrar_usuario_use_case.run(usuario, '123') == True) 

    logar_use_case = LogarUseCase(conta_impl)
    assert(logar_use_case.run(usuario, "123") == True)

    del conta_impl

