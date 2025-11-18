from datetime import date

from models.Cliente import Cliente
from models.Veiculo import Veiculo
from models.OrdemServico import OrdemServico
from models.Funcionario import Atendente, Mecanico
from models.Peca import Peca

def fluxo_cliente():
    titulo(" FLUXO DO CLIENTE - SOLICITAÇÃO E ACOMPANHAMENTO ")

    # ETAPA 1: Cadastro do cliente e associação do veículo
    print("\n ETAPA 1: Cadastro do Cliente e Veículo")
    linha("-")
    veiculo = Veiculo("ABC1234", "Fusca", "VW", 1980)
    cliente = Cliente(nome="João Silva", veiculos=[veiculo])
    print(f" Cliente cadastrado: {cliente.nome} (ID: {cliente.id_cliente})")
    print(f" Veículo associado: {veiculo.exibir_info()}")

    # ETAPA 2: Cliente abre chamado
    print("\n ETAPA 2: Abertura do Chamado")
    linha("-")
    ordem = cliente.abrir_chamado(veiculo, "Troca de óleo e revisão completa")
    # registra a ordem na lista mantida pelo main
    orders_list.append(ordem)
    print(f" Chamado aberto: OS #{ordem.id_os} - Status: {ordem.status}")

    # ETAPA 3: Geração de orçamento (método da OS)
    print("\n ETAPA 3: Geração de Orçamento")
    linha("-")
    # Criar peça: óleo de motor com 50 unidades no estoque
    oleo_motor = Peca(
        id_peca=1,
        nome="Óleo Motor Sintético 5W30",
        descricao="Óleo sintético premium para motores",
        qtd_estoque=50,
        valor_unit=89.90
    )
    print(f" Peça criada: {oleo_motor.nome} - Estoque: {oleo_motor.qtd_estoque}")

    # Retirar 5 unidades para esta OS
    qtd_retirada = 5
    if oleo_motor.retirar_peca(qtd_retirada):
        ordem.adicionar_peca(oleo_motor, qtd_retirada)
        print(f" {qtd_retirada} unidades de {oleo_motor.nome} retiradas do estoque. Estoque restante: {oleo_motor.qtd_estoque}")
    else:
        print(f" Estoque insuficiente para retirar {qtd_retirada} unidades de {oleo_motor.nome}")

    orcamento = ordem.gerar_orcamento()
    print(f" Orçamento calculado: R$ {orcamento:,.2f}")
    print(f" Status atual da OS: {ordem.status}")

    # ETAPA 4: Cliente aprova o orçamento
    print("\n ETAPA 4: Aprovação do Orçamento pelo Cliente")
    linha("-")
    aprovado = cliente.aprovar_orcamento(ordem)
    print(f" Cliente aprovou o orçamento? {'Sim' if aprovado else 'Não'}")
    print(f" Status após ação: {ordem.status}")

    # ETAPA 5: Consulta e exibição detalhada das ordens do cliente
    print("\n ETAPA 5: Consulta das Ordens do Cliente")
    linha("-")
    ordens = cliente.consultar_os(orders_list)
    print(f" Foram encontradas {len(ordens)} ordem(s) para o cliente {cliente.nome}")
    for o in ordens:
        print("--------------------")
        o.exibir_resumo()
    if ordens:
        print("--------------------")

    # ETAPA 6: Incrementa contador de serviços do cliente (exemplo de uso do método)
    print("\n ETAPA 6: Atualização do histórico do cliente")
    linha("-")
    antes = cliente.qtd_servicos
    cliente.incrementar_servicos()
    depois = cliente.qtd_servicos
    print(f" Serviços realizados (antes/depois): {antes} -> {depois}")


"""
Demonstração Completa do Fluxo de um Mecânico
Sistema de Mecânica - POO em Python

Mecânico: José Vilas Boas
Salário Base: R$ 5.000,00
"""

def linha(caractere="=", tamanho=80):
    """Imprime uma linha separadora"""
    print(caractere * tamanho)

def titulo(texto):
    """Imprime um título formatado"""
    linha()
    print(f"  {texto}")
    linha()

def fluxo_mecanico():
    titulo(" FLUXO COMPLETO DO MECÂNICO - JOSÉ VILAS BOAS")
    
    # =====================================================
    # 1. CRIAÇÃO DO MECÂNICO
    # =====================================================
    print("\n ETAPA 1: Cadastro do Mecânico")
    linha("-")
    
    mecanico = Mecanico(
        nome="José Vilas Boas",
        id_funcionario=100,
        salario_base=5000.00,
        qtd_veiculos_atendidos=0,
        bonus_por_veiculo=150.00
    )
    
    print(f" Mecânico cadastrado:")
    print(f"   Nome: {mecanico.nome}")
    print(f"   ID: {mecanico.id}")
    print(f"   Salário Base: R$ {mecanico.salario_base:,.2f}")
    print(f"   Bônus por Veículo: R$ {mecanico.bonus_por_veiculo:,.2f}")
    print(f"   Veículos Atendidos: {mecanico.qtd_veiculos_atendidos}")
    
    # =====================================================
    # 2. CÁLCULO INICIAL DO SALÁRIO (Polimorfismo)
    # =====================================================
    print("\n ETAPA 2: Cálculo do Salário Inicial (Polimorfismo)")
    linha("-")
    
    salario_inicial = mecanico.calcular_salario()
    print(f" Salário Calculado (sem bônus): R$ {salario_inicial:,.2f}")
    print(f"   Fórmula: {mecanico.salario_base:,.2f} + ({mecanico.qtd_veiculos_atendidos} × {mecanico.bonus_por_veiculo:,.2f})")
    
    # =====================================================
    # 3. CRIAÇÃO DO CLIENTE E VEÍCULO
    # =====================================================
    print("\n ETAPA 3: Cliente solicita serviço")
    linha("-")
    
    veiculo = Veiculo(
        placa="XYZ9876",
        nome_veiculo="Honda Civic",
        modelo="EXL 2.0",
        ano_fabricacao=2022
    )

    cliente = Cliente(
        nome="Maria Silva Santos",
        qtd_servicos=3,
        satisfacao="Satisfeito",
        veiculos=[veiculo]
    )
    
    print(f" Cliente: {cliente.nome} (ID: {cliente.id_cliente})")
    print(f" Veículo: {veiculo.exibir_info()}")
    print(f" Idade do veículo: {veiculo.calcular_idade()} anos")
    
    # =====================================================
    # 4. CRIAÇÃO DA ORDEM DE SERVIÇO
    # =====================================================
    print("\n ETAPA 4: Criação da Ordem de Serviço")
    linha("-")
    
    ordem_servico = OrdemServico(
        data_abertura=date.today(),
        status="Aberto",
        descricao="Revisão completa dos 30.000 km + Troca de óleo e filtros",
        valor_total=0.0,
        cliente=cliente,
        mecanico=None,
        veiculo=veiculo
    )
    
    print(f"   OS #{ordem_servico.id_os} criada")
    print(f"   Data: {ordem_servico.data_abertura}")
    print(f"   Status: {ordem_servico.status}")
    print(f"   Descrição: {ordem_servico.descricao}")
    
    # =====================================================
    # 5. MECÂNICO É ATRIBUÍDO À OS
    # =====================================================
    print("\n ETAPA 5: Atribuição do Mecânico à OS")
    linha("-")
    
    ordem_servico.atribuir_mecanico(mecanico)
    ordem_servico.atribuir_veiculo(veiculo)
    
    print(f" Mecânico {mecanico.nome} atribuído à OS #{ordem_servico.id_os}")
    print(f"   Mecânico atual da OS: {ordem_servico.mecanico.nome}")
    
    # =====================================================
    # 6. CRIAÇÃO DO ESTOQUE DE PEÇAS
    # =====================================================
    print("\n ETAPA 6: Verificação do Estoque de Peças")
    linha("-")
    
    # Criando peças no estoque
    oleo_motor = Peca(
        id_peca=1,
        nome="Óleo Motor Sintético 5W30",
        descricao="Óleo sintético premium para motores",
        qtd_estoque=50,
        valor_unit=89.90
    )
    
    filtro_oleo = Peca(
        id_peca=2,
        nome="Filtro de Óleo",
        descricao="Filtro de óleo original Honda",
        qtd_estoque=30,
        valor_unit=45.50
    )
    
    filtro_ar = Peca(
        id_peca=3,
        nome="Filtro de Ar",
        descricao="Filtro de ar esportivo",
        qtd_estoque=20,
        valor_unit=78.00
    )
    
    filtro_combustivel = Peca(
        id_peca=4,
        nome="Filtro de Combustível",
        descricao="Filtro de combustível original",
        qtd_estoque=15,
        valor_unit=62.00
    )
    
    print(" Peças disponíveis no estoque:")
    print(f"   1. {oleo_motor.nome} - Estoque: {oleo_motor.qtd_estoque} - R$ {oleo_motor.valor_unit:.2f}")
    print(f"   2. {filtro_oleo.nome} - Estoque: {filtro_oleo.qtd_estoque} - R$ {filtro_oleo.valor_unit:.2f}")
    print(f"   3. {filtro_ar.nome} - Estoque: {filtro_ar.qtd_estoque} - R$ {filtro_ar.valor_unit:.2f}")
    print(f"   4. {filtro_combustivel.nome} - Estoque: {filtro_combustivel.qtd_estoque} - R$ {filtro_combustivel.valor_unit:.2f}")
    
    # =====================================================
    # 7. MECÂNICO REQUISITA PEÇAS DO ESTOQUE
    # =====================================================
    print("\n  ETAPA 7: Mecânico Requisita Peças do Estoque")
    linha("-")
    
    print(f"\n Requisitando 4 litros de óleo motor...")
    if mecanico.requisitar_estoque(oleo_motor, 4):
        print(f"   Requisição aprovada! Estoque atualizado: {oleo_motor.qtd_estoque} unidades")
        ordem_servico.adicionar_peca(oleo_motor, 4)
    else:
        print(f"    Estoque insuficiente!")
    
    print(f"\n Requisitando 1 filtro de óleo...")
    if mecanico.requisitar_estoque(filtro_oleo, 1):
        print(f"    Requisição aprovada! Estoque atualizado: {filtro_oleo.qtd_estoque} unidades")
        ordem_servico.adicionar_peca(filtro_oleo, 1)
    else:
        print(f" Estoque insuficiente!")
    
    print(f"\n Requisitando 1 filtro de ar...")
    if mecanico.requisitar_estoque(filtro_ar, 1):
        print(f"  Requisição aprovada! Estoque atualizado: {filtro_ar.qtd_estoque} unidades")
        ordem_servico.adicionar_peca(filtro_ar, 1)
    else:
        print(f" Estoque insuficiente!")
    
    print(f"\n Requisitando 1 filtro de combustível...")
    if mecanico.requisitar_estoque(filtro_combustivel, 1):
        print(f" Requisição aprovada! Estoque atualizado: {filtro_combustivel.qtd_estoque} unidades")
        ordem_servico.adicionar_peca(filtro_combustivel, 1)
    else:
        print(f" Estoque insuficiente!")
    
    # =====================================================
    # 8. GERAÇÃO DE ORÇAMENTO
    # =====================================================
    print("\n ETAPA 8: Geração de Orçamento")
    linha("-")
    
    orcamento = ordem_servico.gerar_orcamento()
    print(f" Orçamento gerado: R$ {orcamento:,.2f}")
    print(f"   Status da OS: {ordem_servico.status}")
    print(f"   Valor Total de Peças: R$ {ordem_servico.valor_total:,.2f}")
    
    # =====================================================
    # 9. ALTERAÇÃO DE STATUS DA OS (Múltiplas Mudanças)
    # =====================================================
    print("\n ETAPA 9: Mecânico Altera Status da OS")
    linha("-")
    
    print(f"\n Status atual: {ordem_servico.status}")
    
    print(f"\n Cliente aprovou o orçamento...")
    mecanico.alterar_status(ordem_servico, "Aprovado")
    print(f"    Novo status: {ordem_servico.status}")
    
    print(f"\n Mecânico iniciou o serviço...")
    mecanico.alterar_status(ordem_servico, "Em Andamento")
    print(f"    Novo status: {ordem_servico.status}")
    
    # =====================================================
    # 10. RESUMO DA OS EM ANDAMENTO
    # =====================================================
    print("\n ETAPA 10: Resumo da Ordem de Serviço")
    linha("-")
    
    ordem_servico.exibir_resumo()
    
    # =====================================================
    # 11. CONCLUSÃO DO SERVIÇO
    # =====================================================
    print("\n ETAPA 11: Conclusão do Serviço")
    linha("-")
    
    print(f"\n Mecânico finalizou o serviço...")
    ordem_servico.fechar_ordem()
    print(f"   OS concluída com sucesso!")
    print(f"   Status final: {ordem_servico.status}")
    print(f"   Veículos atendidos pelo mecânico: {mecanico.qtd_veiculos_atendidos}")
    
    # =====================================================
    # 12. CÁLCULO FINAL DO SALÁRIO (Polimorfismo)
    # =====================================================
    print("\n ETAPA 12: Cálculo do Salário Final (Polimorfismo)")
    linha("-")
    
    salario_final = mecanico.calcular_salario()
    bonus_ganho = salario_final - salario_inicial
    
    print(f"\n EVOLUÇÃO DO SALÁRIO:")
    print(f"   Salário Inicial: R$ {salario_inicial:,.2f}")
    print(f"   Veículos Atendidos: {mecanico.qtd_veiculos_atendidos}")
    print(f"   Bônus Ganho: R$ {bonus_ganho:,.2f}")
    print(f"   SALÁRIO FINAL: R$ {salario_final:,.2f}")
    print(f"\n   Fórmula: {mecanico.salario_base:,.2f} + ({mecanico.qtd_veiculos_atendidos} × {mecanico.bonus_por_veiculo:,.2f})")

if __name__ == "__main__":
    # Lista global de ordens de serviço criada no main (persistência em memória esta execução)
    orders_list = []
    fluxo_cliente()
    print()
    fluxo_mecanico()
    print()
