import tkinter as tk
from tkinter import messagebox, ttk, simpledialog


class MecanicoWindow:
    """Interface para Mecânico - Alterar status, requisitar peças, fechar OS."""
    
    def __init__(self, root, sistema, mecanico, login_root):
        self.root = root
        self.sistema = sistema
        self.mecanico = mecanico
        self.login_root = login_root
        
        self.root.title(f"Sistema de Mecânica - Mecânico: {mecanico.nome}")
        self.root.state('zoomed')
        self.root.configure(bg="#F5F7FA")
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.criar_widgets()
    
    def criar_widgets(self):
        """Cria todos os widgets da interface com design moderno."""
        
        # HEADER
        header = tk.Frame(self.root, bg="#E67E22", height=80)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        
        # Container do header
        header_content = tk.Frame(header, bg="#E67E22")
        header_content.pack(expand=True, fill="both", padx=30)
        
        # Info do mecânico
        info_frame = tk.Frame(header_content, bg="#E67E22")
        info_frame.pack(side="left", fill="y")
        
        tk.Label(info_frame, text=f"Mecânico: {self.mecanico.nome}", 
                font=("Segoe UI", 16, "bold"), bg="#E67E22", fg="white").pack(anchor="w")
        salario = self.mecanico.calcular_salario()
        self.info_label = tk.Label(info_frame, text=f"ID: {self.mecanico.id} | Veículos Atendidos: {self.mecanico.qtd_veiculos_atendidos} | Salário: R$ {salario:,.2f}", 
                font=("Segoe UI", 10), bg="#E67E22", fg="white")
        self.info_label.pack(anchor="w")
        
        # Botão sair
        btn_sair = tk.Button(header_content, text="Sair", font=("Segoe UI", 11),
                            bg="white", fg="#E67E22", relief="flat", cursor="hand2",
                            padx=20, pady=8, command=self.on_closing)
        btn_sair.pack(side="right", pady=20)
        
        # ÁREA DE TABS CUSTOMIZADAS
        tabs_frame = tk.Frame(self.root, bg="#F5F7FA", height=60)
        tabs_frame.pack(fill="x", padx=30, pady=(20, 0))
        tabs_frame.pack_propagate(False)
        
        self.tab_buttons = {}
        tabs = [
            ("Minhas OS", "minhas_os"),
            ("Requisitar Peças", "requisitar_pecas"),
            ("Estoque", "estoque")
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
        self.tabs["minhas_os"] = self.aba_minhas_os()
        self.tabs["requisitar_pecas"] = self.aba_requisitar_pecas()
        self.tabs["estoque"] = self.aba_estoque()
        
        # Mostrar primeira aba
        self.switch_tab("minhas_os")
    
    def atualizar_header(self):
        """Atualiza as informações do header com contadores dinâmicos."""
        qtd_veiculos = self.mecanico.calcular_veiculos_atendidos(self.sistema.ordens_servico)
        salario = self.mecanico.calcular_salario()
        self.info_label.config(text=f"ID: {self.mecanico.id} | Veículos Atendidos: {qtd_veiculos} | Salário: R$ {salario:,.2f}")
    
    def switch_tab(self, tab_id):
        """Alterna entre as abas."""
        # Atualizar header ao trocar de aba
        self.atualizar_header()
        
        # Esconder todas as abas
        for tab in self.tabs.values():
            tab.pack_forget()
        
        # Resetar estilo de todos os botões
        for btn in self.tab_buttons.values():
            btn.config(bg="white", fg="#666666")
        
        # Mostrar aba selecionada
        self.tabs[tab_id].pack(fill="both", expand=True)
        
        # Destacar botão ativo
        self.tab_buttons[tab_id].config(bg="#E67E22", fg="white")
    
    def aba_minhas_os(self):
        """Aba para visualizar e alterar status das OS."""
        frame = tk.Frame(self.content_frame, bg="#F5F7FA")
        
        # Card principal
        card = tk.Frame(frame, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Título
        tk.Label(card, text="Ordens de Serviço Atribuídas", 
                font=("Segoe UI", 14, "bold"), bg="white", fg="#333333").pack(pady=20, padx=20, anchor="w")
        
        # Frame para Treeview
        tree_frame = tk.Frame(card, bg="white")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Scrollbars
        scrollbar_y = tk.Scrollbar(tree_frame)
        scrollbar_y.pack(side="right", fill="y")
        
        scrollbar_x = tk.Scrollbar(tree_frame, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")
        
        # Treeview
        columns = ("ID", "Cliente", "Veículo", "Status", "Descrição", "Valor", "Peças")
        self.os_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            height=12
        )
        
        scrollbar_y.config(command=self.os_tree.yview)
        scrollbar_x.config(command=self.os_tree.xview)
        
        # Configurar colunas
        self.os_tree.heading("ID", text="ID")
        self.os_tree.heading("Cliente", text="Cliente")
        self.os_tree.heading("Veículo", text="Veículo")
        self.os_tree.heading("Status", text="Status")
        self.os_tree.heading("Descrição", text="Descrição")
        self.os_tree.heading("Valor", text="Valor")
        self.os_tree.heading("Peças", text="Peças")
        
        self.os_tree.column("ID", width=50, anchor="center")
        self.os_tree.column("Cliente", width=150)
        self.os_tree.column("Veículo", width=150)
        self.os_tree.column("Status", width=120, anchor="center")
        self.os_tree.column("Descrição", width=200)
        self.os_tree.column("Valor", width=80, anchor="center")
        self.os_tree.column("Peças", width=80, anchor="center")
        
        self.os_tree.pack(fill="both", expand=True)
        
        # Frame de botões
        btn_frame = tk.Frame(card, bg="white")
        btn_frame.pack(pady=(0, 20))
        
        tk.Button(
            btn_frame,
            text="Alterar Status",
            command=self.alterar_status_os,
            font=("Segoe UI", 10),
            bg="#4A90E2",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        ).pack(side="left", padx=5)
        
        tk.Button(
            btn_frame,
            text="Concluir OS",
            command=self.concluir_os,
            font=("Segoe UI", 10),
            bg="#28A745",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        ).pack(side="left", padx=5)
        
        tk.Button(
            btn_frame,
            text="Atualizar",
            command=self.atualizar_minhas_os,
            font=("Segoe UI", 10),
            bg="#6C757D",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        ).pack(side="left", padx=5)
        
        self.atualizar_minhas_os()
        return frame
    
    def aba_requisitar_pecas(self):
        """Aba para requisitar peças do estoque."""
        frame = tk.Frame(self.content_frame, bg="#F5F7FA")
        
        # Card principal
        card = tk.Frame(frame, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Título
        tk.Label(card, text="Requisição de Peças", 
                font=("Segoe UI", 14, "bold"), bg="white", fg="#333333").pack(pady=20, padx=20, anchor="w")
        
        # Frame formulário
        form_frame = tk.Frame(card, bg="white")
        form_frame.pack(fill="both", expand=True, padx=40, pady=(0, 20))
        
        # Selecionar OS
        tk.Label(
            form_frame,
            text="Selecione a Ordem de Serviço:",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#333333"
        ).pack(anchor="w", pady=(10, 5))
        
        self.os_requisicao_var = tk.StringVar()
        self.os_requisicao_combo = ttk.Combobox(
            form_frame,
            textvariable=self.os_requisicao_var,
            state="readonly",
            font=("Segoe UI", 10),
            width=60
        )
        self.os_requisicao_combo.pack(fill="x", pady=(0, 15))
        
        # Selecionar peça
        tk.Label(
            form_frame,
            text="Selecione a Peça:",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#333333"
        ).pack(anchor="w", pady=(10, 5))
        
        self.peca_requisicao_var = tk.StringVar()
        self.peca_requisicao_combo = ttk.Combobox(
            form_frame,
            textvariable=self.peca_requisicao_var,
            state="readonly",
            font=("Segoe UI", 10),
            width=60
        )
        self.peca_requisicao_combo.pack(fill="x", pady=(0, 15))
        
        # Quantidade
        tk.Label(
            form_frame,
            text="Quantidade:",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#333333"
        ).pack(anchor="w", pady=(10, 5))
        
        self.qtd_requisicao_var = tk.StringVar(value="1")
        qtd_entry = tk.Entry(
            form_frame,
            textvariable=self.qtd_requisicao_var,
            font=("Segoe UI", 10),
            width=15,
            relief="solid",
            borderwidth=1
        )
        qtd_entry.pack(anchor="w", pady=(0, 20))
        
        # Botões
        btn_frame = tk.Frame(form_frame, bg="white")
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="Requisitar Peça",
            command=self.requisitar_peca,
            font=("Segoe UI", 10),
            bg="#E67E22",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=12
        ).pack(side="left", padx=5)
        
        tk.Button(
            btn_frame,
            text="Atualizar Listas",
            command=self.atualizar_combos_requisicao,
            font=("Segoe UI", 10),
            bg="#4A90E2",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=12
        ).pack(side="left", padx=5)
        
        self.atualizar_combos_requisicao()
        return frame
    
    def aba_estoque(self):
        """Aba para visualizar estoque de peças."""
        frame = tk.Frame(self.content_frame, bg="#F5F7FA")
        
        # Card principal
        card = tk.Frame(frame, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Título
        tk.Label(card, text="Estoque de Peças", 
                font=("Segoe UI", 14, "bold"), bg="white", fg="#333333").pack(pady=20, padx=20, anchor="w")
        
        # Frame para Treeview
        tree_frame = tk.Frame(card, bg="white")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        scrollbar = tk.Scrollbar(tree_frame)
        scrollbar.pack(side="right", fill="y")
        
        columns = ("ID", "Nome", "Descrição", "Estoque", "Valor Unit.", "Valor Total")
        self.estoque_tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            yscrollcommand=scrollbar.set,
            height=15
        )
        
        scrollbar.config(command=self.estoque_tree.yview)
        
        self.estoque_tree.heading("ID", text="ID")
        self.estoque_tree.heading("Nome", text="Nome")
        self.estoque_tree.heading("Descrição", text="Descrição")
        self.estoque_tree.heading("Estoque", text="Qtd. Estoque")
        self.estoque_tree.heading("Valor Unit.", text="Valor Unit.")
        self.estoque_tree.heading("Valor Total", text="Valor Total")
        
        self.estoque_tree.column("ID", width=50, anchor="center")
        self.estoque_tree.column("Nome", width=150)
        self.estoque_tree.column("Descrição", width=250)
        self.estoque_tree.column("Estoque", width=100, anchor="center")
        self.estoque_tree.column("Valor Unit.", width=100, anchor="center")
        self.estoque_tree.column("Valor Total", width=120, anchor="center")
        
        self.estoque_tree.pack(fill="both", expand=True)
        
        # Botão atualizar
        tk.Button(
            card,
            text="Atualizar Estoque",
            command=self.atualizar_estoque,
            font=("Segoe UI", 10),
            bg="#4A90E2",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=10
        ).pack(pady=(0, 20))
        
        self.atualizar_estoque()
        return frame
    
    def atualizar_minhas_os(self):
        """Atualiza a lista de OS do mecânico."""
        for item in self.os_tree.get_children():
            self.os_tree.delete(item)
        
        minhas_os = [os for os in self.sistema.ordens_servico if os.mecanico == self.mecanico]
        
        if not minhas_os:
            self.os_tree.insert("", "end", values=("", "", "", "Nenhuma OS atribuída", "", "", ""))
        else:
            for os in minhas_os:
                cliente_nome = os.cliente.nome if os.cliente else "N/A"
                veiculo_info = f"{os.veiculo.nome_veiculo} ({os.veiculo.placa})" if os.veiculo else "N/A"
                qtd_pecas = len(os.pecas)
                
                self.os_tree.insert(
                    "",
                    "end",
                    values=(
                        os.id_os,
                        cliente_nome,
                        veiculo_info,
                        os.status,
                        os.descricao[:40],
                        f"R$ {os.valor_total:.2f}",
                        qtd_pecas
                    )
                )
    
    def alterar_status_os(self):
        """Altera o status da OS selecionada."""
        selecao = self.os_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma OS.")
            return
        
        item = self.os_tree.item(selecao[0])
        os_id = item['values'][0]
        
        # Buscar OS
        os_obj = next((os for os in self.sistema.ordens_servico if os.id_os == os_id), None)
        if not os_obj:
            messagebox.showerror("Erro", "OS não encontrada.")
            return
        
        # Janela para selecionar novo status
        status_window = tk.Toplevel(self.root)
        status_window.title("Alterar Status")
        status_window.geometry("350x400")
        status_window.configure(bg="#F5F7FA")
        status_window.transient(self.root)
        status_window.grab_set()
        
        # Card
        card = tk.Frame(status_window, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(
            card,
            text=f"Alterar Status da OS #{os_id}",
            font=("Segoe UI", 13, "bold"),
            bg="white",
            fg="#333333"
        ).pack(pady=20)
        
        status_var = tk.StringVar(value=os_obj.status)
        status_opcoes = ["Aberto", "Orçamento", "Aprovado", "Em Andamento", "Concluído", "Cancelado"]
        
        for status in status_opcoes:
            tk.Radiobutton(
                card,
                text=status,
                variable=status_var,
                value=status,
                font=("Segoe UI", 10),
                bg="white"
            ).pack(anchor="w", padx=40, pady=5)
        
        def confirmar():
            novo_status = status_var.get()
            self.mecanico.alterar_status(os_obj, novo_status)
            messagebox.showinfo("Sucesso", f"Status alterado para: {novo_status}")
            status_window.destroy()
            self.atualizar_minhas_os()
        
        tk.Button(
            card,
            text="Confirmar",
            command=confirmar,
            font=("Segoe UI", 10),
            bg="#28A745",
            fg="white",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=10
        ).pack(pady=20)
    
    def concluir_os(self):
        """Conclui a OS selecionada."""
        selecao = self.os_tree.selection()
        if not selecao:
            messagebox.showwarning("Atenção", "Selecione uma OS.")
            return
        
        item = self.os_tree.item(selecao[0])
        os_id = item['values'][0]
        
        os_obj = next((os for os in self.sistema.ordens_servico if os.id_os == os_id), None)
        if os_obj:
            self.mecanico.alterar_status(os_obj, "Concluído")
            self.mecanico.qtd_veiculos_atendidos += 1
            messagebox.showinfo("Sucesso", f"OS #{os_id} concluída com sucesso!")
            self.atualizar_minhas_os()
    
    def atualizar_combos_requisicao(self):
        """Atualiza os comboboxes de requisição."""
        # Atualizar OS
        minhas_os = [os for os in self.sistema.ordens_servico if os.mecanico == self.mecanico]
        os_opcoes = [f"OS #{os.id_os} - {os.cliente.nome if os.cliente else 'N/A'}" for os in minhas_os]
        self.os_requisicao_combo['values'] = os_opcoes
        if os_opcoes:
            self.os_requisicao_combo.current(0)
        
        # Atualizar peças
        pecas_opcoes = [f"ID {p.id} - {p.nome} (Estoque: {p.qtd_estoque})" for p in self.sistema.pecas]
        self.peca_requisicao_combo['values'] = pecas_opcoes
        if pecas_opcoes:
            self.peca_requisicao_combo.current(0)
    
    def requisitar_peca(self):
        """Requisita uma peça do estoque."""
        if not self.os_requisicao_combo.get() or not self.peca_requisicao_combo.get():
            messagebox.showwarning("Atenção", "Selecione uma OS e uma peça.")
            return
        
        try:
            qtd = int(self.qtd_requisicao_var.get())
            if qtd <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida.")
            return
        
        # Buscar OS e peça
        os_index = self.os_requisicao_combo.current()
        peca_index = self.peca_requisicao_combo.current()
        
        minhas_os = [os for os in self.sistema.ordens_servico if os.mecanico == self.mecanico]
        os_obj = minhas_os[os_index] if os_index < len(minhas_os) else None
        peca_obj = self.sistema.pecas[peca_index] if peca_index < len(self.sistema.pecas) else None
        
        if not os_obj or not peca_obj:
            messagebox.showerror("Erro", "OS ou peça não encontrada.")
            return
        
        # Requisitar do estoque
        if self.mecanico.requisitar_estoque(peca_obj, qtd):
            # Adicionar à OS
            os_obj.adicionar_peca(peca_obj, qtd)
            messagebox.showinfo(
                "Sucesso",
                f"{qtd} unidade(s) de {peca_obj.nome} requisitada(s)!\n"
                f"Adicionada(s) à OS #{os_obj.id_os}\n"
                f"Novo valor total: R$ {os_obj.valor_total:.2f}"
            )
            self.atualizar_combos_requisicao()
            self.atualizar_estoque()
            self.atualizar_minhas_os()
        else:
            messagebox.showerror(
                "Erro",
                f"Estoque insuficiente de {peca_obj.nome}!\n"
                f"Disponível: {peca_obj.qtd_estoque}"
            )
    
    def atualizar_estoque(self):
        """Atualiza a visualização do estoque."""
        for item in self.estoque_tree.get_children():
            self.estoque_tree.delete(item)
        
        if not self.sistema.pecas:
            self.estoque_tree.insert("", "end", values=("", "", "Nenhuma peça no estoque", "", "", ""))
        else:
            for peca in self.sistema.pecas:
                valor_total = peca.qtd_estoque * peca.valor_unit
                self.estoque_tree.insert(
                    "",
                    "end",
                    values=(
                        peca.id,
                        peca.nome,
                        peca.descricao,
                        peca.qtd_estoque,
                        f"R$ {peca.valor_unit:.2f}",
                        f"R$ {valor_total:.2f}"
                    )
                )
    
    def on_closing(self):
        """Fecha a janela e volta ao login."""
        self.root.destroy()
        self.login_root.state('zoomed')
        self.login_root.deiconify()
    
    def logout(self):
        """Realiza logout do mecânico."""
        self.on_closing()
