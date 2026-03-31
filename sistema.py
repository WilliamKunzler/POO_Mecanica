"""
Sistema de Gerenciamento de Mecânica
Classe principal para gerenciar dados do sistema.
"""

from repositories.interfaces import UsuarioRepository, OrdemServicoRepository, EstoqueRepository
from models.Funcionario import Atendente, Mecanico
from services.cliente_service import ClienteService
from services.veiculo_service import VeiculoService
from services.peca_service import PecaService
from services.ordem_servico_service import OrdemServicoService


class SistemaMecanica(UsuarioRepository, OrdemServicoRepository, EstoqueRepository):
    """Classe central para armazenar e gerenciar todos os dados do sistema."""
    
    def __init__(self):
        self.clientes = []
        self.mecanicos = []
        self.atendentes = []
        self.pecas = []
        self.ordens_servico = []

        self.cliente_service = ClienteService()
        self.veiculo_service = VeiculoService()
        self.peca_service = PecaService()
        self.ordem_servico_service = OrdemServicoService()
    
    def buscar_usuario(self, tipo, nome_usuario):
        """Busca um usuário pelo tipo e nome.
        
        Args:
            tipo (str): Tipo do usuário ('Cliente', 'Mecânico', 'Atendente')
            nome_usuario (str): Nome do usuário
        
        Returns:
            Objeto do usuário ou None se não encontrado
        """
        nome_lower = nome_usuario.lower().strip()
        if tipo == "Cliente":
            return next((c for c in self.clientes if c.nome.lower() == nome_lower), None)
        elif tipo == "Mecânico":
            return next((m for m in self.mecanicos if m.nome.lower() == nome_lower), None)
        elif tipo == "Atendente":
            return next((a for a in self.atendentes if a.nome.lower() == nome_lower), None)
        return None

    def listar_ordens_servico(self):
        return self.ordens_servico

    def adicionar_ordem_servico(self, ordem_servico):
        self.ordens_servico.append(ordem_servico)

    def listar_pecas(self):
        return self.pecas

    def adicionar_peca(self, peca):
        self.pecas.append(peca)
    
    def carregar_dados_exemplo(self):
        """Carrega dados de exemplo para demonstração do sistema."""
        # Criar mecânicos primeiro para terem IDs 1 e 2
        mecanico1 = Mecanico(
            nome="Roberto Silva",
            salario_base=3500.00,
            qtd_veiculos_atendidos=0,
            bonus_por_veiculo=150.00
        )
        mecanico2 = Mecanico(
            nome="Carlos Oliveira",
            salario_base=3200.00,
            qtd_veiculos_atendidos=0,
            bonus_por_veiculo=120.00
        )
        self.mecanicos.extend([mecanico1, mecanico2])
        
        # Criar atendentes
        atendente1 = Atendente(
            nome="Juliana Santos",
            salario_base=3000.00,
            comissao=60.00,
            qtd_clientes=0
        )
        self.atendentes.append(atendente1)
        
        # Criar clientes
        cliente1 = self.cliente_service.criar(
            nome="Ana Maria Costa",
            qtd_servicos=0,
            satisfacao="Não avaliado",
            atendente=atendente1,
        )
        self.clientes.append(cliente1)
        
        cliente2 = self.cliente_service.criar(
            nome="Pedro Henrique Lima",
            qtd_servicos=1,
            satisfacao="Satisfeito",
            atendente=atendente1,
        )
        self.clientes.append(cliente2)
        
        cliente3 = self.cliente_service.criar(
            nome="Mariana Fernandes",
            qtd_servicos=0,
            satisfacao="Não avaliado",
            atendente=atendente1,
        )
        self.clientes.append(cliente3)
        
        # Criar veículos
        veiculo1 = self.veiculo_service.criar(
            placa="ABC1234",
            nome_veiculo="Honda Civic",
            modelo="EXL 2.0",
            ano_fabricacao=2022,
            cliente=cliente1,
        )
        
        veiculo2 = self.veiculo_service.criar(
            placa="XYZ9876",
            nome_veiculo="Toyota Corolla",
            modelo="Altis 2.0",
            ano_fabricacao=2021,
            cliente=cliente1,
        )
        
        veiculo3 = self.veiculo_service.criar(
            placa="DEF5678",
            nome_veiculo="Volkswagen Golf",
            modelo="GTI",
            ano_fabricacao=2023,
            cliente=cliente2,
        )
        
        veiculo4 = self.veiculo_service.criar(
            placa="GHI9012",
            nome_veiculo="Chevrolet Onix",
            modelo="Premier",
            ano_fabricacao=2020,
            cliente=cliente3,
        )
        
        # Criar peças
        peca1 = self.peca_service.criar(
            nome="Filtro de Óleo",
            descricao="Filtro de óleo premium",
            qtd_estoque=50,
            valor_unit=35.90,
        )
        self.pecas.append(peca1)
        
        peca2 = self.peca_service.criar(
            nome="Pastilha de Freio",
            descricao="Pastilha de freio dianteira",
            qtd_estoque=30,
            valor_unit=120.00,
        )
        self.pecas.append(peca2)
        
        peca3 = self.peca_service.criar(
            nome="Vela de Ignição",
            descricao="Vela de ignição NGK",
            qtd_estoque=100,
            valor_unit=25.50,
        )
        self.pecas.append(peca3)
        
        peca4 = self.peca_service.criar(
            nome="Óleo de Motor",
            descricao="Óleo sintético 5W30",
            qtd_estoque=80,
            valor_unit=45.00,
        )
        self.pecas.append(peca4)
        
        peca5 = self.peca_service.criar(
            nome="Correia Dentada",
            descricao="Correia dentada com kit",
            qtd_estoque=20,
            valor_unit=280.00,
        )
        self.pecas.append(peca5)
        
        # Criar algumas ordens de serviço
        os1 = self.ordem_servico_service.criar(
            cliente=cliente1,
            veiculo=veiculo1,
            descricao="Troca de óleo e filtros. Revisão dos 10.000 km.",
        )
        os1.atribuir_mecanico(mecanico1)
        os1.adicionar_peca(peca1, 1)
        os1.adicionar_peca(peca4, 4)
        self.ordens_servico.append(os1)
        
        os2 = self.ordem_servico_service.criar(
            cliente=cliente2,
            veiculo=veiculo3,
            descricao="Substituição de pastilhas de freio e revisão do sistema.",
        )
        os2.atribuir_mecanico(mecanico2)
        os2.adicionar_peca(peca2, 2)
        os2.alterar_status("Orçamento")
        self.ordens_servico.append(os2)
        
        os3 = self.ordem_servico_service.criar(
            cliente=cliente3,
            veiculo=veiculo4,
            descricao="Troca de velas de ignição e limpeza do sistema de injeção.",
        )
        self.ordens_servico.append(os3)
        
        print("\n✅ Dados de exemplo carregados com sucesso!")
        print(f"   - {len(self.atendentes)} Atendente(s)")
        print(f"   - {len(self.mecanicos)} Mecânico(s)")
        print(f"   - {len(self.clientes)} Cliente(s)")
        print(f"   - {len(self.pecas)} Peça(s) no estoque")
        print(f"   - {len(self.ordens_servico)} Ordem(ns) de Serviço")
        print("\n📝 Credenciais de acesso:")
        print(f"   Cliente: IDs {cliente1.id_cliente}, {cliente2.id_cliente}, {cliente3.id_cliente}")
        print(f"   Mecânico: IDs {mecanico1.id}, {mecanico2.id}")
        print(f"   Atendente: ID {atendente1.id}")
