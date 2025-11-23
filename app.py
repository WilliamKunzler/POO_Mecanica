"""
Sistema de Mecânica - Interface Gráfica com Tkinter
Aplicação principal que inicia o sistema.
"""

import tkinter as tk
from gui.login_window import LoginWindow
from sistema import SistemaMecanica


def main():
    """Função principal para iniciar o sistema."""
    # Criar janela principal
    root = tk.Tk()
    
    # Criar instância do sistema
    sistema = SistemaMecanica()
    
    # Carregar dados de exemplo
    print("="*60)
    print("    SISTEMA DE GERENCIAMENTO DE MECÂNICA")
    print("="*60)
    sistema.carregar_dados_exemplo()
    print("="*60)
    print("\n🚀 Iniciando interface gráfica...")
    
    # Criar tela de login
    LoginWindow(root, sistema)
    
    # Iniciar loop principal
    root.mainloop()


if __name__ == "__main__":
    main()
