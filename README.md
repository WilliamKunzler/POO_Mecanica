# Sistema de Mecânica - Programação Orientada a Objetos

Este projeto implementa um sistema de mecânica completo em Python, aplicando todos os conceitos fundamentais da Programação Orientada a Objetos (POO) conforme especificado no diagrama UML fornecido. 

## 📐 Diagrama UML
O diagrama UML abaixo representa a estrutura do sistema de mecânica, destacando todas as classes, seus atributos, métodos e relacionamentos definidos no projeto. 

Ele serve como uma visão geral da arquitetura orientada a objetos, que permite compreender:
- As principais entidades do sistema
- As relações entre classes (herança, composição, associação)
- O fluxo da aplicação baseado em objetos. 


![Diagrama UML](images/diagrama.jpeg)
(Para melhor visualização, acessar a pasta images e acessar o pdf do diagrama)

## 📁 Estrutura do Projeto

```
POO_Mecanica/
├── models/              # Classes do modelo (domínio)
│   ├── Cliente.py          # Classe Cliente
│   ├── Funcionario.py      # Classes Funcionario, Mecanico e Atendente
│   ├── OrdemServico.py     # Classe OrdemServico
│   ├── Peca.py             # Classe Peca
│   └── Veiculo.py          # Classe Veiculo
├── gui/                 # Interface gráfica (Tkinter)
│   ├── __init__.py         # Inicialização do pacote
│   ├── login_window.py     # Tela de login
│   ├── cliente_window.py   # Interface do cliente
│   ├── mecanico_window.py  # Interface do mecânico
│   └── atendente_window.py # Interface do atendente
├── images/              # Recursos visuais
│   └── diagrama.jpeg       # Diagrama UML do sistema
├── app.py               # Ponto de entrada da aplicação (GUI)
├── sistema.py           # Classe central de gerenciamento
├── main.py              # Demonstração em console (deprecated)
├── regras.py            # Testes unitários e de integração
└── README.md            # Documentação do projeto
```

## 🔧 Conceitos de POO Implementados

### 1. **Herança e Abstração**
- **Classe abstrata**: `Funcionario` (usando `abc.ABC`)
- **Herança**: `Mecanico` e `Atendente` herdam de `Funcionario`
- **Método abstrato**: `calcular_salario()` com `@abstractmethod`

```python
class Funcionario(ABC):
    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Mecanico(Funcionario):
    def calcular_salario(self) -> float:
        return self._salario_base + (self._qtd_veiculos_atendidos * self._bonus_por_veiculo)
```

### 2. **Polimorfismo**
- Implementação específica de `calcular_salario()` em cada classe filha
- Comportamentos distintos para mecânicos (bônus por veículo) e atendentes (comissão por cliente)

### 3. **Encapsulamento**
- **Atributos privados**: Uso de `_` para indicar atributos protegidos
- **Properties**: Uso do decorador `@property` para controle de acesso
- **Validações**: Setters com validação de dados

```python
@property
def nome(self) -> str:
    return self._nome

@nome.setter
def nome(self, valor: str):
    if not valor or not isinstance(valor, str):
        raise ValueError("Nome deve ser uma string não vazia")
    self._nome = valor
```

### 4. **Relacionamentos**
- **Agregação**: Cliente possui Veículos (cliente pode existir sem veículos)
- **Composição**: OrdemServico contém Peças (peças fazem parte da OS)
- **Associação**: OrdemServico se relaciona com Cliente, Mecanico e Veiculo


## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- Tkinter (geralmente já incluído no Python)

### Execução

1. **Interface Gráfica (recomendado)**:
```bash
python app.py
```

2. **Demonstração em console**:
```bash
python main.py
```

3. **Executar testes**:
```bash
python regras.py
```

## 🖥️ Interface Gráfica

O sistema possui uma interface gráfica completa desenvolvida com **Tkinter**, a biblioteca padrão do Python para criação de GUIs.

### Características da Interface

- **Design Moderno**: Interface com visual clean e profissional
- **Tela Cheia**: Todas as janelas abrem maximizadas
- **Código de Cores**: Cada tipo de usuário tem sua cor característica
  - 🔵 **Cliente**: Azul (#4A90E2)
  - 🟠 **Mecânico**: Laranja (#E67E22)
  - 🟣 **Atendente**: Roxo (#8E44AD)
- **Navegação por Abas**: Sistema de tabs customizado para cada interface
- **Contadores Dinâmicos**: Estatísticas atualizadas em tempo real

### Estrutura da Interface

#### 1. Tela de Login (`login_window.py`)
- Seleção do tipo de usuário (Cliente, Mecânico ou Atendente)
- Login por nome (case-insensitive)
- Design com card centralizado

#### 2. Interface do Cliente (`cliente_window.py`)
Funcionalidades disponíveis:
- **Solicitar Serviço**: Criar nova ordem de serviço
- **Aprovar Orçamento**: Aprovar orçamentos pendentes
- **Consultar Status**: Acompanhar andamento dos serviços

#### 3. Interface do Mecânico (`mecanico_window.py`)
Funcionalidades disponíveis:
- **Ordens de Serviço**: Visualizar OS atribuídas
- **Alterar Status**: Atualizar status das OS (Orçamento → Aprovado → Em Andamento → Concluído)
- **Requisitar Peças**: Solicitar peças do estoque

#### 4. Interface do Atendente (`atendente_window.py`)
Funcionalidades CRUD completas:
- **Clientes**: Criar, editar, visualizar e remover clientes
- **Veículos**: Gerenciar veículos dos clientes
- **Peças**: Controlar estoque de peças
- **Ordens de Serviço**: Criar e gerenciar OS

### Guia Rápido de Uso

#### Como Acessar o Sistema

1. Execute `python app.py`
2. Selecione o tipo de usuário
3. Digite o nome do usuário (use os dados de exemplo abaixo)

#### Credenciais de Exemplo

Após executar `app.py`, o sistema carrega automaticamente dados de exemplo:

**Clientes**:
- Ana Maria Costa
- Pedro Henrique Lima
- Mariana Fernandes

**Mecânicos**:
- Roberto Silva
- Carlos Oliveira

**Atendente**:
- Juliana Santos

#### Fluxo Típico de Uso

1. **Atendente** cria um novo cliente e cadastra seu veículo
2. **Atendente** cria uma ordem de serviço e atribui a um mecânico
3. **Mecânico** visualiza a OS, cria orçamento e altera status para "Orçamento"
4. **Cliente** aprova o orçamento
5. **Mecânico** executa o serviço, requisita peças e finaliza (status "Concluído")
6. **Cliente** consulta o status e avalia o serviço

## ⚙️ Funcionalidades

### Gestão de Funcionários
- Cadastro de mecânicos e atendentes
- Cálculo automático de salários com bônus/comissões

### Gestão de Clientes e Veículos
- Cadastro de clientes com validações
- Associação de múltiplos veículos por cliente
- Controle de satisfação do cliente

### Controle de Estoque
- Cadastro de peças com validações
- Controle de entrada e saída
- Alertas de estoque baixo

### Ordens de Serviço
- Criação e acompanhamento de OS
- Atribuição de mecânicos
- Cálculo automático de valores
- Controle de status (Aberto → Em Andamento → Concluído)

## 💻 Exemplos de Uso

### Criando Funcionários
```python
# Mecânico com bônus por veículo
mecanico = Mecanico("João Silva", 1, 3000.00, 0, 150.00)

# Atendente com comissão por cliente
atendente = Atendente("Ana Costa", 2, 2500.00, 50.00, 0)
```

### Criando Ordem de Serviço
```python
# Criar OS
os = sistema.criar_ordem_servico(
    cliente.id_cliente, 
    veiculo.placa, 
    "Troca de óleo e filtros"
)
```

## 🧪 Testes

O sistema inclui uma bateria completa de testes:

### Testes Automatizados
- Testes unitários para todas as classes
- Validação de herança e polimorfismo
- Testes de encapsulamento e properties
- Validação de regras de negócio

### Testes Manuais de Integração
- Fluxo completo de atendimento
- Validações de negócio
- Cálculos e relatórios

### Executar Testes
```bash
python regras.py
```

## 🏗️ Arquitetura

### Camadas da Aplicação

1. **Modelos (`models/`)**
   - Definição das classes principais separadas em diferentes arquivos
   - Regras básicas de validação
   - Relacionamentos entre entidades
   - Lógica de negócio (cálculos, validações)

2. **Sistema (`sistema.py`)**
   - Classe central `SistemaMecanica`
   - Gerenciamento de dados (clientes, funcionários, peças, OS)
   - Autenticação de usuários
   - Carregamento de dados de exemplo

3. **Interface Gráfica (`gui/`)**
   - Camada de apresentação com Tkinter
   - Janelas específicas para cada tipo de usuário
   - Controle de navegação e interação
   - Atualização dinâmica de contadores

4. **Aplicação (`app.py`)**
   - Ponto de entrada do sistema
   - Inicialização da interface gráfica
   - Configuração inicial

5. **Apresentação Console (`main.py`)**
   - Interface do usuário em console (deprecated)
   - Demonstrações do sistema
   - Fluxos de uso

6. **Testes (`regras.py`)**
   - Validação de funcionalidades
   - Testes de integração
   - Cenários de erro

## 📊 Demonstrações

O sistema oferece duas formas de demonstração:

### 1. Interface Gráfica (`app.py`)
Demonstração completa e interativa com:
- Login visual por tipo de usuário
- Interfaces personalizadas para cada perfil
- Operações CRUD completas
- Navegação intuitiva por abas
- Contadores e estatísticas em tempo real

### 2. Console (`main.py`)
Demonstrações programáticas de:
1. **Herança e Polimorfismo**: Cálculo diferenciado de salários
2. **Encapsulamento**: Validações com properties
3. **Agregação e Composição**: Relacionamentos entre objetos
4. **Sistema Completo**: Fluxo end-to-end

## ✅ Regras de Negócio

### Funcionários
- Nome não pode ser vazio
- ID deve ser único e positivo
- Salário base deve ser positivo
- Validação de tipos de dados

### Clientes
- Não é permitido nome vazio
- Satisfação deve estar na lista de valores válidos

### Veículos
- Placa com formato válido (mínimo 7 caracteres)
- Ano de fabricação entre 1900 e ano atual + 1
- Nome do veículo obrigatório

### Peças
- Valor unitário positivo
- Quantidade em estoque não negativa
- Nome obrigatório

### Ordens de Serviço
- Status deve estar na lista válida
- Cliente e veículo devem existir
- Mecânico deve ser do tipo correto

## 🎉 Resultados

### Execução da Demonstração
- ✅ Sistema executa sem erros
- ✅ Todas as funcionalidades principais demonstradas corretamente
- ✅ Cálculos corretos (folha, orçamentos, etc.)
- ✅ Relatórios gerados com sucesso
- ✅ Interações entre classes funcionando de acordo com o diagrama UML

### Testes
- ✅ **Testes automatizados aprovados**
- ✅ **Testes manuais concluídos com sucesso**
- ✅ **Validação das regras de negócio e comportamentos esperados**

## 📝 Conclusão

Este projeto demonstra a aplicação completa e integrada dos principais pilares da Programação Orientada a Objetos (POO) em Python, seguindo fielmente o diagrama UML do sistema:

- **Herança**: Reutilização de código através da hierarquia Funcionario
- **Polimorfismo**: Comportamentos específicos em métodos comuns
- **Abstração**: Classes abstratas definindo contratos
- **Encapsulamento**: Dados protegidos através de atributos privados e validações robustas
- **Relacionamentos**: Agregação, composição e associação implementadas
- **Modularidade**: Código organizado em módulos separados, facilitando manutenção e expansão
- **Validações**: Regras de negócio bem definidas asseguram integridade e confiabilidade dos dados
- **Testes**: Conjunto completo de testes garantindo estabilidade e funcionamento correto do sistema
- **Interface Gráfica**: GUI moderna e intuitiva desenvolvida com Tkinter, proporcionando experiência de usuário profissional

O sistema está pronto para uso e expansão, seguindo as melhores práticas de desenvolvimento orientado a objetos e oferecendo tanto interface gráfica quanto programática.

## 🫂 Desenvolvedores
- **André Luiz Vicenzi Rigo**
- **Kauan Lucas Toldo**
- **William Kunzler**
- **Yasmin Maria Zerbielli**