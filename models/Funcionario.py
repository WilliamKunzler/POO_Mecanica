from abc import ABC, abstractmethod

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