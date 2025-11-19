"""
Atendente: Juliana Santos
Salário Base: R$ 3.000,00

Métodos Separados:
- CRIAR: Solicita atributos e retorna instância
- EDITAR: Recebe instância e atualiza dados
- REMOVER: Recebe instância e remove
- VISUALIZAR: Recebe instância e exibe informações
"""

from models.Funcionario import Atendente, Mecanico
from datetime import date

def linha(caractere="=", tamanho=80):
    print(caractere * tamanho)

def titulo(texto):
    linha()
    print(f"  {texto}")
    linha()

def main():
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
    
if __name__ == "__main__":
    main()
