class SalarioCalculator:
    @staticmethod
    def calcular_salario_atendente(salario_base, qtd_clientes, comissao):
        return max(0.0, salario_base + (qtd_clientes * comissao))

    @staticmethod
    def calcular_salario_mecanico(salario_base, qtd_veiculos, bonus_por_veiculo):
        return max(0.0, salario_base + (qtd_veiculos * bonus_por_veiculo))
