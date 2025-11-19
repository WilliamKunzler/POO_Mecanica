from abc import ABC, abstractmethod

class Funcionario(ABC):
    """Classe abstrata para funcionários da mecânica."""
    
    _next_id = 1
    
    def __init__(self, nome, salario_base):

        self.nome = nome
        # Atribui ID automaticamente (não deve ser passado na instanciação)
        self._id = Funcionario._next_id
        Funcionario._next_id += 1
        self.salario_base = salario_base
    
    @property                                                           
    def nome(self):
        """Getter para o nome do funcionário."""
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if not valor:
            return print("Nome deve ser uma string não vazia")
        self._nome = valor
    
    @property
    def id(self):
        return self._id
    
    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self, valor):
        if not valor or valor <= 0:
            return print("Salário base deve ser positivo")
        self.__salario_base = valor
    
    @abstractmethod                                                     
    def calcular_salario(self):
        """Método abstrato para calcular o salário do funcionário."""
        pass


class Mecanico(Funcionario):
    
    def __init__(self, nome, salario_base,              
                 qtd_veiculos_atendidos=0, bonus_por_veiculo=0.0):
        super().__init__(nome, salario_base)
        self.qtd_veiculos_atendidos = qtd_veiculos_atendidos
        self.bonus_por_veiculo = bonus_por_veiculo
    
    @property
    def qtd_veiculos_atendidos(self):                                   
        """Getter para quantidade de veículos atendidos."""
        return self._qtd_veiculos_atendidos
    
    @qtd_veiculos_atendidos.setter                                      
    def qtd_veiculos_atendidos(self, valor):
        """Setter para quantidade de veículos atendidos."""
        if valor < 0:
            return print("Quantidade de veículos não pode ser negativa")
        self._qtd_veiculos_atendidos = valor
    
    @property
    def bonus_por_veiculo(self):
        return self.__bonus_por_veiculo
    
    @bonus_por_veiculo.setter
    def bonus_por_veiculo(self, valor):
        if valor < 0:
            return print("Bônus não pode ser negativo")
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
    
    def __init__(self, nome, salario_base, 
                 comissao=0.0, qtd_clientes=0):
        super().__init__(nome, salario_base)
        self.comissao = comissao
        self.qtd_clientes = qtd_clientes
    
    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, valor):
        if valor < 0:
            return print("Comissão não pode ser negativa")
        self.__comissao = valor
    
    @property                                                           
    def qtd_clientes(self):
        """Getter para quantidade de clientes."""
        return self._qtd_clientes
    
    @qtd_clientes.setter                                                
    def qtd_clientes(self, valor):
        """Setter para quantidade de clientes."""
        if valor < 0:
            return print("Quantidade de clientes não pode ser negativa")
        self._qtd_clientes = valor
    
    # ========== MÉTODOS DE CLIENTE ==========
    
    def criar_cliente(self, nome, qtd_servicos=0, satisfacao="Não avaliado"):
        """Cria um novo cliente solicitando atributos."""
        from models.Cliente import Cliente
        
        try:
            novo_cliente = Cliente(
                nome=nome,
                qtd_servicos=qtd_servicos,
                satisfacao=satisfacao
            )
            self._qtd_clientes += 1
            print(f"   Cliente {novo_cliente.nome} criado com sucesso!")
            print(f"   ID: {novo_cliente.id_cliente}")
            print(f"   Satisfação: {novo_cliente.satisfacao}")
            return novo_cliente
        except ValueError as e:
            print(f"❌ Erro ao criar cliente: {e}")
            return None
    
    def editar_cliente(self, cliente, nome=None, satisfacao=None):
        """Edita dados de um cliente existente."""
        try:
            if nome:
                cliente.nome = nome
            if satisfacao:
                cliente.satisfacao = satisfacao
            print(f"   Cliente {cliente.nome} editado com sucesso!")
            return True
        except ValueError as e:
            print(f"  Erro ao editar cliente: {e}")
            return False
    
    def remover_cliente(self, cliente):
        """Remove um cliente do sistema."""
        if self._qtd_clientes > 0:
            self._qtd_clientes -= 1
        print(f"   Cliente {cliente.nome} (ID: {cliente.id_cliente}) removido do sistema!")
        return True
    
    def visualizar_cliente(self, cliente):
        """Visualiza informações detalhadas de um cliente."""
        print(f"\n{'='*50}")
        print(f"   INFORMAÇÕES DO CLIENTE")
        print(f"{'='*50}")
        print(f"Nome: {cliente.nome}")
        print(f"ID: {cliente.id_cliente}")
        print(f"Serviços Realizados: {cliente.qtd_servicos}")
        print(f"Satisfação: {cliente.satisfacao}")
        print(f"Veículos Cadastrados: {len(cliente.veiculos)}")
        for i, veiculo in enumerate(cliente.veiculos, 1):
            print(f"  {i}. {veiculo.nome_veiculo} - {veiculo.placa}")
        print(f"{'='*50}\n")
        return True
    
    # ========== MÉTODOS DE VEÍCULO ==========
    
    def criar_veiculo(self, placa, nome_veiculo, modelo, ano_fabricacao, cliente):
        """Cria um novo veículo e associa a um cliente."""
        from models.Veiculo import Veiculo
        
        try:
            novo_veiculo = Veiculo(
                placa=placa,
                nome_veiculo=nome_veiculo,
                modelo=modelo,
                ano_fabricacao=ano_fabricacao
            )
            cliente._veiculos.append(novo_veiculo)
            print(f"   Veículo {novo_veiculo.nome_veiculo} ({novo_veiculo.placa}) criado e associado a {cliente.nome}!")
            return novo_veiculo
        except ValueError as e:
            print(f"  Erro ao criar veículo: {e}")
            return None
    
    def editar_veiculo(self, veiculo, nome_veiculo=None, modelo=None):
        """Edita dados de um veículo existente."""
        try:
            if nome_veiculo:
                veiculo.nome_veiculo = nome_veiculo
            if modelo:
                veiculo.modelo = modelo
            print(f"   Veículo {veiculo.placa} editado com sucesso!")
            return True
        except ValueError as e:
            print(f"  Erro ao editar veículo: {e}")
            return False
    
    def remover_veiculo(self, veiculo, cliente):
        """Remove um veículo de um cliente."""
        if veiculo in cliente._veiculos:
            cliente._veiculos.remove(veiculo)
            print(f"   Veículo {veiculo.placa} removido de {cliente.nome}!")
            return True
        else:
            print(f"  Veículo {veiculo.placa} não encontrado para o cliente {cliente.nome}!")
            return False
    
    def visualizar_veiculo(self, veiculo):
        """Visualiza informações detalhadas de um veículo."""
        print(f"\n{'='*50}")
        print(f"   INFORMAÇÕES DO VEÍCULO")
        print(f"{'='*50}")
        print(f"Placa: {veiculo.placa}")
        print(f"Veículo: {veiculo.nome_veiculo}")
        print(f"Modelo: {veiculo.modelo}")
        print(f"Ano de Fabricação: {veiculo.ano_fabricacao}")
        print(f"Idade: {veiculo.calcular_idade()} anos")
        print(f"{'='*50}\n")
        return True
    
    # ========== MÉTODOS DE ORDEM DE SERVIÇO ==========
    
    def criar_ordem_servico(self, cliente, veiculo, descricao):
        """Cria uma nova ordem de serviço."""
        from models.OrdemServico import OrdemServico
        from datetime import date
        
        try:
            nova_os = OrdemServico(
                data_abertura=date.today(),
                status="Aberto",
                descricao=descricao,
                valor_total=0.0,
                cliente=cliente,
                mecanico=None,
                veiculo=veiculo
            )
            print(f" Ordem de Serviço #{nova_os.id_os} criada por {self.nome}")
            print(f"   Cliente: {cliente.nome}")
            print(f"   Veículo: {veiculo.nome_veiculo} ({veiculo.placa})")
            print(f"   Descrição: {descricao}")
            return nova_os
        except ValueError as e:
            print(f"  Erro ao criar OS: {e}")
            return None
    
    def editar_ordem_servico(self, ordem_servico, descricao=None, status=None):
        """Edita dados de uma ordem de serviço existente."""
        try:
            if descricao:
                ordem_servico.descricao = descricao
            if status:
                ordem_servico.alterar_status(status)
            print(f"   OS #{ordem_servico.id_os} editada com sucesso!")
            return True
        except ValueError as e:
            print(f"  Erro ao editar OS: {e}")
            return False
    
    def remover_ordem_servico(self, ordem_servico):
        """Remove/Cancela uma ordem de serviço."""
        ordem_servico.alterar_status("Cancelado")
        print(f"   OS #{ordem_servico.id_os} cancelada/removida!")
        return True
    
    def visualizar_ordem_servico(self, ordem_servico):
        """Visualiza informações detalhadas de uma ordem de serviço."""
        print(f"\n{'='*50}")
        print(f" INFORMAÇÕES DA ORDEM DE SERVIÇO")
        print(f"{'='*50}")
        ordem_servico.exibir_resumo()
        print(f"{'='*50}\n")
        return True
    
    def atribuir_mecanico_os(self, ordem_servico, mecanico):
        """Atribui um mecânico a uma ordem de serviço."""
        ordem_servico.atribuir_mecanico(mecanico)
        print(f"   Mecânico {mecanico.nome} atribuído à OS #{ordem_servico.id_os}")
        return True
    
    def gerar_orcamento_os(self, ordem_servico):
        """Gera orçamento para uma ordem de serviço."""
        valor = ordem_servico.gerar_orcamento()
        print(f"   Orçamento gerado para OS #{ordem_servico.id_os}: R$ {valor:,.2f}")
        return valor
    
    # ========== MÉTODOS DE PEÇA/ESTOQUE ==========
    
    def criar_peca(self, nome, descricao, qtd_estoque, valor_unit):
        """Cria uma nova peça no estoque."""
        from models.Peca import Peca
        
        try:
            nova_peca = Peca(
                nome=nome,
                descricao=descricao,
                qtd_estoque=qtd_estoque,
                valor_unit=valor_unit
            )
            print(f"   Peça {nova_peca.nome} criada no estoque!")
            print(f"   ID: {nova_peca.id}")
            print(f"   Quantidade: {nova_peca.qtd_estoque}")
            print(f"   Valor Unitário: R$ {nova_peca.valor_unit:.2f}")
            return nova_peca
        except ValueError as e:
            print(f"  Erro ao criar peça: {e}")
            return None
    
    def editar_peca(self, peca, nome=None, descricao=None, valor_unit=None):
        """Edita dados de uma peça existente."""
        try:
            if nome:
                peca.nome = nome
            if descricao:
                peca.descricao = descricao
            if valor_unit:
                peca.valor_unit = valor_unit
            print(f"   Peça {peca.nome} editada com sucesso!")
            return True
        except ValueError as e:
            print(f"  Erro ao editar peça: {e}")
            return False
    
    def remover_peca(self, peca):
        """Remove uma peça do estoque (zera quantidade)."""
        peca.qtd_estoque = 0
        print(f"   Peça {peca.nome} removida do estoque!")
        return True
    
    def visualizar_peca(self, peca):
        """Visualiza informações detalhadas de uma peça."""
        print(f"\n{'='*50}")
        print(f"   INFORMAÇÕES DA PEÇA")
        print(f"{'='*50}")
        print(f"Nome: {peca.nome}")
        print(f"Descrição: {peca.descricao}")
        print(f"Quantidade em Estoque: {peca.qtd_estoque}")
        print(f"Valor Unitário: R$ {peca.valor_unit:.2f}")
        print(f"Valor Total em Estoque: R$ {(peca.qtd_estoque * peca.valor_unit):.2f}")
        print(f"{'='*50}\n")
        return True
    
    def adicionar_estoque_peca(self, peca, quantidade):
        """Adiciona quantidade ao estoque de uma peça."""
        peca.adicionar_peca(quantidade)
        print(f"   {quantidade} unidade(s) de {peca.nome} adicionada(s) ao estoque!")
        print(f"   Estoque atual: {peca.qtd_estoque}")
        return True
    
    def remover_estoque_peca(self, peca, quantidade):
        """Remove quantidade do estoque de uma peça."""
        if peca.retirar_peca(quantidade):
            print(f"   {quantidade} unidade(s) de {peca.nome} removida(s) do estoque!")
            print(f"   Estoque atual: {peca.qtd_estoque}")
            return True
        else:
            print(f"  Estoque insuficiente de {peca.nome}! Disponível: {peca.qtd_estoque}")
            return False
    
    def calcular_salario(self):
        return self.salario_base + (self._qtd_clientes * self.comissao)