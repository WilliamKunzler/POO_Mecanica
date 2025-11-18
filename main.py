from datetime import date

from models.Cliente import Cliente
from models.Veiculo import Veiculo
from models.OrdemServico import OrdemServico
from models.Funcionario import Atendente, Mecanico
from models.Peca import Peca

def fluxo_cliente():
    print("--- Fluxo do Cliente ---")
    # Cria veículo primeiro e associa ao cliente na instanciação
    veiculo = Veiculo("ABC1234", "Fusca", "VW", 1980)
    cliente = Cliente("João Silva", veiculos=[veiculo])
    print(f"Cliente criado: {cliente.nome} (ID: {cliente.id_cliente})")
    print(f"Veículo associado ao cliente: {veiculo.exibir_info()}")

    # Abre chamado
    ordem = cliente.abrir_chamado(veiculo, "Troca de óleo e revisão")
    print(f"Chamado aberto: OS #{ordem.id_os} - Status: {ordem.status}")

    # Consulta ordens do cliente
    # Adiciona ordem à lista global de ordens (não usar _registry)
    orders_list.append(ordem)
    # Usa o método do Cliente para consultar suas ordens
    ordens = cliente.consultar_os(orders_list)
    print(f"Ordens encontradas para o cliente {cliente.nome}: {len(ordens)}")
    if ordens:
        # Imprime todas as informações de cada ordem encontrada
        for o in ordens:
            print("--------------------")
            o.exibir_resumo()
        print("--------------------")

if __name__ == "__main__":
    # Lista global de ordens de serviço criada no main (persistência em memória esta execução)
    orders_list = []
    fluxo_cliente()
    print()