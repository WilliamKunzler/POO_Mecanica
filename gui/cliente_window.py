import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date


class ClienteWindow:
    """Interface para Cliente - Abrir chamados, aprovar orçamentos, consultar OS."""
    
    def __init__(self, root, sistema, cliente, login_root):
        self.root = root
        self.sistema = sistema
        self.cliente = cliente
        self.login_root = login_root
        
        self.root.title(f"Sistema de Mecânica - Cliente: {cliente.nome}")
        self.root.state('zoomed')
        self.root.configure(bg="#F5F7FA")
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.criar_widgets()
    
    def criar_widgets(self):
        """Cria os widgets da interface do cliente."""
        # Header azul
        header = tk.Frame(self.root, bg="#4A90E2", height=70)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        
        # Info do cliente no header
        info_frame = tk.Frame(header, bg="#4A90E2")
        info_frame.pack(side="left", padx=25, pady=15)
        
        tk.Label(
            info_frame,
            text=f"👤 Cliente: {self.cliente.nome}",
            font=("Segoe UI", 13, "bold"),
            bg="#4A90E2",
            fg="white"
        ).pack(anchor="w")
        
        self.info_label = tk.Label(
            info_frame,
            text=f"ID: {self.cliente.id_cliente} | Serviços: {self.cliente.qtd_servicos} | Não avaliado",
            font=("Segoe UI", 9),
            bg="#4A90E2",
            fg="white"
        )
        self.info_label.pack(anchor="w")
        
        # Botão Sair
        btn_sair = tk.Button(
            header,
            text="Sair",
            command=self.on_closing,
            font=("Segoe UI", 10),
            bg="#E74C3C",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8,
            activebackground="#C0392B",
            activeforeground="white"
        )
        btn_sair.pack(side="right", padx=25, pady=15)
        
        # Container principal com abas
        container = tk.Frame(self.root, bg="#F5F7FA")
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Frame para as abas customizadas
        tabs_frame = tk.Frame(container, bg="#F5F7FA")
        tabs_frame.pack(fill="x", pady=(0, 20))
        
        # Criar abas customizadas
        self.current_tab = "abrir_chamado"
        self.tab_buttons = {}
        
        tabs = [
            ("📝 Abrir Chamado", "abrir_chamado"),
            ("✅ Aprovar Orçamentos", "aprovar_orcamentos"),
            ("📋 Minhas OS", "minhas_os")
        ]
        
        for i, (text, tab_id) in enumerate(tabs):
            btn = tk.Button(
                tabs_frame,
                text=text,
                command=lambda t=tab_id: self.switch_tab(t),
                font=("Segoe UI", 11),
                bg="white" if i == 0 else "#E8EAF0",
                fg="#4A90E2" if i == 0 else "#6C757D",
                relief="flat",
                cursor="hand2",
                padx=20,
                pady=10,
                activebackground="white",
                activeforeground="#4A90E2",
                borderwidth=0,
                highlightthickness=0
            )
            btn.pack(side="left", padx=5)
            self.tab_buttons[tab_id] = btn
        
        # Container de conteúdo
        self.content_frame = tk.Frame(container, bg="#F5F7FA")
        self.content_frame.pack(fill="both", expand=True)
        
        # Mostrar primeira aba
        self.switch_tab("abrir_chamado")
    
    def atualizar_header(self):
        """Atualiza as informações do header com contadores dinâmicos."""
        qtd_servicos = self.cliente.calcular_servicos_ativos(self.sistema.ordens_servico)
        self.info_label.config(text=f"ID: {self.cliente.id_cliente} | Serviços: {qtd_servicos} | {self.cliente.satisfacao}")
    
    def switch_tab(self, tab_id):
        """Troca entre as abas."""
        # Atualizar header ao trocar de aba
        self.atualizar_header()
        
        self.current_tab = tab_id
        
        # Atualizar estilo dos botões
        for tid, btn in self.tab_buttons.items():
            if tid == tab_id:
                btn.configure(bg="white", fg="#4A90E2", font=("Segoe UI", 11, "bold"))
            else:
                btn.configure(bg="#E8EAF0", fg="#6C757D", font=("Segoe UI", 11))
        
        # Limpar conteúdo atual
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Mostrar conteúdo da aba selecionada
        if tab_id == "abrir_chamado":
            self.aba_abrir_chamado()
        elif tab_id == "aprovar_orcamentos":
            self.aba_aprovar_orcamento()
        elif tab_id == "minhas_os":
            self.aba_consultar_os()
    
    def aba_abrir_chamado(self):
        """Cria a aba para abrir novos chamados."""
        # Card branco
        card = tk.Frame(self.content_frame, bg="white", relief="flat")
        card.pack(fill="both", expand=True, padx=10, pady=10)
        card.configure(highlightbackground="#E0E0E0", highlightthickness=1)
        
        # Padding interno
        inner = tk.Frame(card, bg="white")
        inner.pack(fill="both", expand=True, padx=40, pady=30)
        
        # Título
        tk.Label(
            inner,
            text="Abrir Novo Chamado",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#2C3E50"
        ).pack(anchor="w", pady=(0, 25))
        
        # Selecionar veículo
        tk.Label(
            inner,
            text="Selecione o Veículo:",
            font=("Segoe UI", 10),
            bg="white",
            fg="#495057"
        ).pack(anchor="w", pady=(0, 8))
        
        self.veiculo_var = tk.StringVar()
        veiculos = self.cliente.veiculos
        
        if veiculos:
            opcoes_veiculos = [f"{v.placa} - {v.nome_veiculo} {v.modelo}" for v in veiculos]
            
            # Frame do combobox
            combo_frame = tk.Frame(inner, bg="white", relief="solid", bd=1)
            combo_frame.pack(fill="x", pady=(0, 25))
            
            self.veiculo_combo = ttk.Combobox(
                combo_frame,
                textvariable=self.veiculo_var,
                values=opcoes_veiculos,
                state="readonly",
                font=("Segoe UI", 10)
            )
            self.veiculo_combo.pack(fill="x", padx=10, pady=10)
            if opcoes_veiculos:
                self.veiculo_combo.current(0)
        else:
            alert_frame = tk.Frame(inner, bg="#FFF3CD", relief="solid", bd=1)
            alert_frame.pack(fill="x", pady=(0, 25))
            tk.Label(
                alert_frame,
                text="⚠️ Nenhum veículo cadastrado. Contate o atendente.",
                font=("Segoe UI", 10),
                bg="#FFF3CD",
                fg="#856404"
            ).pack(padx=15, pady=10)
        
        # Descrição do problema
        tk.Label(
            inner,
            text="Descrição do Problema:",
            font=("Segoe UI", 10),
            bg="white",
            fg="#495057"
        ).pack(anchor="w", pady=(0, 8))
        
        # Frame do textarea
        text_frame = tk.Frame(inner, bg="white", relief="solid", bd=1)
        text_frame.pack(fill="both", expand=True, pady=(0, 25))
        
        self.descricao_text = tk.Text(
            text_frame,
            height=8,
            font=("Segoe UI", 10),
            relief="flat",
            bd=0,
            wrap="word",
            bg="white",
            fg="#495057"
        )
        self.descricao_text.pack(fill="both", expand=True, padx=12, pady=12)
        self.descricao_text.insert("1.0", "Descreva o problema com o máximo de detalhes possível...")
        self.descricao_text.bind("<FocusIn>", self.on_descricao_focus_in)
        self.descricao_text.bind("<FocusOut>", self.on_descricao_focus_out)
        self.descricao_text.configure(fg="#ADB5BD")
        
        # Botão Abrir Chamado
        btn_frame = tk.Frame(inner, bg="white")
        btn_frame.pack(fill="x")
        
        tk.Button(
            btn_frame,
            text="▶  Abrir Chamado",
            command=self.abrir_chamado,
            font=("Segoe UI", 11, "bold"),
            bg="#28A745",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=12,
            activebackground="#218838",
            activeforeground="white"
        ).pack(side="right")
    
    def on_descricao_focus_in(self, event):
        """Remove placeholder quando ganha foco."""
        if self.descricao_text.get("1.0", "end-1c") == "Descreva o problema com o máximo de detalhes possível...":
            self.descricao_text.delete("1.0", "end")
            self.descricao_text.configure(fg="#495057")
    
    def on_descricao_focus_out(self, event):
        """Adiciona placeholder quando perde foco."""
        if not self.descricao_text.get("1.0", "end-1c").strip():
            self.descricao_text.insert("1.0", "Descreva o problema com o máximo de detalhes possível...")
            self.descricao_text.configure(fg="#ADB5BD")
    
    def aba_aprovar_orcamento(self):
        """Cria a aba para aprovar orçamentos."""
        # Card branco
        card = tk.Frame(self.content_frame, bg="white", relief="flat")
        card.pack(fill="both", expand=True, padx=10, pady=10)
        card.configure(highlightbackground="#E0E0E0", highlightthickness=1)
        
        inner = tk.Frame(card, bg="white")
        inner.pack(fill="both", expand=True, padx=40, pady=30)
        
        # Título
        tk.Label(
            inner,
            text="Orçamentos Pendentes de Aprovação",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#2C3E50"
        ).pack(anchor="w", pady=(0, 25))
        
        # Frame da lista
        lista_frame = tk.Frame(inner, bg="white", relief="solid", bd=1)
        lista_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Scrollbar
        scrollbar = tk.Scrollbar(lista_frame)
        scrollbar.pack(side="right", fill="y")
        
        # Listbox
        self.orcamentos_listbox = tk.Listbox(
            lista_frame,
            font=("Segoe UI", 10),
            yscrollcommand=scrollbar.set,
            selectmode="single",
            bg="white",
            fg="#495057",
            relief="flat",
            bd=0,
            highlightthickness=0,
            selectbackground="#E8F5E9",
            selectforeground="#2E7D32"
        )
        self.orcamentos_listbox.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar.config(command=self.orcamentos_listbox.yview)
        
        # Botões
        btn_frame = tk.Frame(inner, bg="white")
        btn_frame.pack(fill="x")
        
        tk.Button(
            btn_frame,
            text="🔄  Atualizar Lista",
            command=self.atualizar_orcamentos,
            font=("Segoe UI", 10),
            bg="#6C757D",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            activebackground="#5A6268"
        ).pack(side="left")
        
        tk.Button(
            btn_frame,
            text="✅  Aprovar Orçamento",
            command=self.aprovar_orcamento,
            font=("Segoe UI", 11, "bold"),
            bg="#28A745",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=12,
            activebackground="#218838"
        ).pack(side="right")
        
        self.atualizar_orcamentos()
    
    def aba_consultar_os(self):
        """Cria a aba para consultar ordens de serviço."""
        # Card branco
        card = tk.Frame(self.content_frame, bg="white", relief="flat")
        card.pack(fill="both", expand=True, padx=10, pady=10)
        card.configure(highlightbackground="#E0E0E0", highlightthickness=1)
        
        inner = tk.Frame(card, bg="white")
        inner.pack(fill="both", expand=True, padx=40, pady=30)
        
        # Título
        tk.Label(
            inner,
            text="Minhas Ordens de Serviço",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#2C3E50"
        ).pack(anchor="w", pady=(0, 25))
        
        # Frame da tabela
        table_frame = tk.Frame(inner, bg="white", relief="solid", bd=1)
        table_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Scrollbars
        scrollbar_y = tk.Scrollbar(table_frame)
        scrollbar_y.pack(side="right", fill="y")
        
        scrollbar_x = tk.Scrollbar(table_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")
        
        # Treeview com estilo
        columns = ("ID", "Data", "Status", "Veículo", "Descrição", "Valor")
        self.os_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            height=15
        )
        
        scrollbar_y.config(command=self.os_tree.yview)
        scrollbar_x.config(command=self.os_tree.xview)
        
        # Configurar colunas
        self.os_tree.heading("ID", text="ID")
        self.os_tree.heading("Data", text="Data Abertura")
        self.os_tree.heading("Status", text="Status")
        self.os_tree.heading("Veículo", text="Veículo")
        self.os_tree.heading("Descrição", text="Descrição")
        self.os_tree.heading("Valor", text="Valor Total")
        
        self.os_tree.column("ID", width=60, anchor="center")
        self.os_tree.column("Data", width=110, anchor="center")
        self.os_tree.column("Status", width=130, anchor="center")
        self.os_tree.column("Veículo", width=180)
        self.os_tree.column("Descrição", width=280)
        self.os_tree.column("Valor", width=110, anchor="center")
        
        self.os_tree.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Botão atualizar
        btn_frame = tk.Frame(inner, bg="white")
        btn_frame.pack(fill="x")
        
        tk.Button(
            btn_frame,
            text="🔄  Atualizar Lista",
            command=self.atualizar_os,
            font=("Segoe UI", 10),
            bg="#6C757D",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10,
            activebackground="#5A6268"
        ).pack(side="left")
        
        self.atualizar_os()
    
    def abrir_chamado(self):
        """Abre um novo chamado de serviço."""
        veiculos = self.cliente.veiculos
        
        if not veiculos:
            messagebox.showerror("Erro", "Você não possui veículos cadastrados.")
            return
        
        veiculo_selecionado = self.veiculo_combo.current()
        if veiculo_selecionado < 0:
            messagebox.showwarning("Atenção", "Selecione um veículo.")
            return
        
        veiculo = veiculos[veiculo_selecionado]
        descricao = self.descricao_text.get("1.0", "end-1c").strip()
        
        if not descricao or descricao == "Descreva o problema com o máximo de detalhes possível...":
            messagebox.showwarning("Atenção", "Descreva o problema do veículo.")
            return
        
        # Criar ordem de serviço
        nova_os = self.cliente.abrir_chamado(veiculo, descricao)
        self.sistema.ordens_servico.append(nova_os)
        
        messagebox.showinfo(
            "Sucesso",
            f"Chamado #{nova_os.id_os} aberto com sucesso!\n\n"
            f"Veículo: {veiculo.nome_veiculo}\n"
            f"Status: {nova_os.status}"
        )
        
        # Limpar campos
        self.descricao_text.delete("1.0", "end")
        self.descricao_text.insert("1.0", "Descreva o problema com o máximo de detalhes possível...")
        self.descricao_text.configure(fg="#ADB5BD")
    
    def atualizar_orcamentos(self):
        """Atualiza a lista de orçamentos pendentes."""
        self.orcamentos_listbox.delete(0, "end")
        
        # Buscar OS com status "Orçamento" do cliente
        orcamentos_pendentes = self.cliente.consultar_os(self.sistema.ordens_servico)
        orcamentos_pendentes = [os for os in orcamentos_pendentes if os.status == "Orçamento"]
        
        if not orcamentos_pendentes:
            self.orcamentos_listbox.insert("end", "  Nenhum orçamento pendente de aprovação.")
        else:
            for os in orcamentos_pendentes:
                veiculo_info = f"{os.veiculo.nome_veiculo} ({os.veiculo.placa})" if os.veiculo else "N/A"
                texto = f"OS #{os.id_os} | {veiculo_info} | R$ {os.valor_total:.2f} | {os.descricao[:50]}"
                self.orcamentos_listbox.insert("end", texto)
    
    def aprovar_orcamento(self):
        """Aprova o orçamento selecionado."""
        selecao = self.orcamentos_listbox.curselection()
        
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione um orçamento para aprovar.")
            return
        
        # Buscar OS correspondente
        orcamentos_pendentes = self.cliente.consultar_os(self.sistema.ordens_servico)
        orcamentos_pendentes = [os for os in orcamentos_pendentes if os.status == "Orçamento"]
        
        if selecao[0] < len(orcamentos_pendentes):
            os_selecionada = orcamentos_pendentes[selecao[0]]
            
            # Aprovar orçamento
            self.cliente.aprovar_orcamento(os_selecionada)
            
            messagebox.showinfo(
                "Sucesso",
                f"Orçamento da OS #{os_selecionada.id_os} aprovado com sucesso!\n"
                f"Valor: R$ {os_selecionada.valor_total:.2f}"
            )
            
            # Atualizar lista
            self.atualizar_orcamentos()
    
    def atualizar_os(self):
        """Atualiza a lista de ordens de serviço do cliente."""
        # Limpar tree
        for item in self.os_tree.get_children():
            self.os_tree.delete(item)
        
        # Buscar todas as OS do cliente
        minhas_os = self.cliente.consultar_os(self.sistema.ordens_servico)
        
        if not minhas_os:
            self.os_tree.insert("", "end", values=("", "", "Nenhuma OS encontrada", "", "", ""))
        else:
            for os in minhas_os:
                veiculo_info = f"{os.veiculo.nome_veiculo} ({os.veiculo.placa})" if os.veiculo else "N/A"
                data_str = os.data_abertura.strftime("%d/%m/%Y") if os.data_abertura else "N/A"
                
                self.os_tree.insert(
                    "",
                    "end",
                    values=(
                        os.id_os,
                        data_str,
                        os.status,
                        veiculo_info,
                        os.descricao[:50],
                        f"R$ {os.valor_total:.2f}"
                    )
                )
    
    def on_closing(self):
        """Fecha a janela e volta ao login."""
        self.root.destroy()
        self.login_root.state('zoomed')
        self.login_root.deiconify()
