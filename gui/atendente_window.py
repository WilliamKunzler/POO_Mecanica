import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from services.cliente_service import ClienteService
from services.veiculo_service import VeiculoService
from services.peca_service import PecaService
from services.estoque_service import EstoqueService
from services.ordem_servico_service import OrdemServicoService


class AtendenteWindow:
    """Interface para Atendente - CRUD completo de Clientes, Veículos, Peças e OS."""
    
    def __init__(self, root, sistema, atendente, login_root):
        self.root = root
        self.sistema = sistema
        self.atendente = atendente
        self.login_root = login_root
        self.cliente_service = ClienteService()
        self.veiculo_service = VeiculoService()
        self.peca_service = PecaService()
        self.estoque_service = EstoqueService()
        self.ordem_servico_service = OrdemServicoService()
        
        self.root.title(f"Sistema de Mecânica - Atendente: {atendente.nome}")
        self.root.state('zoomed')
        self.root.configure(bg="#F5F7FA")
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.criar_widgets()
    
    def criar_widgets(self):
        """Cria todos os widgets da interface com design moderno."""
        
        # HEADER ROXO
        header = tk.Frame(self.root, bg="#8E44AD", height=80)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        
        # Container do header
        header_content = tk.Frame(header, bg="#8E44AD")
        header_content.pack(expand=True, fill="both", padx=30)
        
        # Info do atendente
        info_frame = tk.Frame(header_content, bg="#8E44AD")
        info_frame.pack(side="left", fill="y")
        
        tk.Label(info_frame, text=f"Atendente: {self.atendente.nome}", 
                font=("Segoe UI", 16, "bold"), bg="#8E44AD", fg="white").pack(anchor="w")
        salario = self.atendente.calcular_salario()
        self.info_label = tk.Label(info_frame, text=f"ID {self.atendente.id} | Clientes Atendidos: {self.atendente.qtd_clientes} | Salário: R$ {salario:,.2f}", 
                font=("Segoe UI", 10), bg="#8E44AD", fg="white")
        self.info_label.pack(anchor="w")
        
        # Botão sair
        btn_sair = tk.Button(header_content, text="Sair", font=("Segoe UI", 11),
                            bg="white", fg="#8E44AD", relief="flat", cursor="hand2",
                            padx=20, pady=8, command=self.on_closing)
        btn_sair.pack(side="right", pady=20)
        
        # ÁREA DE TABS CUSTOMIZADAS
        tabs_frame = tk.Frame(self.root, bg="#F5F7FA", height=60)
        tabs_frame.pack(fill="x", padx=30, pady=(20, 0))
        tabs_frame.pack_propagate(False)
        
        self.tab_buttons = {}
        tabs = [
            ("Clientes", "clientes"),
            ("Veículos", "veiculos"),
            ("Peças", "pecas"),
            ("Ordens de Serviço", "os")
        ]
        
        for text, tab_id in tabs:
            btn = tk.Button(tabs_frame, text=text, font=("Segoe UI", 11),
                          bg="white", fg="#666666", relief="flat", cursor="hand2",
                          padx=25, pady=12, borderwidth=0,
                          command=lambda t=tab_id: self.switch_tab(t))
            btn.pack(side="left", padx=(0, 5))
            self.tab_buttons[tab_id] = btn
        
        # ÁREA DE CONTEÚDO
        self.content_frame = tk.Frame(self.root, bg="#F5F7FA")
        self.content_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        # Criar todas as abas
        self.tabs = {}
        self.tabs["clientes"] = self.aba_crud_clientes()
        self.tabs["veiculos"] = self.aba_crud_veiculos()
        self.tabs["pecas"] = self.aba_crud_pecas()
        self.tabs["os"] = self.aba_crud_os()
        
        # Mostrar primeira aba
        self.switch_tab("clientes")
    
    def atualizar_header(self):
        """Atualiza as informações do header com contadores dinâmicos."""
        qtd_clientes = self.atendente.calcular_clientes_atendidos(self.sistema.clientes)
        salario = self.atendente.calcular_salario()
        self.info_label.config(text=f"ID {self.atendente.id} | Clientes Atendidos: {qtd_clientes} | Salário: R$ {salario:,.2f}")
    
    def switch_tab(self, tab_id):
        """Alterna entre as abas."""
        # Atualizar header ao trocar de aba
        self.atualizar_header()
        
        for tab in self.tabs.values():
            tab.pack_forget()
        
        for btn in self.tab_buttons.values():
            btn.config(bg="white", fg="#666666")
        
        self.tabs[tab_id].pack(fill="both", expand=True)
        self.tab_buttons[tab_id].config(bg="#8E44AD", fg="white")
    
    # ==================== CRUD CLIENTES ====================
    
    def aba_crud_clientes(self):
        """Aba para CRUD de Clientes."""
        frame = tk.Frame(self.content_frame, bg="#F5F7FA")
        
        # Card principal
        card = tk.Frame(frame, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Header do card com título e botões
        header_card = tk.Frame(card, bg="white")
        header_card.pack(fill="x", padx=20, pady=20)
        
        tk.Label(header_card, text="Gerenciamento de Clientes", 
                font=("Segoe UI", 14, "bold"), bg="white", fg="#333333").pack(side="left")
        
        # Botões à direita
        btn_container = tk.Frame(header_card, bg="white")
        btn_container.pack(side="right")
        
        tk.Button(btn_container, text="Atualizar", command=self.atualizar_clientes,
                 font=("Segoe UI", 9), bg="#6C757D", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Remover Cliente", command=self.remover_cliente,
                 font=("Segoe UI", 9), bg="#DC3545", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Editar Cliente", command=self.editar_cliente,
                 font=("Segoe UI", 9), bg="#4A90E2", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Criar Cliente", command=self.criar_cliente,
                 font=("Segoe UI", 9), bg="#28A745", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        # Frame para Treeview
        tree_frame = tk.Frame(card, bg="white")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        columns = ("ID", "Nome", "Qtd Serviços", "Satisfação", "Veículos")
        self.clientes_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=15
        )
        
        scrollbar.config(command=self.clientes_tree.yview)
        
        self.clientes_tree.heading("ID", text="ID")
        self.clientes_tree.heading("Nome", text="NOME")
        self.clientes_tree.heading("Qtd Serviços", text="QTD SERVIÇOS")
        self.clientes_tree.heading("Satisfação", text="SATISFAÇÃO")
        self.clientes_tree.heading("Veículos", text="VEÍCULOS")
        
        self.clientes_tree.column("ID", width=80, anchor="center")
        self.clientes_tree.column("Nome", width=250)
        self.clientes_tree.column("Qtd Serviços", width=120, anchor="center")
        self.clientes_tree.column("Satisfação", width=150, anchor="center")
        self.clientes_tree.column("Veículos", width=100, anchor="center")
        
        self.clientes_tree.pack(fill="both", expand=True)
        
        self.atualizar_clientes()
        return frame
    
    def criar_cliente(self):
        """Cria um novo cliente."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Criar Novo Cliente")
        dialog.geometry("400x300")
        dialog.configure(bg="#F5F7FA")
        dialog.transient(self.root)
        dialog.grab_set()
        
        card = tk.Frame(dialog, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(card, text="Nome:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(20, 5), padx=20, anchor="w")
        nome_entry = tk.Entry(card, font=("Segoe UI", 10), width=40, relief="solid", borderwidth=1)
        nome_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Satisfação:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        satisfacao_var = tk.StringVar(value="Não avaliado")
        satisfacao_combo = ttk.Combobox(
            card,
            textvariable=satisfacao_var,
            values=["Muito Satisfeito", "Satisfeito", "Neutro", "Insatisfeito", "Não avaliado"],
            state="readonly",
            font=("Segoe UI", 10)
        )
        satisfacao_combo.pack(pady=(0, 20), padx=20, fill="x")
        
        def salvar():
            nome = nome_entry.get().strip()
            if not nome:
                messagebox.showerror("Erro", "Nome é obrigatório.")
                return
            
            novo_cliente = self.cliente_service.criar(
                nome=nome,
                satisfacao=satisfacao_var.get(),
                atendente=self.atendente,
            )
            self.sistema.clientes.append(novo_cliente)
            messagebox.showinfo("Sucesso", f"Cliente {nome} criado com sucesso!\nID: {novo_cliente.id_cliente}")
            dialog.destroy()
            self.atualizar_clientes()
        
        tk.Button(card, text="Salvar", command=salvar, font=("Segoe UI", 10),
                 bg="#28A745", fg="white", relief="flat", cursor="hand2",
                 padx=30, pady=10).pack(pady=(0, 20))
    
    def editar_cliente(self):
        """Edita um cliente selecionado."""
        selecao = self.clientes_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione um cliente.")
            return
        
        item = self.clientes_tree.item(selecao[0])
        cliente_id = item['values'][0]
        cliente = next((c for c in self.sistema.clientes if c.id_cliente == cliente_id), None)
        
        if not cliente:
            messagebox.showerror("Erro", "Cliente não encontrado.")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Editar Cliente - ID {cliente_id}")
        dialog.geometry("400x300")
        dialog.configure(bg="#F5F7FA")
        dialog.transient(self.root)
        dialog.grab_set()
        
        card = tk.Frame(dialog, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(card, text="Nome:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(20, 5), padx=20, anchor="w")
        nome_entry = tk.Entry(card, font=("Segoe UI", 10), width=40, relief="solid", borderwidth=1)
        nome_entry.insert(0, cliente.nome)
        nome_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Satisfação:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        satisfacao_var = tk.StringVar(value=cliente.satisfacao)
        satisfacao_combo = ttk.Combobox(
            card,
            textvariable=satisfacao_var,
            values=["Muito Satisfeito", "Satisfeito", "Neutro", "Insatisfeito", "Não avaliado"],
            state="readonly",
            font=("Segoe UI", 10)
        )
        satisfacao_combo.pack(pady=(0, 20), padx=20, fill="x")
        
        def salvar():
            nome = nome_entry.get().strip()
            if not nome:
                messagebox.showerror("Erro", "Nome é obrigatório.")
                return
            
            self.cliente_service.editar(cliente, nome=nome, satisfacao=satisfacao_var.get())
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            dialog.destroy()
            self.atualizar_clientes()
        
        tk.Button(card, text="Salvar", command=salvar, font=("Segoe UI", 10),
                 bg="#4A90E2", fg="white", relief="flat", cursor="hand2",
                 padx=30, pady=10).pack(pady=(0, 20))
    
    def remover_cliente(self):
        """Remove um cliente selecionado."""
        selecao = self.clientes_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione um cliente.")
            return
        
        item = self.clientes_tree.item(selecao[0])
        cliente_id = item['values'][0]
        cliente = next((c for c in self.sistema.clientes if c.id_cliente == cliente_id), None)
        
        if not cliente:
            return
        
        confirmar = messagebox.askyesno("Confirmar Remoção", f"Deseja realmente remover o cliente {cliente.nome}?")
        
        if confirmar:
            self.cliente_service.remover(cliente, self.sistema.clientes, atendente=self.atendente)
            messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
            self.atualizar_clientes()
    
    def atualizar_clientes(self):
        """Atualiza a lista de clientes."""
        for item in self.clientes_tree.get_children():
            self.clientes_tree.delete(item)
        
        for cliente in self.sistema.clientes:
            self.clientes_tree.insert("", "end", values=(
                cliente.id_cliente,
                cliente.nome,
                cliente.qtd_servicos,
                cliente.satisfacao,
                len(cliente.veiculos)
            ))
    
    # ==================== CRUD VEÍCULOS ====================
    
    def aba_crud_veiculos(self):
        """Aba para CRUD de Veículos."""
        frame = tk.Frame(self.content_frame, bg="#F5F7FA")
        
        card = tk.Frame(frame, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=5, pady=5)
        
        header_card = tk.Frame(card, bg="white")
        header_card.pack(fill="x", padx=20, pady=20)
        
        tk.Label(header_card, text="Gerenciamento de Veículos", 
                font=("Segoe UI", 14, "bold"), bg="white", fg="#333333").pack(side="left")
        
        btn_container = tk.Frame(header_card, bg="white")
        btn_container.pack(side="right")
        
        tk.Button(btn_container, text="Atualizar", command=self.atualizar_veiculos,
                 font=("Segoe UI", 9), bg="#6C757D", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Remover Veículo", command=self.remover_veiculo,
                 font=("Segoe UI", 9), bg="#DC3545", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Editar Veículo", command=self.editar_veiculo,
                 font=("Segoe UI", 9), bg="#4A90E2", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Criar Veículo", command=self.criar_veiculo,
                 font=("Segoe UI", 9), bg="#28A745", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tree_frame = tk.Frame(card, bg="white")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        columns = ("Placa", "Nome", "Modelo", "Ano", "Cliente", "Idade")
        self.veiculos_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=15
        )
        
        scrollbar.config(command=self.veiculos_tree.yview)
        
        self.veiculos_tree.heading("Placa", text="PLACA")
        self.veiculos_tree.heading("Nome", text="NOME")
        self.veiculos_tree.heading("Modelo", text="MODELO")
        self.veiculos_tree.heading("Ano", text="ANO")
        self.veiculos_tree.heading("Cliente", text="CLIENTE")
        self.veiculos_tree.heading("Idade", text="IDADE")
        
        self.veiculos_tree.column("Placa", width=100, anchor="center")
        self.veiculos_tree.column("Nome", width=180)
        self.veiculos_tree.column("Modelo", width=180)
        self.veiculos_tree.column("Ano", width=80, anchor="center")
        self.veiculos_tree.column("Cliente", width=200)
        self.veiculos_tree.column("Idade", width=80, anchor="center")
        
        self.veiculos_tree.pack(fill="both", expand=True)
        
        self.atualizar_veiculos()
        return frame
    
    def criar_veiculo(self):
        """Cria um novo veículo."""
        if not self.sistema.clientes:
            messagebox.showerror("Erro", "Crie um cliente primeiro.")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Criar Novo Veículo")
        dialog.geometry("450x500")
        dialog.configure(bg="#F5F7FA")
        dialog.transient(self.root)
        dialog.grab_set()
        
        card = tk.Frame(dialog, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(card, text="Cliente:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(20, 5), padx=20, anchor="w")
        cliente_var = tk.StringVar()
        cliente_combo = ttk.Combobox(
            card,
            textvariable=cliente_var,
            values=[f"ID {c.id_cliente} - {c.nome}" for c in self.sistema.clientes],
            state="readonly",
            font=("Segoe UI", 10)
        )
        cliente_combo.pack(pady=(0, 15), padx=20, fill="x")
        if self.sistema.clientes:
            cliente_combo.current(0)
        
        tk.Label(card, text="Placa:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        placa_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        placa_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Nome do Veículo:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        nome_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        nome_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Modelo:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        modelo_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        modelo_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Ano de Fabricação:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        ano_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        ano_entry.pack(pady=(0, 20), padx=20, fill="x")
        
        def salvar():
            try:
                cliente_idx = cliente_combo.current()
                cliente = self.sistema.clientes[cliente_idx]
                
                placa = placa_entry.get().strip()
                nome = nome_entry.get().strip()
                modelo = modelo_entry.get().strip()
                ano = int(ano_entry.get().strip())
                
                if not all([placa, nome, modelo]):
                    raise ValueError("Preencha todos os campos.")
                
                novo_veiculo = self.veiculo_service.criar(
                    placa=placa,
                    nome_veiculo=nome,
                    modelo=modelo,
                    ano_fabricacao=ano,
                    cliente=cliente
                )
                
                messagebox.showinfo("Sucesso", f"Veículo {nome} criado com sucesso!")
                dialog.destroy()
                self.atualizar_veiculos()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao criar veículo: {str(e)}")
        
        tk.Button(card, text="Salvar", command=salvar, font=("Segoe UI", 10),
                 bg="#28A745", fg="white", relief="flat", cursor="hand2",
                 padx=30, pady=10).pack(pady=(0, 20))
    
    def editar_veiculo(self):
        """Edita um veículo selecionado."""
        selecao = self.veiculos_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione um veículo.")
            return
        
        item = self.veiculos_tree.item(selecao[0])
        placa = item['values'][0]
        
        veiculo = None
        for cliente in self.sistema.clientes:
            for v in cliente.veiculos:
                if v.placa == placa:
                    veiculo = v
                    break
        
        if not veiculo:
            messagebox.showerror("Erro", "Veículo não encontrado.")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Editar Veículo - {placa}")
        dialog.geometry("400x300")
        dialog.configure(bg="#F5F7FA")
        dialog.transient(self.root)
        dialog.grab_set()
        
        card = tk.Frame(dialog, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(card, text="Nome do Veículo:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(20, 5), padx=20, anchor="w")
        nome_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        nome_entry.insert(0, veiculo.nome_veiculo)
        nome_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Modelo:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        modelo_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        modelo_entry.insert(0, veiculo.modelo)
        modelo_entry.pack(pady=(0, 20), padx=20, fill="x")
        
        def salvar():
            nome = nome_entry.get().strip()
            modelo = modelo_entry.get().strip()
            
            if nome or modelo:
                self.veiculo_service.editar(veiculo, nome_veiculo=nome, modelo=modelo)
                messagebox.showinfo("Sucesso", "Veículo atualizado com sucesso!")
                dialog.destroy()
                self.atualizar_veiculos()
        
        tk.Button(card, text="Salvar", command=salvar, font=("Segoe UI", 10),
                 bg="#4A90E2", fg="white", relief="flat", cursor="hand2",
                 padx=30, pady=10).pack(pady=(0, 20))
    
    def remover_veiculo(self):
        """Remove um veículo selecionado."""
        selecao = self.veiculos_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione um veículo.")
            return
        
        item = self.veiculos_tree.item(selecao[0])
        placa = item['values'][0]
        
        veiculo = None
        cliente_dono = None
        for cliente in self.sistema.clientes:
            for v in cliente.veiculos:
                if v.placa == placa:
                    veiculo = v
                    cliente_dono = cliente
                    break
        
        if not veiculo or not cliente_dono:
            return
        
        confirmar = messagebox.askyesno("Confirmar Remoção", f"Deseja realmente remover o veículo {veiculo.nome_veiculo} ({placa})?")
        
        if confirmar:
            self.veiculo_service.remover(veiculo, cliente_dono)
            messagebox.showinfo("Sucesso", "Veículo removido com sucesso!")
            self.atualizar_veiculos()
    
    def atualizar_veiculos(self):
        """Atualiza a lista de veículos."""
        for item in self.veiculos_tree.get_children():
            self.veiculos_tree.delete(item)
        
        for cliente in self.sistema.clientes:
            for veiculo in cliente.veiculos:
                self.veiculos_tree.insert("", "end", values=(
                    veiculo.placa,
                    veiculo.nome_veiculo,
                    veiculo.modelo,
                    veiculo.ano_fabricacao,
                    cliente.nome,
                    f"{veiculo.calcular_idade()} anos"
                ))
    
    # ==================== CRUD PEÇAS ====================
    
    def aba_crud_pecas(self):
        """Aba para CRUD de Peças."""
        frame = tk.Frame(self.content_frame, bg="#F5F7FA")
        
        card = tk.Frame(frame, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=5, pady=5)
        
        header_card = tk.Frame(card, bg="white")
        header_card.pack(fill="x", padx=20, pady=20)
        
        tk.Label(header_card, text="Gerenciamento de Peças", 
                font=("Segoe UI", 14, "bold"), bg="white", fg="#333333").pack(side="left")
        
        btn_container = tk.Frame(header_card, bg="white")
        btn_container.pack(side="right")
        
        tk.Button(btn_container, text="Atualizar", command=self.atualizar_pecas,
                 font=("Segoe UI", 9), bg="#6C757D", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Adicionar Estoque", command=self.adicionar_estoque,
                 font=("Segoe UI", 9), bg="#FFC107", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Editar Peça", command=self.editar_peca,
                 font=("Segoe UI", 9), bg="#4A90E2", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Criar Peça", command=self.criar_peca,
                 font=("Segoe UI", 9), bg="#28A745", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tree_frame = tk.Frame(card, bg="white")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        columns = ("ID", "Nome", "Descrição", "Estoque", "Valor Unit.", "Valor Total")
        self.pecas_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=15
        )
        
        scrollbar.config(command=self.pecas_tree.yview)
        
        self.pecas_tree.heading("ID", text="ID")
        self.pecas_tree.heading("Nome", text="NOME")
        self.pecas_tree.heading("Descrição", text="DESCRIÇÃO")
        self.pecas_tree.heading("Estoque", text="QTD ESTOQUE")
        self.pecas_tree.heading("Valor Unit.", text="VALOR UNIT.")
        self.pecas_tree.heading("Valor Total", text="VALOR TOTAL")
        
        self.pecas_tree.column("ID", width=60, anchor="center")
        self.pecas_tree.column("Nome", width=180)
        self.pecas_tree.column("Descrição", width=280)
        self.pecas_tree.column("Estoque", width=100, anchor="center")
        self.pecas_tree.column("Valor Unit.", width=100, anchor="center")
        self.pecas_tree.column("Valor Total", width=120, anchor="center")
        
        self.pecas_tree.pack(fill="both", expand=True)
        
        self.atualizar_pecas()
        return frame
    
    def criar_peca(self):
        """Cria uma nova peça."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Criar Nova Peça")
        dialog.geometry("450x450")
        dialog.configure(bg="#F5F7FA")
        dialog.transient(self.root)
        dialog.grab_set()
        
        card = tk.Frame(dialog, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(card, text="Nome:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(20, 5), padx=20, anchor="w")
        nome_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        nome_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Descrição:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        desc_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        desc_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Quantidade em Estoque:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        qtd_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        qtd_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Valor Unitário (R$):", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        valor_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        valor_entry.pack(pady=(0, 20), padx=20, fill="x")
        
        def salvar():
            try:
                nome = nome_entry.get().strip()
                desc = desc_entry.get().strip()
                qtd = int(qtd_entry.get().strip())
                valor = float(valor_entry.get().strip())
                
                if not nome:
                    raise ValueError("Nome é obrigatório.")
                
                nova_peca = self.peca_service.criar(nome=nome, descricao=desc, qtd_estoque=qtd, valor_unit=valor)
                self.sistema.pecas.append(nova_peca)
                
                messagebox.showinfo("Sucesso", f"Peça {nome} criada com sucesso!\nID: {nova_peca.id}")
                dialog.destroy()
                self.atualizar_pecas()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao criar peça: {str(e)}")
        
        tk.Button(card, text="Salvar", command=salvar, font=("Segoe UI", 10),
                 bg="#28A745", fg="white", relief="flat", cursor="hand2",
                 padx=30, pady=10).pack(pady=(0, 20))
    
    def editar_peca(self):
        """Edita uma peça selecionada."""
        selecao = self.pecas_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma peça.")
            return
        
        item = self.pecas_tree.item(selecao[0])
        peca_id = item['values'][0]
        peca = next((p for p in self.sistema.pecas if p.id == peca_id), None)
        
        if not peca:
            messagebox.showerror("Erro", "Peça não encontrada.")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Editar Peça - ID {peca_id}")
        dialog.geometry("400x350")
        dialog.configure(bg="#F5F7FA")
        dialog.transient(self.root)
        dialog.grab_set()
        
        card = tk.Frame(dialog, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(card, text="Nome:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(20, 5), padx=20, anchor="w")
        nome_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        nome_entry.insert(0, peca.nome)
        nome_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Descrição:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        desc_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        desc_entry.insert(0, peca.descricao)
        desc_entry.pack(pady=(0, 15), padx=20, fill="x")
        
        tk.Label(card, text="Valor Unitário (R$):", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        valor_entry = tk.Entry(card, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        valor_entry.insert(0, str(peca.valor_unit))
        valor_entry.pack(pady=(0, 20), padx=20, fill="x")
        
        def salvar():
            try:
                nome = nome_entry.get().strip()
                desc = desc_entry.get().strip()
                valor = float(valor_entry.get().strip())
                
                self.peca_service.editar(peca, nome=nome, descricao=desc, valor_unit=valor)
                messagebox.showinfo("Sucesso", "Peça atualizada com sucesso!")
                dialog.destroy()
                self.atualizar_pecas()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao editar peça: {str(e)}")
        
        tk.Button(card, text="Salvar", command=salvar, font=("Segoe UI", 10),
                 bg="#4A90E2", fg="white", relief="flat", cursor="hand2",
                 padx=30, pady=10).pack(pady=(0, 20))
    
    def adicionar_estoque(self):
        """Adiciona estoque a uma peça."""
        selecao = self.pecas_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma peça.")
            return
        
        item = self.pecas_tree.item(selecao[0])
        peca_id = item['values'][0]
        peca = next((p for p in self.sistema.pecas if p.id == peca_id), None)
        
        if not peca:
            return
        
        qtd = simpledialog.askinteger("Adicionar Estoque", f"Quantidade a adicionar para {peca.nome}:", minvalue=1)
        
        if qtd:
            self.estoque_service.adicionar_estoque(peca, qtd)
            messagebox.showinfo("Sucesso", f"{qtd} unidade(s) adicionada(s) ao estoque!")
            self.atualizar_pecas()
    
    def atualizar_pecas(self):
        """Atualiza a lista de peças."""
        for item in self.pecas_tree.get_children():
            self.pecas_tree.delete(item)
        
        for peca in self.sistema.pecas:
            valor_total = peca.qtd_estoque * peca.valor_unit
            self.pecas_tree.insert("", "end", values=(
                peca.id,
                peca.nome,
                peca.descricao,
                peca.qtd_estoque,
                f"R$ {peca.valor_unit:.2f}",
                f"R$ {valor_total:.2f}"
            ))
    
    # ==================== CRUD ORDENS DE SERVIÇO ====================
    
    def aba_crud_os(self):
        """Aba para CRUD de Ordens de Serviço."""
        frame = tk.Frame(self.content_frame, bg="#F5F7FA")
        
        card = tk.Frame(frame, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=5, pady=5)
        
        header_card = tk.Frame(card, bg="white")
        header_card.pack(fill="x", padx=20, pady=20)
        
        tk.Label(header_card, text="Gerenciamento de Ordens de Serviço", 
                font=("Segoe UI", 14, "bold"), bg="white", fg="#333333").pack(side="left")
        
        btn_container = tk.Frame(header_card, bg="white")
        btn_container.pack(side="right")
        
        tk.Button(btn_container, text="Atualizar", command=self.atualizar_os,
                 font=("Segoe UI", 9), bg="#6C757D", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Gerar Orçamento", command=self.gerar_orcamento,
                 font=("Segoe UI", 9), bg="#8E44AD", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Atribuir Mecânico", command=self.atribuir_mecanico,
                 font=("Segoe UI", 9), bg="#E67E22", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tk.Button(btn_container, text="Criar OS", command=self.criar_os,
                 font=("Segoe UI", 9), bg="#28A745", fg="white", relief="flat",
                 cursor="hand2", padx=15, pady=8).pack(side="left", padx=2)
        
        tree_frame = tk.Frame(card, bg="white")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        scrollbar_y = tk.Scrollbar(tree_frame)
        scrollbar_y.pack(side="right", fill="y")
        
        scrollbar_x = tk.Scrollbar(tree_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")
        
        columns = ("ID", "Data", "Cliente", "Veículo", "Mecânico", "Status", "Valor", "Descrição")
        self.os_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            height=15
        )
        
        scrollbar_y.config(command=self.os_tree.yview)
        scrollbar_x.config(command=self.os_tree.xview)
        
        self.os_tree.heading("ID", text="ID")
        self.os_tree.heading("Data", text="DATA")
        self.os_tree.heading("Cliente", text="CLIENTE")
        self.os_tree.heading("Veículo", text="VEÍCULO")
        self.os_tree.heading("Mecânico", text="MECÂNICO")
        self.os_tree.heading("Status", text="STATUS")
        self.os_tree.heading("Valor", text="VALOR")
        self.os_tree.heading("Descrição", text="DESCRIÇÃO")
        
        self.os_tree.column("ID", width=50, anchor="center")
        self.os_tree.column("Data", width=100, anchor="center")
        self.os_tree.column("Cliente", width=150)
        self.os_tree.column("Veículo", width=150)
        self.os_tree.column("Mecânico", width=120)
        self.os_tree.column("Status", width=120, anchor="center")
        self.os_tree.column("Valor", width=100, anchor="center")
        self.os_tree.column("Descrição", width=200)
        
        self.os_tree.pack(fill="both", expand=True)
        
        self.atualizar_os()
        return frame
    
    def criar_os(self):
        """Cria uma nova ordem de serviço."""
        if not self.sistema.clientes:
            messagebox.showerror("Erro", "Crie um cliente primeiro.")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Criar Nova Ordem de Serviço")
        dialog.geometry("500x450")
        dialog.configure(bg="#F5F7FA")
        dialog.transient(self.root)
        dialog.grab_set()
        
        card = tk.Frame(dialog, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(card, text="Cliente:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(20, 5), padx=20, anchor="w")
        cliente_var = tk.StringVar()
        cliente_combo = ttk.Combobox(
            card,
            textvariable=cliente_var,
            values=[f"ID {c.id_cliente} - {c.nome}" for c in self.sistema.clientes],
            state="readonly",
            font=("Segoe UI", 10)
        )
        cliente_combo.pack(pady=(0, 15), padx=20, fill="x")
        if self.sistema.clientes:
            cliente_combo.current(0)
        
        tk.Label(card, text="Veículo:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        veiculo_var = tk.StringVar()
        veiculo_combo = ttk.Combobox(
            card,
            textvariable=veiculo_var,
            state="readonly",
            font=("Segoe UI", 10)
        )
        veiculo_combo.pack(pady=(0, 15), padx=20, fill="x")
        
        def atualizar_veiculos_combo(event=None):
            idx = cliente_combo.current()
            if idx >= 0:
                cliente = self.sistema.clientes[idx]
                veiculos = cliente.veiculos
                veiculo_combo['values'] = [f"{v.placa} - {v.nome_veiculo}" for v in veiculos]
                if veiculos:
                    veiculo_combo.current(0)
        
        cliente_combo.bind("<<ComboboxSelected>>", atualizar_veiculos_combo)
        atualizar_veiculos_combo()
        
        tk.Label(card, text="Descrição:", font=("Segoe UI", 10, "bold"), bg="white", fg="#333333").pack(pady=(10, 5), padx=20, anchor="w")
        desc_text = tk.Text(card, height=6, font=("Segoe UI", 10), relief="solid", borderwidth=1)
        desc_text.pack(pady=(0, 20), padx=20, fill="both")
        
        def salvar():
            try:
                cliente_idx = cliente_combo.current()
                veiculo_idx = veiculo_combo.current()
                
                if cliente_idx < 0 or veiculo_idx < 0:
                    raise ValueError("Selecione cliente e veículo.")
                
                cliente = self.sistema.clientes[cliente_idx]
                veiculo = cliente.veiculos[veiculo_idx]
                descricao = desc_text.get("1.0", "end-1c").strip()
                
                if not descricao:
                    raise ValueError("Descrição é obrigatória.")
                
                nova_os = self.ordem_servico_service.criar(cliente, veiculo, descricao)
                self.sistema.ordens_servico.append(nova_os)
                
                messagebox.showinfo("Sucesso", f"OS #{nova_os.id_os} criada com sucesso!")
                dialog.destroy()
                self.atualizar_os()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao criar OS: {str(e)}")
        
        tk.Button(card, text="Salvar", command=salvar, font=("Segoe UI", 10),
                 bg="#28A745", fg="white", relief="flat", cursor="hand2",
                 padx=30, pady=10).pack(pady=(0, 20))
    
    def atribuir_mecanico(self):
        """Atribui um mecânico a uma OS."""
        selecao = self.os_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma OS.")
            return
        
        if not self.sistema.mecanicos:
            messagebox.showerror("Erro", "Não há mecânicos cadastrados.")
            return
        
        item = self.os_tree.item(selecao[0])
        os_id = item['values'][0]
        os_obj = next((os for os in self.sistema.ordens_servico if os.id_os == os_id), None)
        
        if not os_obj:
            return
        
        mecanico_nome = simpledialog.askstring(
            "Atribuir Mecânico",
            f"Mecânicos disponíveis:\n" + "\n".join([f"ID {m.id} - {m.nome}" for m in self.sistema.mecanicos]) +
            "\n\nDigite o ID do mecânico:"
        )
        
        if mecanico_nome:
            try:
                mec_id = int(mecanico_nome)
                mecanico = next((m for m in self.sistema.mecanicos if m.id == mec_id), None)
                
                if mecanico:
                    self.ordem_servico_service.atribuir_mecanico(os_obj, mecanico)
                    messagebox.showinfo("Sucesso", f"Mecânico {mecanico.nome} atribuído à OS #{os_id}")
                    self.atualizar_os()
                else:
                    messagebox.showerror("Erro", "Mecânico não encontrado.")
            except:
                messagebox.showerror("Erro", "ID inválido.")
    
    def gerar_orcamento(self):
        """Gera orçamento para uma OS."""
        selecao = self.os_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma OS.")
            return
        
        item = self.os_tree.item(selecao[0])
        os_id = item['values'][0]
        os_obj = next((os for os in self.sistema.ordens_servico if os.id_os == os_id), None)
        
        if os_obj:
            os_obj.alterar_status("Orçamento")
            valor = self.ordem_servico_service.gerar_orcamento(os_obj)
            messagebox.showinfo("Orçamento Gerado", f"Orçamento da OS #{os_id}:\nR$ {valor:.2f}")
            self.atualizar_os()
    
    def atualizar_os(self):
        """Atualiza a lista de ordens de serviço."""
        for item in self.os_tree.get_children():
            self.os_tree.delete(item)
        
        for os in self.sistema.ordens_servico:
            cliente_nome = os.cliente.nome if os.cliente else "N/A"
            veiculo_info = f"{os.veiculo.nome_veiculo} ({os.veiculo.placa})" if os.veiculo else "N/A"
            mecanico_nome = os.mecanico.nome if os.mecanico else "Não atribuído"
            data_str = os.data_abertura.strftime("%d/%m/%Y") if os.data_abertura else "N/A"
            
            self.os_tree.insert("", "end", values=(
                os.id_os,
                data_str,
                cliente_nome,
                veiculo_info,
                mecanico_nome,
                os.status,
                f"R$ {os.valor_total:.2f}",
                os.descricao[:50]
            ))
    
    def on_closing(self):
        """Fecha a janela e volta ao login."""
        self.root.destroy()
        self.login_root.state('zoomed')
        self.login_root.deiconify()
