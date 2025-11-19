from datetime import date
from models.OrdemServico import OrdemServico


class Cliente:

    # Próximo ID disponível para clientes (auto-incremento)
    _next_id = 1

    def __init__(self, nome, veiculos=None, qtd_servicos=0, satisfacao="Não avaliado"):
        self.nome = nome
        # Atribui ID automaticamente (não deve ser passado na instanciação)
        self._id_cliente = Cliente._next_id
        Cliente._next_id += 1
        self.__qtd_servicos = qtd_servicos
        self.satisfacao = satisfacao
        # Permite associar veículos já na instanciação (lista)
        self._veiculos = list(veiculos) if veiculos else []  # Agregação - cliente pode ter múltiplos veículos
    
    @property
    def nome(self):                                                 
        """Getter para nome do cliente."""
        return self._nome
    
    @nome.setter                                                      
    def nome(self, valor):
        """Setter para nome do cliente."""
        if not valor:
            return print("Nome não pode ser vazio")
        self._nome = valor
    
    @property                                                         
    def id_cliente(self):
        """Getter para ID do cliente."""
        return self._id_cliente
    
    @property
    def qtd_servicos(self):
        return self.__qtd_servicos
    
    @property                                                        
    def satisfacao(self):
        """Getter para satisfação do cliente."""
        return self._satisfacao
    
    @satisfacao.setter                                                   
    def satisfacao(self, valor):
        """Setter para satisfação do cliente."""
        satisfacoes_validas = ["Muito Satisfeito", "Satisfeito", "Neutro", "Insatisfeito", "Não avaliado"]
        if valor not in satisfacoes_validas:
            return print(f"Satisfação deve ser uma das opções: {satisfacoes_validas}")
        self._satisfacao = valor
    
    @property                                                        
    def veiculos(self):
        """Getter para lista de veículos."""
        return self._veiculos.copy()  # Retorna cópia para manter encapsulamento

    
    def abrir_chamado(self, veiculo, descricao):                                              
        """Abre um chamado de serviço."""
        nova_os = OrdemServico(
            data_abertura=date.today(),
            status="Aberto",
            descricao=descricao,
            valor_total=0.0,
            cliente=self,
            mecanico=None,
            veiculo=veiculo
        )
        return nova_os
    
    def aprovar_orcamento(self, ordem_servico):                  
        """Aprova um orçamento de serviço."""
        if ordem_servico.status == "Orçamento":
            ordem_servico.alterar_status("Aprovado")
            return True
        return False
    
    def consultar_os(self, orders_list):
        """Retorna as ordens de serviço dessa instância de cliente filtrando
        a partir da lista `orders_list` passada como parâmetro.

        Exemplo: cliente.consultar_os(orders_list)
        """
        if not orders_list:
            return []
        resultado = [o for o in orders_list if getattr(o, 'cliente', None) == self]
        return resultado
    
    def incrementar_servicos(self):
        self.__qtd_servicos += 1