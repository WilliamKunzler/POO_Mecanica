from models.Peca import Peca


class PecaService:
    @staticmethod
    def criar(nome, descricao, qtd_estoque, valor_unit):
        return Peca(
            nome=nome,
            descricao=descricao,
            qtd_estoque=qtd_estoque,
            valor_unit=valor_unit,
        )

    @staticmethod
    def editar(peca, nome=None, descricao=None, valor_unit=None):
        if nome:
            peca.nome = nome
        if descricao:
            peca.descricao = descricao
        if valor_unit is not None:
            peca.valor_unit = valor_unit
        return peca
