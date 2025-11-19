from datetime import date

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