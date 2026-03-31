class EstoqueService:
    @staticmethod
    def adicionar_estoque(peca, quantidade):
        peca.adicionar_peca(quantidade)
        return peca

    @staticmethod
    def remover_estoque(peca, quantidade):
        return peca.retirar_peca(quantidade)

    @staticmethod
    def requisitar(mecanico, peca, qtd):
        return mecanico.requisitar_estoque(peca, qtd)
