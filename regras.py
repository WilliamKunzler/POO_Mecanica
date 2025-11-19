
from models.Cliente import Cliente
from models.Funcionario import (Funcionario, Mecanico, Atendente)
from models.Peca import Peca
from models.OrdemServico import OrdemServico
from models.Veiculo import Veiculo


def regras():
    func1 = Mecanico("João", 1500.0, qtd_veiculos_atendidos=5, bonus_por_veiculo=150.0)
    func2 = Atendente("Maria", 2500.0, comissao=0.05, qtd_clientes=10)

    
    print("==========================")
    print("Testes Atendente")
    print("==========================\n")
    print(f"Atendente: {func2.nome}, ID: {func2._id}")
    print(f"Salário do atendente: $ {func2.calcular_salario()}")  # Salário do atendente
    func2.nome = ""
    func2.salario_base = 0.0
    func2.qtd_clientes = -2
    func2.comissao = -0.1


    print("\n==========================")
    print("Testes Mecânico")
    print("==========================\n")
    print(f"Mecânico: {func1.nome}, ID: {func1._id}")
    print(f"Salário do mecânico: $ {func1.calcular_salario()}")  # Salário do mecânico
    func1.nome = ""
    func1.salario_base = -500.0
    func1.qtd_veiculos_atendidos = -3
    func1.bonus_por_veiculo = -100.0

    print("\n==========================")
    print("Testes Peça")
    print("==========================\n")
    amortecedor = Peca("Amortecedor", "Peça para absorver impactos", 5, 300.0)
    print(f"Peça: {amortecedor.nome}, Estoque: {amortecedor.qtd_estoque}, Valor Unitário: $ {amortecedor.valor_unit}")

    func1.requisitar_estoque(amortecedor, 3)
    print(f"Após requisição, Estoque: {amortecedor.qtd_estoque}")

    amortecedor.qtd_estoque = -10  
    amortecedor.valor_unit = -50.0  

    amortecedor.adicionar_peca(11)
    amortecedor.retirar_peca(4)
    print(f"Após adicionar peças, Estoque: {amortecedor.qtd_estoque}")

    if(not func1.requisitar_estoque(amortecedor, 5)):
        print("Requisição falhou: Estoque insuficiente")
    







regras()