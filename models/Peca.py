class Peca:
    
    _next_id = 1  # Atributo de classe para controle de IDs automáticos
    def __init__(self, nome, descricao, 
                 qtd_estoque, valor_unit):
        # Atribui ID automaticamente (não deve ser passado na instanciação)
        self.id = Peca._next_id
        Peca._next_id += 1
        self.nome = nome
        self.descricao = descricao
        self.qtd_estoque = qtd_estoque
        self.valor_unit = valor_unit
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
            return print("Nome deve ser uma string não vazia")
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
            return print("Quantidade em estoque não pode ser negativa")
        self.__qtd_estoque = valor
    
    @property
    def valor_unit(self):
        return self.__valor_unit
    
    @valor_unit.setter
    def valor_unit(self, valor):
        if valor <= 0:
            return print("Valor unitário deve ser positivo")
        self.__valor_unit = valor
    
    def adicionar_peca(self, qtd):
        if qtd > 0:
            self.__qtd_estoque += qtd
    
    def retirar_peca(self, qtd):
        if qtd <= self.__qtd_estoque:
            self.__qtd_estoque -= qtd
            return True
        return False