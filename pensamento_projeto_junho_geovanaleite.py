import tkinter as tk
from tkinter import ttk, messagebox

# ==============================================================================
# BANCO DE DADOS SIMULADO EM MEMÓRIA
# ==============================================================================
produtos = []
vendas = []
clientes = []

# ==============================================================================
# FUNÇÕES DE LÓGICA DO SISTEMA
# ==============================================================================
def cadastrar_produto():
    try:
        produto = {
            'codigo': txt_p_cod.get(),
            'nome': txt_p_nome.get(),
            'marca': txt_p_marca.get(),
            'estoque': int(txt_p_est.get()),
            'estoque_minimo': int(txt_p_est_min.get()),
            'preco_custo': float(txt_p_custo.get()),
            'preco_venda': float(txt_p_venda.get()),
            'validade': txt_p_val.get(),
            'lote': txt_p_lote.get(),
            'descricao': txt_p_desc.get()
        }
        if not produto['codigo'] or not produto['nome']:
            raise ValueError("Código e Nome são obrigatórios.")
            
        produtos.append(produto)
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        limpar_campos_produto()
        atualizar_tabela_produtos()
    except ValueError as e:
        messagebox.showerror("Erro", f"Dados inválidos ou incompletos:\n{e}")

def atualizar_tabela_produtos():
    # Limpa a tabela antes de recarregar
    for i in tree_produtos.get_children():
        tree_produtos.delete(i)
    # Insere os dados atualizados
    for p in produtos:
        tree_produtos.insert("", "end", values=(p['codigo'], p['nome'], p['estoque'], f"R$ {p['preco_venda']:.2f}"))

def realizar_venda():
    if not produtos:
        messagebox.showwarning("Aviso", "Não há produtos cadastrados para vender.")
        return
        
    cod_prod = txt_v_prod_cod.get()
    produto_encontrado = None
    
    for p in produtos:
        if p['codigo'] == cod_prod:
            produto_encontrado = p
            break
            
    if produto_encontrado:
        try:
            qtd = int(txt_v_qtd.get())
            if produto_encontrado['estoque'] >= qtd:
                produto_encontrado['estoque'] -= qtd
                valor_total = produto_encontrado['preco_venda'] * qtd
                
                venda = {
                    'codigo_venda': txt_v_cod.get(),
                    'cliente': txt_v_cliente.get(),
                    'produto': produto_encontrado['nome'],
                    'quantidade': qtd,
                    'valor_total': valor_total,
                    'lucro_estimado': (produto_encontrado['preco_venda'] - produto_encontrado['preco_custo']) * qtd
                }
                vendas.append(venda)
                messagebox.showinfo("Sucesso", f"Venda realizada!\nTotal: R$ {valor_total:.2f}")
                
                atualizar_tabela_produtos()
                atualizar_tabela_vendas()
                limpar_campos_venda()
            else:
                messagebox.showerror("Erro", "Estoque insuficiente para este produto.")
        except ValueError:
            messagebox.showerror("Erro", "Insira uma quantidade válida.")
    else:
        messagebox.showerror("Erro", "Produto não encontrado com este código.")

def atualizar_tabela_vendas():
    for i in tree_vendas.get_children():
        tree_vendas.delete(i)
    for v in vendas:
        tree_vendas.insert("", "end", values=(v['codigo_venda'], v['cliente'], v['produto'], v['quantidade'], f"R$ {v['valor_total']:.2f}"))

def cadastrar_cliente():
    nome = txt_c_nome.get()
    if nome:
        cliente = {
            'nome': nome,
            'telefone': txt_c_tel.get(),
            'preferencia': txt_c_pref.get()
        }
        clientes.append(cliente)
        messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado!")
        txt_c_nome.delete(0, tk.END)
        txt_c_tel.delete(0, tk.END)
        txt_c_pref.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "O nome do cliente é obrigatório.")

def rodar_analise_ia():
    if not vendas:
        lbl_ia_res.config(text="Dados insuficientes para análise. Realize vendas primeiro.")
        return
    faturamento = sum(v['valor_total'] for v in vendas)
    lucro = sum(v['lucro_estimado'] for v in vendas)
    lbl_ia_res.config(text=f"Faturamento Total: R$ {faturamento:.2f}\n"
                           f"Lucro Líquido Estimado: R$ {lucro:.2f}\n"
                           f"Transações Analisadas: {len(vendas)}\n"
                           f"Insight: Sugerir promoções combinadas para os itens mais vendidos.")

def limpar_campos_produto():
    for campo in [txt_p_cod, txt_p_nome, txt_p_marca, txt_p_est, txt_p_est_min, txt_p_custo, txt_p_venda, txt_p_val, txt_p_lote, txt_p_desc]:
        campo.delete(0, tk.END)

def limpar_campos_venda():
    txt_v_cod.delete(0, tk.END)
    txt_v_cliente.delete(0, tk.END)
    txt_v_prod_cod.delete(0, tk.END)
    txt_v_qtd.delete(0, tk.END)

# ==============================================================================
# ESTRUTURA DA INTERFACE GRÁFICA (TKINTER)
# ==============================================================================
janela = tk.Tk()
janela.title("Sistema de Vendas - Açaiteria")
janela.geometry("850x700")
janela.resizable(False, False)

# Estilo para deixar o visual do UX mais moderno
style = ttk.Style()
style.theme_use("clam")

# Criando as Abas (Notebook)
notebook = ttk.Notebook(janela)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)
aba3 = ttk.Frame(notebook)
aba4 = ttk.Frame(notebook)

notebook.add(aba1, text="Produtos & Clientes")
notebook.add(aba2, text="Realizar Vendas")
notebook.add(aba3, text="Histórico de Vendas")
notebook.add(aba4, text="Módulo IA & UX/Dev")

# --- ABA 1: PRODUTOS & CLIENTES ---
# Formulário de Cadastro de Produto
lbl_frame_prod = ttk.LabelFrame(aba1, text=" Cadastrar Novo Produto ")
lbl_frame_prod.pack(padx=10, pady=5, fill="x")

campos_prod = [
    ("Código:", "txt_p_cod"), ("Nome:", "txt_p_nome"), ("Marca:", "txt_p_marca"),
    ("Estoque:", "txt_p_est"), ("Estoque Mín:", "txt_p_est_min"), ("Preço Custo:", "txt_p_custo"),
    ("Preço Venda:", "txt_p_venda"), ("Validade:", "txt_p_val"), ("Lote:", "txt_p_lote"),
    ("Descrição:", "txt_p_desc")
]

# Grid interno para organizar os campos de produto de forma limpa
for idx, (label_text, var_name) in enumerate(campos_prod):
    r = idx // 2
    c = (idx % 2) * 2
    ttk.Label(lbl_frame_prod, text=label_text).grid(row=r, column=c, padx=5, pady=3, sticky="e")
    globals()[var_name] = ttk.Entry(lbl_frame_prod, width=18)
    globals()[var_name].grid(row=r, column=c+1, padx=5, pady=3, sticky="w")

btn_cad_prod = ttk.Button(lbl_frame_prod, text="Salvar Produto", command=cadastrar_produto)
btn_cad_prod.grid(row=5, column=0, columnspan=4, pady=10)

# Formulário de Cadastro de Cliente
lbl_frame_cli = ttk.LabelFrame(aba1, text=" Cadastrar Cliente ")
lbl_frame_cli.pack(padx=10, pady=5, fill="x")

ttk.Label(lbl_frame_cli, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
txt_c_nome = ttk.Entry(lbl_frame_cli, width=15)
txt_c_nome.grid(row=0, column=1, padx=5, pady=5, sticky="w")

ttk.Label(lbl_frame_cli, text="Telefone:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
txt_c_tel = ttk.Entry(lbl_frame_cli, width=12)
txt_c_tel.grid(row=0, column=3, padx=5, pady=5, sticky="w")

ttk.Label(lbl_frame_cli, text="Preferência:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
txt_c_pref = ttk.Entry(lbl_frame_cli, width=12)
txt_c_pref.grid(row=0, column=5, padx=5, pady=5, sticky="w")

btn_cad_cli = ttk.Button(lbl_frame_cli, text="Salvar Cliente", command=cadastrar_cliente)
btn_cad_cli.grid(row=0, column=6, padx=10, pady=5)

# Tabela de Produtos cadastrados para visualização imediata
lbl_frame_lista_prod = ttk.LabelFrame(aba1, text=" Estoque Atual de Produtos ")
lbl_frame_lista_prod.pack(padx=10, pady=5, fill="both", expand=True)

tree_produtos = ttk.Treeview(lbl_frame_lista_prod, columns=("Código", "Nome", "Estoque", "Preço Venda"), show="headings", height=5)
tree_produtos.heading("Código", text="Código")
tree_produtos.heading("Nome", text="Nome")
tree_produtos.heading("Estoque", text="Estoque")
tree_produtos.heading("Preço Venda", text="Preço Venda")
tree_produtos.pack(fill="both", expand=True, padx=5, pady=5)

# --- ABA 2: REALIZAR VENDAS ---
lbl_frame_realizar_venda = ttk.LabelFrame(aba2, text=" Informações da Venda ")
lbl_frame_realizar_venda.pack(padx=20, pady=20, fill="both", expand=True)

ttk.Label(lbl_frame_realizar_venda, text="Cód. Venda:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
txt_v_cod = ttk.Entry(lbl_frame_realizar_venda, width=25)
txt_v_cod.grid(row=0, column=1, padx=10, pady=10, sticky="w")

ttk.Label(lbl_frame_realizar_venda, text="Cliente:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
txt_v_cliente = ttk.Entry(lbl_frame_realizar_venda, width=25)
txt_v_cliente.grid(row=1, column=1, padx=10, pady=10, sticky="w")

ttk.Label(lbl_frame_realizar_venda, text="Cód. Produto:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
txt_v_prod_cod = ttk.Entry(lbl_frame_realizar_venda, width=25)
txt_v_prod_cod.grid(row=2, column=1, padx=10, pady=10, sticky="w")

ttk.Label(lbl_frame_realizar_venda, text="Quantidade:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
txt_v_qtd = ttk.Entry(lbl_frame_realizar_venda, width=25)
txt_v_qtd.grid(row=3, column=1, padx=10, pady=10, sticky="w")

btn_vender = ttk.Button(lbl_frame_realizar_venda, text="Confirmar Transação", command=realizar_venda)
btn_vender.grid(row=4, column=0, columnspan=2, pady=20)

# --- ABA 3: HISTÓRICO DE VENDAS ---
lbl_frame_historico = ttk.LabelFrame(aba3, text=" Relatório de Vendas Efetuadas ")
lbl_frame_historico.pack(padx=10, pady=10, fill="both", expand=True)

tree_vendas = ttk.Treeview(lbl_frame_historico, columns=("ID Venda", "Cliente", "Produto", "Qtd", "Valor Total"), show="headings")
tree_vendas.heading("ID Venda", text="ID Venda")
tree_vendas.heading("Cliente", text="Cliente")
tree_vendas.heading("Produto", text="Produto")
tree_vendas.heading("Qtd", text="Qtd")
tree_vendas.heading("Valor Total", text="Valor Total")
tree_vendas.pack(fill="both", expand=True, padx=5, pady=5)

# --- ABA 4: MÓDULO IA & UX/DEV ---
# Frame da IA
lf_ia = ttk.LabelFrame(aba4, text=" Análise Predictiva & Relatório de Desempenho (IA) ")
lf_ia.pack(padx=10, pady=5, fill="both", expand=True)

btn_ia = ttk.Button(lf_ia, text="Executar Análise de Dados", command=rodar_analise_ia)
btn_ia.pack(pady=10)

lbl_ia_res = ttk.Label(lf_ia, text="Dados insuficientes para análise. Realize vendas primeiro.", justify="center", font=("Arial", 10, "bold"))
lbl_ia_res.pack(pady=15)

# Frame de Informações Técnicas
lf_ux_dev = ttk.LabelFrame(aba4, text=" Informações Técnicas (Módulos UX / Tech / Dev) ")
lf_ux_dev.pack(padx=10, pady=10, fill="both", expand=True)

info_tech = (
    "• UX (Interface): Mudança do terminal para abas Tkinter para reduzir a carga\n"
    "  cognitiva e otimizar o tempo de atendimento do operador.\n\n"
    "• Dev/Tech (Código): Lógica modularizada por funções estruturadas.\n"
    "  Campos limpos automaticamente após as inserções de dados bem-sucedidas.\n\n"
    "• QA: Validações de tipos implementadas por tratamento de exceção (try/except)."
)

lbl_tech_info = ttk.Label(lf_ux_dev, text=info_tech, justify="left")
lbl_tech_info.pack(padx=10, pady=10, anchor="nw")

# Inicia o loop principal da aplicação
janela.mainloop()