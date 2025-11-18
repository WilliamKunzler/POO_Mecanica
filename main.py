"""
Demonstração Completa do Fluxo de um Mecânico
Sistema de Mecânica - POO em Python

Mecânico: José Vilas Boas
Salário Base: R$ 5.000,00
"""

from models.Funcionario import Mecanico
from models.OrdemServico import OrdemServico
from models.Peca import Peca
from models.Cliente import Cliente
from models.Veiculo import Veiculo
from datetime import date

def linha(caractere="=", tamanho=80):
    """Imprime uma linha separadora"""
    print(caractere * tamanho)

def titulo(texto):
    """Imprime um título formatado"""
    linha()
    print(f"  {texto}")
    linha()

def main():
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
    
    cliente = Cliente(
        nome="Maria Silva Santos",
        id_cliente=501,
        qtd_servicos=3,
        satisfacao="Satisfeito"
    )
    
    veiculo = Veiculo(
        placa="XYZ9876",
        nome_veiculo="Honda Civic",
        modelo="EXL 2.0",
        ano_fabricacao=2022
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
        id_os=2001,
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
    main()
