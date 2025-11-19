
from models.Cliente import Cliente
from models.Funcionario import (Funcionario, Mecanico, Atendente)
from models.Peca import Peca
from models.OrdemServico import OrdemServico
from models.Veiculo import Veiculo


def regra():
    func1 = Mecanico("João", 1500.0, qtd_veiculos_atendidos=5, bonus_por_veiculo=150.0)
    func2 = Atendente("Maria", 2500.0, comissao=0.05, qtd_clientes=10)
    
    print("==========================")
    print("Testes Atendente")
    print("==========================\n")

    print(f"Atendente: {func2.nome}, ID: {func2._id}")
    func3 = Atendente("Ana", 0.0, comissao=0.1, qtd_clientes=20) # salario base 0
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
    func4 = Mecanico("Jair", 0.0, bonus_por_veiculo=0.1, qtd_veiculos_atendidos=20) # salario base 0

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
    
    print("\n==========================")
    print("Testes Veículos")
    print("========================== \n")
    veiculo = Veiculo("222", "gol", "Teste", 2000) # Com placa menor que 7 digitos
    veiculo2 = Veiculo("2223424", "gol", "Teste", 2029) # Com ano de fabricação maior que o ano atual +1
    veiculo3 = Veiculo("2223424", "gol", "Teste", 1800) # Com ano de fabricação menor que 1900
    veiculo4 = Veiculo ("2223424", "", "Teste", 2000) # Com nome de veículo vazio
    veiculo5 = Veiculo ("2223424", "Palio", "Teste", 2015)

    print("\n==========================")
    print("Testes Clientes")
    print("========================== \n")
    cliente1 = Cliente("", veiculos=[veiculo, veiculo2, veiculo3, veiculo4], qtd_servicos=1, satisfacao="Muito Satisfeito") #Com nome vazio
    cliente2 = Cliente("Teste", veiculos=[veiculo, veiculo2, veiculo3, veiculo4], qtd_servicos=1, satisfacao="Teste errado") #Com satisfação não está na lista de valores válidos
    
    cliente1.qtd_servicos = -5
    cliente1.abrir_chamado(veiculo, "Teste de chamado")


    print("\n==========================")
    print("Testes OS")
    print("========================== \n")
    os1 = OrdemServico(data_abertura="2023-10-10", descricao="Troca de óleo", cliente=cliente1, valor_total=0.0, status="Aberto", mecanico=func1, veiculo=veiculo)
    os2 = OrdemServico(data_abertura="2023-10-10", descricao="Troca de óleo", cliente=cliente1, valor_total=100.0, status="Orçamento", mecanico=func1, veiculo=veiculo5) # Com status inválido
    
    
    cliente1.aprovar_orcamento(os2)
    if(not cliente1.aprovar_orcamento(os1)):
        print("Orçamento não pode ser aprovado.")

    os2.adicionar_peca(amortecedor, 2)
    print(f"Valor orçamento os2: {os2.gerar_orcamento()}")
    os2.exibir_resumo()

regra()