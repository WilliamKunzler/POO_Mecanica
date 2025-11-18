"""
Módulo de modelos para o sistema de mecânica.
"""

from abc import ABC, abstractmethod
from datetime import date


class Funcionario(ABC):
    """Classe abstrata para funcionários da mecânica."""
    
    def __init__(self, nome, id_funcionario, salario_base):
        self._nome = nome
        self._id = id_funcionario
        self.__salario_base = salario_base
    
    @property                                                           
    def nome(self):
        """Getter para o nome do funcionário."""
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome deve ser uma string não vazia")
        self._nome = valor
    
    @property
    def id(self):
        return self._id
    
    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self, valor):
        if valor <= 0:
            raise ValueError("Salário base deve ser positivo")
        self.__salario_base = valor
    
    @abstractmethod                                                     
    def calcular_salario(self):
        """Método abstrato para calcular o salário do funcionário."""
        pass


class Mecanico(Funcionario):
    
    def __init__(self, nome, id_funcionario, salario_base,              
                 qtd_veiculos_atendidos=0, bonus_por_veiculo=0.0):
        super().__init__(nome, id_funcionario, salario_base)
        self._qtd_veiculos_atendidos = qtd_veiculos_atendidos
        self.__bonus_por_veiculo = bonus_por_veiculo
    
    @property
    def qtd_veiculos_atendidos(self):                                   
        """Getter para quantidade de veículos atendidos."""
        return self._qtd_veiculos_atendidos
    
    @qtd_veiculos_atendidos.setter                                      
    def qtd_veiculos_atendidos(self, valor):
        """Setter para quantidade de veículos atendidos."""
        if valor < 0:
            raise ValueError("Quantidade de veículos não pode ser negativa")
        self._qtd_veiculos_atendidos = valor
    
    @property
    def bonus_por_veiculo(self):
        return self.__bonus_por_veiculo
    
    @bonus_por_veiculo.setter
    def bonus_por_veiculo(self, valor):
        if valor < 0:
            raise ValueError("Bônus não pode ser negativo")
        self.__bonus_por_veiculo = valor
    
    def alterar_status(self, ordem_servico, novo_status):                              
        """Altera o status de uma ordem de serviço."""
        ordem_servico.alterar_status(novo_status)
    
    def requisitar_estoque(self, peca, qtd):                            
        """Requisita uma peça do estoque."""
        if peca.qtd_estoque >= qtd:
            peca.qtd_estoque -= qtd
            return True
        return False
    
    def calcular_salario(self):
        return self.salario_base + (self._qtd_veiculos_atendidos * self.bonus_por_veiculo)


class Atendente(Funcionario):
    
    def __init__(self, nome, id_funcionario, salario_base, 
                 comissao=0.0, qtd_clientes=0):
        super().__init__(nome, id_funcionario, salario_base)
        self.__comissao = comissao
        self._qtd_clientes = qtd_clientes
    
    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, valor):
        if valor < 0:
            raise ValueError("Comissão não pode ser negativa")
        self.__comissao = valor
    
    @property                                                           
    def qtd_clientes(self):
        """Getter para quantidade de clientes."""
        return self._qtd_clientes
    
    @qtd_clientes.setter                                                
    def qtd_clientes(self, valor):
        """Setter para quantidade de clientes."""
        if valor < 0:
            raise ValueError("Quantidade de clientes não pode ser negativa")
        self._qtd_clientes = valor
    
    def gerenciar_cliente(self, acao, cliente):                         
        """Gerencia ações relacionadas aos clientes."""
        if acao == "adicionar":
            self._qtd_clientes += 1
        elif acao == "remover" and self._qtd_clientes > 0:
            self._qtd_clientes -= 1
    
    def gerenciar_veiculos(self, acao, veiculo):                        
        """Gerencia ações relacionadas aos veículos."""
        print(f"Gerenciando veículo: {acao} - {veiculo.nome_veiculo}")
    
    def gerenciar_os(self, acao, ordem_servico):                         
        """Gerencia ordens de serviço."""
        print(f"Gerenciando OS: {acao} - OS #{ordem_servico.id_os}")
    
    def gerenciar_estoque(self, acao, peca):                           
        """Gerencia estoque de peças."""
        print(f"Gerenciando estoque: {acao} - {peca.nome}")
    
    def calcular_salario(self):
        return self.salario_base + (self._qtd_clientes * self.comissao)


class Peca:
    
    def __init__(self, id_peca, nome, descricao, 
                 qtd_estoque, valor_unit):
        self._id = id_peca
        self._nome = nome
        self._descricao = descricao
        self.__qtd_estoque = qtd_estoque
        self.__valor_unit = valor_unit
    
    @property                                                         
    def id(self):
        """Getter para ID da peça."""
        return self._id
    
    @property                                                         
    def nome(self):
        """Getter para nome da peça."""
        return self._nome
    
    @nome.setter                                                   
    def nome(self, valor):
        """Setter para nome da peça."""
        if not valor:
            raise ValueError("Nome deve ser uma string não vazia")
        self._nome = valor
    
    @property                                                        
    def descricao(self):
        """Getter para descrição da peça."""
        return self._descricao
    
    @descricao.setter                                               
    def descricao(self, valor):
        """Setter para descrição da peça."""
        self._descricao = valor
    
    @property
    def qtd_estoque(self):
        return self.__qtd_estoque
    
    @qtd_estoque.setter
    def qtd_estoque(self, valor):
        if valor < 0:
            raise ValueError("Quantidade em estoque não pode ser negativa")
        self.__qtd_estoque = valor
    
    @property
    def valor_unit(self):
        return self.__valor_unit
    
    @valor_unit.setter
    def valor_unit(self, valor):
        if valor <= 0:
            raise ValueError("Valor unitário deve ser positivo")
        self.__valor_unit = valor
    
    def adicionar_peca(self, qtd):
        if qtd > 0:
            self.__qtd_estoque += qtd
    
    def retirar_peca(self, qtd):
        if qtd <= self.__qtd_estoque:
            self.__qtd_estoque -= qtd
            return True
        return False


class Veiculo:
    
    def __init__(self, placa, nome_veiculo, modelo, ano_fabricacao):  
        self._placa = placa
        self._nome_veiculo = nome_veiculo
        self._modelo = modelo
        self._ano_fabricacao = ano_fabricacao
    
    @property                                                         
    def placa(self):
        """Getter para placa do veículo."""
        return self._placa
    
    @placa.setter                                                   
    def placa(self, valor):
        """Setter para placa do veículo."""
        if not valor or len(valor) < 7:
            raise ValueError("Placa deve ter formato válido")
        self._placa = valor
    
    @property                                                       
    def nome_veiculo(self):
        """Getter para nome do veículo."""
        return self._nome_veiculo
    
    @nome_veiculo.setter                                                  
    def nome_veiculo(self, valor):
        """Setter para nome do veículo."""
        if not valor:
            raise ValueError("Nome do veículo não pode ser vazio")
        self._nome_veiculo = valor
    
    @property                                                       
    def modelo(self):
        """Getter para modelo do veículo."""
        return self._modelo
    
    @modelo.setter                                                   
    def modelo(self, valor):
        """Setter para modelo do veículo."""
        self._modelo = valor
    
    @property                                                      
    def ano_fabricacao(self):
        """Getter para ano de fabricação."""
        return self._ano_fabricacao
    
    @ano_fabricacao.setter                                                 
    def ano_fabricacao(self, valor):
        """Setter para ano de fabricação."""
        if valor < 1900 or valor > 2025:
            raise ValueError("Ano de fabricação inválido")
        self._ano_fabricacao = valor
    
    def exibir_info(self):                                                
        """Retorna informações do veículo."""
        return f"{self._nome_veiculo} {self._modelo} ({self._ano_fabricacao}) - Placa: {self._placa}"
    
    def calcular_idade(self):                                                
        """Calcula a idade do veículo."""
        return date.today().year - self._ano_fabricacao
    

    
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
        from datetime import date
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


class OrdemServico:
    
    def __init__(self, id_os, data_abertura, status, 
                 descricao, valor_total, cliente, 
                 mecanico=None, veiculo=None):
        self._id_os = id_os
        self._data_abertura = data_abertura
        self._status = status
        self._descricao = descricao
        self.__valor_total = valor_total
        self._cliente = cliente  # Associação
        self._mecanico = mecanico  # Associação
        self._pecas = []  # Composição - peças fazem parte da OS
        self._veiculo = veiculo  # Associação
    
    @property                                                   
    def id_os(self):
        """Getter para ID da ordem de serviço."""
        return self._id_os
    
    @property                                                   
    def data_abertura(self):
        """Getter para data de abertura."""
        return self._data_abertura
    
    @property                                                  
    def status(self):
        """Getter para status da OS."""
        return self._status
    
    @property                                                
    def descricao(self):
        """Getter para descrição da OS."""
        return self._descricao
    
    @descricao.setter                                               
    def descricao(self, valor):
        """Setter para descrição da OS."""
        self._descricao = valor
    
    @property
    def valor_total(self):
        return self.__valor_total
    
    @property                                               
    def cliente(self):
        """Getter para cliente da OS."""
        return self._cliente
    
    @property                                             
    def mecanico(self):
        """Getter para mecânico da OS."""
        return self._mecanico
    
    @property                                           
    def veiculo(self):
        """Getter para veículo da OS."""
        return self._veiculo
    
    @property                                              
    def pecas(self):
        """Getter para lista de peças."""
        return self._pecas.copy()
    
    def adicionar_peca(self, peca, qtd):                                            
        """Adiciona uma peça à ordem de serviço."""
        for _ in range(qtd):
            self._pecas.append(peca)
        self.calcular_total()
    
    def remover_peca(self, peca):                                         
        """Remove uma peça da ordem de serviço."""
        if peca in self._pecas:
            self._pecas.remove(peca)
            self.calcular_total()
    
    def calcular_total(self):
        total_pecas = sum(peca.valor_unit for peca in self._pecas)
        self.__valor_total = total_pecas
        return self.__valor_total
    
    def alterar_status(self, novo_status):                                          
        """Altera o status da ordem de serviço."""
        status_validos = ["Aberto", "Orçamento", "Aprovado", "Em Andamento", "Concluído", "Cancelado"]
        if novo_status in status_validos:
            self._status = novo_status
        else:
            raise ValueError(f"Status deve ser um dos: {status_validos}")
    
    def atribuir_mecanico(self, mecanico):                                         
        """Atribui um mecânico à ordem de serviço."""
        self._mecanico = mecanico
    
    def atribuir_veiculo(self, veiculo):                                        
        """Atribui um veículo à ordem de serviço."""
        self._veiculo = veiculo
    
    def gerar_orcamento(self):
        self.calcular_total()
        self.alterar_status("Orçamento")
        return self.valor_total
    
    def fechar_ordem(self):                                         
        """Fecha a ordem de serviço."""
        if self._status == "Em Andamento":
            self.alterar_status("Concluído")
            if self._mecanico:
                self._mecanico.qtd_veiculos_atendidos += 1
    
    def exibir_resumo(self):
        print(f"OS #{self._id_os} - {self._status}")
        print(f"Cliente: {self._cliente.nome}")
        if self._veiculo:
            print(f"Veículo: {self._veiculo.exibir_info()}")
        if self._mecanico:
            print(f"Mecânico: {self._mecanico.nome}")
        print(f"Valor Total: R$ {self.__valor_total:.2f}")
        print(f"Peças utilizadas: {len(self._pecas)}")