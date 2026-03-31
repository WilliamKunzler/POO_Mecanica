from abc import ABC, abstractmethod


class UsuarioRepository(ABC):
    @abstractmethod
    def buscar_usuario(self, tipo, nome_usuario):
        pass


class OrdemServicoRepository(ABC):
    @abstractmethod
    def listar_ordens_servico(self):
        pass

    @abstractmethod
    def adicionar_ordem_servico(self, ordem_servico):
        pass


class EstoqueRepository(ABC):
    @abstractmethod
    def listar_pecas(self):
        pass

    @abstractmethod
    def adicionar_peca(self, peca):
        pass
