from models.Veiculo import Veiculo


class VeiculoService:
    @staticmethod
    def criar(placa, nome_veiculo, modelo, ano_fabricacao, cliente):
        veiculo = Veiculo(
            placa=placa,
            nome_veiculo=nome_veiculo,
            modelo=modelo,
            ano_fabricacao=ano_fabricacao,
        )
        cliente._veiculos.append(veiculo)
        return veiculo

    @staticmethod
    def editar(veiculo, nome_veiculo=None, modelo=None):
        if nome_veiculo:
            veiculo.nome_veiculo = nome_veiculo
        if modelo:
            veiculo.modelo = modelo
        return veiculo

    @staticmethod
    def remover(veiculo, cliente):
        if veiculo in cliente._veiculos:
            cliente._veiculos.remove(veiculo)
            return True
        return False
