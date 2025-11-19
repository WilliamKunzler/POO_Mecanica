from datetime import date

from models.Cliente import Cliente
from models.Veiculo import Veiculo
from models.OrdemServico import OrdemServico
from models.Funcionario import Atendente, Mecanico
from models.Peca import Peca

def fluxo_atendente():
    titulo("   DEMONSTRAÇÃO COMPLETA - ATENDENTE COM MÉTODOS CRUD")
    
    # =====================================================
    # 1. CRIAÇÃO DO ATENDENTE
    # =====================================================
    print("\n   ETAPA 1: Cadastro do Atendente")
    linha("-")
    
    atendente = Atendente(
        nome="Juliana Santos",
        salario_base=3000.00,
        comissao=60.00,
        qtd_clientes=0
    )
    
    print(f"   Atendente: {atendente.nome}")
    print(f"   Salário Base: R$ {atendente.salario_base:,.2f}")
    print(f"   Comissão por Cliente: R$ {atendente.comissao:,.2f}")
    
    # =====================================================
    # 2. CRUD DE CLIENTES
    # =====================================================
    titulo("   CRUD DE CLIENTES")
    
    print("\n CREATE - Criando Clientes")
    linha("-")
    
    # Criando cliente 1
    print("\n   Criando Cliente 1...")
    cliente1 = atendente.criar_cliente(
        nome="Carlos Eduardo Silva",
        qtd_servicos=0,
        satisfacao="Não avaliado"
    )
    
    # Criando cliente 2
    print("\n   Criando Cliente 2...")
    cliente2 = atendente.criar_cliente(
        nome="Beatriz Oliveira",
        qtd_servicos=2,
        satisfacao="Satisfeito"
    )
    
    print(f"\n   Total de clientes cadastrados: {atendente.qtd_clientes}")
    
    # Visualizando clientes
    print("\n    VISUALIZAR - Visualizando Clientes")
    linha("-")
    atendente.visualizar_cliente(cliente1)
    atendente.visualizar_cliente(cliente2)
    
    # Editando cliente
    print("\n    EDITAR - Editando Cliente")
    linha("-")
    print("Atualizando satisfação e nome do Cliente 1...")
    atendente.editar_cliente(
        cliente1,
        nome="Carlos Eduardo Silva Junior",
        satisfacao="Muito Satisfeito"
    )
    atendente.visualizar_cliente(cliente1)
    
    # =====================================================
    # 3. CRUD DE VEÍCULOS
    # =====================================================
    titulo("   CRUD DE VEÍCULOS")
    
    print("\n   CREATE - Criando Veículos")
    linha("-")
    
    # Criando veículo 1 para cliente 1
    print("\n   Criando Veículo para Cliente 1...")
    veiculo1 = atendente.criar_veiculo(
        placa="ABC1234",
        nome_veiculo="Honda Civic",
        modelo="EXL 2.0",
        ano_fabricacao=2022,
        cliente=cliente1
    )
    
    # Criando veículo 2 para cliente 1
    print("\n   Criando Segundo Veículo para Cliente 1...")
    veiculo2 = atendente.criar_veiculo(
        placa="XYZ9876",
        nome_veiculo="Toyota Corolla",
        modelo="Altis 2.0",
        ano_fabricacao=2021,
        cliente=cliente1
    )
    
    # Criando veículo para cliente 2
    print("\n   Criando Veículo para Cliente 2...")
    veiculo3 = atendente.criar_veiculo(
        placa="DEF5678",
        nome_veiculo="Volkswagen Gol",
        modelo="1.0",
        ano_fabricacao=2020,
        cliente=cliente2
    )
    
    # Visualizando veículos
    print("\n    VISUALIZAR - Visualizando Veículos")
    linha("-")
    atendente.visualizar_veiculo(veiculo1)
    atendente.visualizar_veiculo(veiculo2)
    atendente.visualizar_veiculo(veiculo3)
    
    # Editando veículo
    print("\n    EDITAR - Editando Veículo")
    linha("-")
    print("Atualizando modelo do Veículo 1...")
    atendente.editar_veiculo(
        veiculo1,
        modelo="EXL 2.0 Turbo"
    )
    atendente.visualizar_veiculo(veiculo1)
    
    # Visualizando cliente com veículos
    print("\n    Cliente com Veículos Cadastrados")
    linha("-")
    atendente.visualizar_cliente(cliente1)
    
    # =====================================================
    # 4. CRUD DE PEÇAS
    # =====================================================
    titulo("   CRUD DE PEÇAS/ESTOQUE")
    
    print("\n   CREATE - Criando Peças")
    linha("-")
    
    # Criando peça 1
    print("\n   Criando Peça 1...")
    peca1 = atendente.criar_peca(
        nome="Óleo Motor Sintético 5W30",
        descricao="Óleo sintético premium para motores",
        qtd_estoque=50,
        valor_unit=89.90
    )
    
    # Criando peça 2
    print("\n   Criando Peça 2...")
    peca2 = atendente.criar_peca(
        nome="Filtro de Ar",
        descricao="Filtro de ar de alta performance",
        qtd_estoque=30,
        valor_unit=65.00
    )
    
    # Criando peça 3
    print("\n   Criando Peça 3...")
    peca3 = atendente.criar_peca(
        nome="Pastilha de Freio",
        descricao="Pastilha de freio dianteira premium",
        qtd_estoque=20,
        valor_unit=180.00
    )
    
    # Visualizando peças
    print("\n    VISUALIZAR - Visualizando Peças")
    linha("-")
    atendente.visualizar_peca(peca1)
    atendente.visualizar_peca(peca2)
    atendente.visualizar_peca(peca3)
    
    # Editando peça
    print("\n    EDITAR - Editando Peça")
    linha("-")
    print("Atualizando valor da Peça 1...")
    atendente.editar_peca(
        peca1,
        valor_unit=95.00
    )
    atendente.visualizar_peca(peca1)
    
    # Adicionando ao estoque
    print("\n   ADICIONAR ESTOQUE")
    linha("-")
    atendente.adicionar_estoque_peca(peca2, 20)
    atendente.visualizar_peca(peca2)
    
    # Removendo do estoque
    print("\n   REMOVER DO ESTOQUE")
    linha("-")
    atendente.remover_estoque_peca(peca3, 5)
    atendente.visualizar_peca(peca3)
    
    # =====================================================
    # 5. CRUD DE ORDENS DE SERVIÇO
    # =====================================================
    titulo("   CRUD DE ORDENS DE SERVIÇO")
    
    # Criar mecânico para atribuir às OS
    print("\n   Preparação: Criando Mecânico")
    linha("-")
    mecanico = Mecanico(
        nome="Roberto Alves",
        salario_base=3500.00,
        qtd_veiculos_atendidos=0,
        bonus_por_veiculo=150.00
    )
    print(f"   Mecânico criado: {mecanico.nome}")
    
    print("\n   CREATE - Criando Ordens de Serviço")
    linha("-")
    
    # Criando OS 1
    print("\n   Criando OS 1...")
    os1 = atendente.criar_ordem_servico(
        cliente=cliente1,
        veiculo=veiculo1,
        descricao="Troca de óleo e revisão dos 20.000 km"
    )
    
    # Criando OS 2
    print("\n   Criando OS 2...")
    os2 = atendente.criar_ordem_servico(
        cliente=cliente2,
        veiculo=veiculo3,
        descricao="Troca de pastilhas de freio e alinhamento"
    )
    
    # Visualizando OS
    print("\n    VISUALIZAR - Visualizando Ordens de Serviço")
    linha("-")
    atendente.visualizar_ordem_servico(os1)
    atendente.visualizar_ordem_servico(os2)
    
    # Atribuindo mecânico
    print("\n   Atribuindo Mecânico à OS")
    linha("-")
    atendente.atribuir_mecanico_os(os1, mecanico)
    atendente.atribuir_mecanico_os(os2, mecanico)
    
    # Adicionando peças às OS
    print("\n   Adicionando Peças às OS")
    linha("-")
    print("Adicionando peças à OS #4001...")
    os1.adicionar_peca(peca1, 1)
    os1.adicionar_peca(peca2, 1)
    
    print("\nAdicionando peças à OS #4002...")
    os2.adicionar_peca(peca3, 1)
    
    # Gerando orçamentos
    print("\n   Gerando Orçamentos")
    linha("-")
    atendente.gerar_orcamento_os(os1)
    atendente.gerar_orcamento_os(os2)
    
    # Visualizando OS atualizadas
    print("\n    Visualizando OS Atualizadas")
    linha("-")
    atendente.visualizar_ordem_servico(os1)
    atendente.visualizar_ordem_servico(os2)
    
    # Editando OS
    print("\n    EDITAR - Editando Ordem de Serviço")
    linha("-")
    print("Atualizando descrição da OS #4001...")
    atendente.editar_ordem_servico(
        os1,
        descricao="Troca de óleo, filtros e revisão completa dos 20.000 km"
    )
    atendente.visualizar_ordem_servico(os1)
    
    # =====================================================
    # 6. OPERAÇÃO DELETE (REMOVER)
    # =====================================================
    titulo("    OPERAÇÕES DE REMOÇÃO (DELETE)")
    
    # Criar entidades para testar remoção
    print("\n   Criando Cliente de Teste para Remoção...")
    cliente_teste = atendente.criar_cliente(
        nome="Cliente Temporário",
        qtd_servicos=0,
        satisfacao="Não avaliado"
    )
    
    print("\n   Criando Veículo de Teste para Remoção...")
    veiculo_teste = atendente.criar_veiculo(
        placa="TMP0000",
        nome_veiculo="Veículo Teste",
        modelo="Teste",
        ano_fabricacao=2020,
        cliente=cliente_teste
    )
    
    print("\n   Criando Peça de Teste para Remoção...")
    peca_teste = atendente.criar_peca(
        nome="Peça Teste",
        descricao="Para teste de remoção",
        qtd_estoque=10,
        valor_unit=10.00
    )
    
    print("\n   Criando OS de Teste para Remoção...")
    os_teste = atendente.criar_ordem_servico(
        cliente=cliente_teste,
        veiculo=veiculo_teste,
        descricao="OS para teste de remoção"
    )
    
    # Removendo entidades
    print("\n    Removendo Veículo de Teste...")
    atendente.remover_veiculo(veiculo_teste, cliente_teste)
    atendente.visualizar_cliente(cliente_teste)
    
    print("\n    Removendo Peça de Teste...")
    atendente.remover_peca(peca_teste)
    atendente.visualizar_peca(peca_teste)
    
    print("\n    Removendo/Cancelando OS de Teste...")
    atendente.remover_ordem_servico(os_teste)
    atendente.visualizar_ordem_servico(os_teste)
    
    print("\n    Removendo Cliente de Teste...")
    atendente.remover_cliente(cliente_teste)
    
    # =====================================================
    # 7. RELATÓRIO FINAL
    # =====================================================
    titulo("   RELATÓRIO FINAL DO ATENDENTE")
    
    salario_final = atendente.calcular_salario()
    
    print(f"\n    ATENDENTE: {atendente.nome}")
    print(f"    Salário Base: R$ {atendente.salario_base:,.2f}")
    print(f"    Comissão por Cliente: R$ {atendente.comissao:,.2f}")
    print(f"    Clientes Cadastrados: {atendente.qtd_clientes}")
    print(f"    Salário Total: R$ {salario_final:,.2f}")

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
        nome="Óleo Motor Sintético 5W30",
        descricao="Óleo sintético premium para motores",
        qtd_estoque=50,
        valor_unit=89.90
    )
    
    filtro_oleo = Peca(
        nome="Filtro de Óleo",
        descricao="Filtro de óleo original Honda",
        qtd_estoque=30,
        valor_unit=45.50
    )
    
    filtro_ar = Peca(
        nome="Filtro de Ar",
        descricao="Filtro de ar esportivo",
        qtd_estoque=20,
        valor_unit=78.00
    )
    
    filtro_combustivel = Peca(
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
    fluxo_atendente()
    print()