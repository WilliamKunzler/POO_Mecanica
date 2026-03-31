from models.OrdemServico import OrcamentoComponent


class MaoObraComponent(OrcamentoComponent):
    def __init__(self, valor_hora, horas):
        self.valor_hora = valor_hora
        self.horas = horas

    def calcular(self):
        return self.valor_hora * self.horas


class ImpostoComponent(OrcamentoComponent):
    def __init__(self, components, aliquota):
        self.components = components
        self.aliquota = aliquota

    def calcular(self):
        subtotal = sum(component.calcular() for component in self.components)
        return subtotal * self.aliquota
