import tkinter as tk
from tkinter import messagebox, ttk
from gui.cliente_window import ClienteWindow
from gui.mecanico_window import MecanicoWindow
from gui.atendente_window import AtendenteWindow
from repositories.interfaces import UsuarioRepository


class LoginWindow:
    """Tela de Login para o Sistema de Mecânica."""
    
    def __init__(self, root, usuario_repo: UsuarioRepository):
        self.root = root
        self.usuario_repo = usuario_repo
        self.sistema = usuario_repo
        self.root.title("Sistema de Mecânica - Login")
        self.root.state('zoomed')
        self.root.configure(bg="#2C3E50")
        
        self.criar_widgets()
    
    def criar_widgets(self):
        """Cria os widgets da tela de login."""
        # Background
        self.root.configure(bg="#E8EAF0")
        
        # Frame principal centralizado
        main_frame = tk.Frame(self.root, bg="#E8EAF0")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="🔧 SISTEMA DE MECÂNICA",
            font=("Segoe UI", 32, "bold"),
            bg="#E8EAF0",
            fg="#2C3E50"
        )
        titulo.pack(pady=(0, 5))
        
        # Subtítulo
        subtitulo = tk.Label(
            main_frame,
            text="Gestão Completa de Oficina",
            font=("Segoe UI", 11),
            bg="#E8EAF0",
            fg="#6C757D"
        )
        subtitulo.pack(pady=(0, 40))
        
        # Card branco de login
        login_card = tk.Frame(main_frame, bg="white", relief="flat", bd=0)
        login_card.pack(padx=40, pady=20)
        
        # Adicionar sombra simulada com bordas
        login_card.configure(highlightbackground="#D0D3DD", highlightthickness=1)
        
        # Conteúdo do card
        card_content = tk.Frame(login_card, bg="white")
        card_content.pack(padx=50, pady=40)
        
        # Label "Selecione o tipo de usuário:"
        tk.Label(
            card_content,
            text="Selecione o tipo de usuário:",
            font=("Segoe UI", 10),
            bg="white",
            fg="#495057"
        ).pack(anchor="w", pady=(0, 15))
        
        # Frame para os botões de tipo de usuário
        self.tipo_usuario = tk.StringVar(value="Cliente")
        
        tipos_frame = tk.Frame(card_content, bg="white")
        tipos_frame.pack(fill="x", pady=(0, 25))
        
        # Botões estilo card para cada tipo
        tipos = [
            ("👤", "Cliente", "Cliente"),
            ("🔧", "Mecânico", "Mecânico"),
            ("📋", "Atendente", "Atendente")
        ]
        
        for i, (icone, texto, valor) in enumerate(tipos):
            btn_frame = tk.Frame(tipos_frame, bg="white")
            btn_frame.pack(side="left", padx=5)
            
            # Criar botão customizado
            btn = tk.Button(
                btn_frame,
                text=f"{icone}  {texto}",
                command=lambda v=valor: self.selecionar_tipo(v),
                font=("Segoe UI", 10),
                bg="white",
                fg="#495057",
                relief="solid",
                bd=1,
                padx=20,
                pady=12,
                cursor="hand2",
                activebackground="#E8F5E9",
                activeforeground="#2E7D32"
            )
            btn.pack()
            
            # Armazenar referência aos botões
            if not hasattr(self, 'tipo_buttons'):
                self.tipo_buttons = {}
            self.tipo_buttons[valor] = btn
        
        # Selecionar Cliente por padrão
        self.selecionar_tipo("Cliente")
        
        # Label "Nome do Usuário:"
        tk.Label(
            card_content,
            text="Nome do Usuário:",
            font=("Segoe UI", 10),
            bg="white",
            fg="#495057"
        ).pack(anchor="w", pady=(0, 8))
        
        # Frame para o input com ícone
        input_frame = tk.Frame(card_content, bg="white", relief="solid", bd=1)
        input_frame.pack(fill="x", pady=(0, 25))
        
        # Ícone no input
        tk.Label(
            input_frame,
            text="👤",
            font=("Segoe UI", 12),
            bg="white",
            fg="#6C757D"
        ).pack(side="left", padx=(10, 5))
        
        # Entry field
        self.nome_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            relief="flat",
            bd=0,
            bg="white",
            fg="#495057"
        )
        self.nome_entry.pack(side="left", fill="x", expand=True, padx=(5, 10), pady=10)
        self.nome_entry.insert(0, "Digite seu nome")
        self.nome_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.nome_entry.bind("<FocusOut>", self.on_entry_focus_out)
        self.nome_entry.configure(fg="#ADB5BD")
        
        # Botão ENTRAR
        btn_entrar = tk.Button(
            card_content,
            text="➜  ENTRAR",
            command=self.fazer_login,
            font=("Segoe UI", 11, "bold"),
            bg="#28A745",
            fg="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            activebackground="#218838",
            activeforeground="white",
            padx=30,
            pady=12
        )
        btn_entrar.pack(fill="x")
        
        # Rodapé
        rodape = tk.Label(
            main_frame,
            text="Sistema desenvolvido com Python & Tkinter",
            font=("Segoe UI", 9),
            bg="#E8EAF0",
            fg="#ADB5BD"
        )
        rodape.pack(pady=(30, 0))
    
    def selecionar_tipo(self, tipo):
        """Atualiza a seleção do tipo de usuário."""
        self.tipo_usuario.set(tipo)
        
        # Atualizar visual dos botões
        for valor, btn in self.tipo_buttons.items():
            if valor == tipo:
                btn.configure(
                    bg="#E8F5E9",
                    fg="#2E7D32",
                    relief="solid",
                    bd=2
                )
            else:
                btn.configure(
                    bg="white",
                    fg="#495057",
                    relief="solid",
                    bd=1
                )
    
    def on_entry_focus_in(self, event):
        """Remove placeholder quando o campo recebe foco."""
        if self.nome_entry.get() == "Digite seu nome":
            self.nome_entry.delete(0, "end")
            self.nome_entry.configure(fg="#495057")
    
    def on_entry_focus_out(self, event):
        """Adiciona placeholder quando o campo perde foco."""
        if not self.nome_entry.get():
            self.nome_entry.insert(0, "Digite seu nome")
            self.nome_entry.configure(fg="#ADB5BD")
    
    def fazer_login(self):
        """Processa o login do usuário."""
        tipo = self.tipo_usuario.get()
        nome_usuario = self.nome_entry.get().strip()
        
        # Verificar se não é o placeholder
        if not nome_usuario or nome_usuario == "Digite seu nome":
            messagebox.showwarning("Atenção", "Por favor, informe o nome do usuário.")
            return
        
        # Verificar se o usuário existe no sistema
        usuario = self.usuario_repo.buscar_usuario(tipo, nome_usuario)
        
        if usuario:
            messagebox.showinfo("Sucesso", f"Bem-vindo(a), {usuario.nome}!")
            self.abrir_interface(tipo, usuario)
        else:
            messagebox.showerror(
                "Erro de Login",
                f"{tipo} '{nome_usuario}' não encontrado no sistema."
            )
    
    def abrir_interface(self, tipo, usuario):
        """Abre a interface apropriada baseada no tipo de usuário."""
        # Ocultar janela de login
        self.root.withdraw()
        
        # Criar nova janela
        nova_janela = tk.Toplevel(self.root)
        
        if tipo == "Cliente":
            ClienteWindow(nova_janela, self.sistema, usuario, self.root)
        elif tipo == "Mecânico":
            MecanicoWindow(nova_janela, self.sistema, usuario, self.root)
        elif tipo == "Atendente":
            AtendenteWindow(nova_janela, self.sistema, usuario, self.root)
