from models.Cliente import Cliente


class ClienteService:
    def criar(self, nome, qtd_servicos=0, satisfacao="Não avaliado", atendente=None):
        cliente = Cliente(
            nome=nome,
            qtd_servicos=qtd_servicos,
            satisfacao=satisfacao,
            atendente_criador=atendente,
        )
        if atendente is not None:
            atendente.qtd_clientes += 1
        return cliente

    @staticmethod
    def editar(cliente, nome=None, satisfacao=None):
        if nome:
            cliente.nome = nome
        if satisfacao:
            cliente.satisfacao = satisfacao
        return cliente

    @staticmethod
    def remover(cliente, clientes_lista, atendente=None):
        if cliente in clientes_lista:
            clientes_lista.remove(cliente)
            if atendente is not None and atendente.qtd_clientes > 0:
                atendente.qtd_clientes -= 1
            return True
        return False
