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