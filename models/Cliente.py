from datetime import date
from models.OrdemServico import OrdemServico

class Cliente:
    
    def __init__(self, nome, id_cliente, qtd_servicos=0, 
                 satisfacao="Não avaliado"):
        self._nome = nome
        self._id_cliente = id_cliente
        self.__qtd_servicos = qtd_servicos
        self._satisfacao = satisfacao
        self._veiculos = []  # Agregação - cliente pode ter múltiplos veículos
    
    @property
    def nome(self):                                                 
        """Getter para nome do cliente."""
        return self._nome
    
    @nome.setter                                                      
    def nome(self, valor):
        """Setter para nome do cliente."""
        if not valor:
            raise ValueError("Nome não pode ser vazio")
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
            raise ValueError(f"Satisfação deve ser uma das opções: {satisfacoes_validas}")
        self._satisfacao = valor
    
    @property                                                        
    def veiculos(self):
        """Getter para lista de veículos."""
        return self._veiculos.copy()  # Retorna cópia para manter encapsulamento
    
    def abrir_chamado(self, veiculo, descricao):                                              
        """Abre um chamado de serviço."""
        nova_os = OrdemServico(
            id_os=len(self._veiculos) + 1,  # Simplificado para exemplo
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
    
    def consultar_os(self):
        # Aqui mostraria a lista real de ordens de serviço do cliente
        ordens = []
        # Lógica para buscar ordens do cliente seria implementada aqui
        return ordens
    
    def incrementar_servicos(self):
        self.__qtd_servicos += 1