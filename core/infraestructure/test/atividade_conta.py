from core.application.use_cases.atividade_conta_use_cases.consultar_saldo_conta_corrente_use_case import ConsultarSaldoContaCorrenteUseCase
from core.application.use_cases.conta_use_cases.cadastrar_conta_corrente import CadastrarContaCorrente
from core.application.use_cases.atividade_conta_use_cases.depositar_use_case_ import DepositarUseCase
from core.application.use_cases.atividade_conta_use_cases.realizar_transferencia_use_case import RealizarTransferenciaUseCase
from core.application.use_cases.atividade_conta_use_cases.selecionar_conta_corrente_use_case import SelecionarContaCorrenteUseCase
from core.domain.entities.conta_corrente import ContaCorrente
from core.infraestructure.atividade_conta_impl import AtividadeContaImpl
from core.infraestructure.conta_impl import ContaImpl




def test_atividade_conta():
    atividade_conta_impl = AtividadeContaImpl("test.db")
    conta_impl = ContaImpl("test.db", True)
    cadastrar_conta_corrente_use_case = CadastrarContaCorrente(conta_impl)

    conta_corrente_mock = ContaCorrente(33, "Conta corrente 33", "12/12/2015", 0.0, "3333")
    conta_destino_mock = ContaCorrente(34, "Conta corrente 34", "11/11/2014", 0.0, "3333")

    assert(cadastrar_conta_corrente_use_case.run(conta_corrente_mock) == True)
    
    depositar_use_case = DepositarUseCase(atividade_conta_impl)
    assert(depositar_use_case.run(conta_corrente_mock, 5005.3412) == True)

    # consultar_historico_movimento_use_case = ConsultarHistoricoMovimentoUseCase(atividade_conta_impl) Nao implementado ainda
    # consultar_historico_movimento_use_case.run(conta_corrente_mock)

    consultar_saldo_conta_corrente_use_case = ConsultarSaldoContaCorrenteUseCase(atividade_conta_impl)
    novo_saldo = consultar_saldo_conta_corrente_use_case.run(conta_corrente_mock)
    assert(novo_saldo == 5005.3412)
    conta_corrente_mock.saldo = novo_saldo


    realizar_transferencia_use_case = RealizarTransferenciaUseCase(atividade_conta_impl)
    assert(realizar_transferencia_use_case.run(conta_corrente_mock, conta_destino_mock, 4500) == True)
    
    conta_corrente_mock.saldo = conta_corrente_mock.saldo - 4500

    selecionar_conta_corrente_use_case = SelecionarContaCorrenteUseCase(atividade_conta_impl)
    assert(selecionar_conta_corrente_use_case.run(conta_corrente_mock.nome) == conta_corrente_mock)
    