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