from models.Cliente import Cliente
from models.Funcionario import (Funcionario, Atendente, Mecanico)
from models.OrdemServico import OrdemServico
from models.Veiculo import Veiculo
from models.Peca import Peca

def regras(): 
    print("==========================")
    print("Testes Veículos")
    print("========================== \n")
    veiculo = Veiculo("222", "gol", "Teste", 2000) # Com placa menor que 7 digitos
    veiculo2 = Veiculo("2223424", "gol", "Teste", 2029) # Com ano de fabricação maior que o ano atual +1
    veiculo3 = Veiculo("2223424", "gol", "Teste", 1800) # Com ano de fabricação menor que 1900
    veiculo4 = Veiculo ("2223424", "", "Teste", 2000) # Com nome de veículo vazio
    
    print("==========================")
    print("Testes Clientes")
    print("========================== \n")
    cliente1 = Cliente("", veiculos=[veiculo, veiculo2, veiculo3, veiculo4], qtd_servicos=1, satisfacao="Muito Satisfeito") #Com nome vazio
    cliente2 = Cliente("Teste", veiculos=[veiculo, veiculo2, veiculo3, veiculo4], qtd_servicos=1, satisfacao="Teste errado") #Com satisfação não está na lista de valores válidos
    

regras()

