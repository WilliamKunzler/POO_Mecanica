from datetime import date
from models.OrdemServico import OrdemServico


class OrdemServicoService:
    @staticmethod
    def criar(cliente, veiculo, descricao):
        return OrdemServico(
            data_abertura=date.today(),
            status="Aberto",
            descricao=descricao,
            valor_total=0.0,
            cliente=cliente,
            mecanico=None,
            veiculo=veiculo,
        )

    @staticmethod
    def editar(ordem_servico, descricao=None, status=None):
        if descricao:
            ordem_servico.descricao = descricao
        if status:
            ordem_servico.alterar_status(status)
        return ordem_servico

    @staticmethod
    def atribuir_mecanico(ordem_servico, mecanico):
        ordem_servico.atribuir_mecanico(mecanico)
        return ordem_servico

    @staticmethod
    def gerar_orcamento(ordem_servico):
        return ordem_servico.gerar_orcamento()
