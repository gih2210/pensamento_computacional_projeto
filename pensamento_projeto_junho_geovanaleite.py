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
# ESTRUTURA DA INTERFACE GRAFICA (TKINTER)
# ==============================================================================
janela = tk.Tk()
janela.title("Sistema de Vendas - Açaiteria")
janela.geometry("800x650")
janela.resizable(False, False)

# Estilo para deixar o visual do UX mais moderno
style = ttk.Style()
style.theme_use("clam")

# Criando as Abas (Notebook) para separar os módulos de forma limpa
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
lbl_frame_prod.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

campos_prod = [
    ("Código:", "txt_p_cod"), ("Nome:", "txt_p_nome"), ("Marca:", "txt_p_marca"),
    ("Estoque:", "txt_p_est"), ("Estoque Mín:", "txt_p_est_min"), ("Preço Custo:", "txt_p_custo"),
    ("Preço Venda:", "txt_p_venda"), ("Validade:", "txt_p_val"), ("Lote:", "txt_p_lote"),
    ("Descrição:", "txt_p_desc")
]

for idx, (label_text, var_name) in enumerate(campos_prod):
    r = idx // 2
    c = (idx % 2) * 2
    ttk.Label(lbl_frame_prod, text=label_text).grid(row=r, column=c, padx=5, pady=5, sticky="e")
    globals()[var_name] = ttk.Entry(lbl_frame_prod, width=18)
    globals()[var_name].grid(row=r, column=c+1, padx=5, pady=5)

btn_cad_prod = ttk.Button(lbl_frame_prod, text="Salvar Produto", command=cadastrar_produto)
btn_cad_prod.grid(row=5, column=2, columnspan=2, pady=10)

# Formulário de Cadastro de Cliente
lbl_frame_cli = ttk.LabelFrame(aba1, text=" Cadastrar Cliente ")
lbl_frame_cli.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

ttk.Label(lbl_frame_cli, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
txt_c_nome = ttk.Entry(lbl_frame_cli, width=20)
txt_c_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(lbl_frame_cli, text="Telefone:").grid(row=0, column=2, padx=5, pady=5)
txt_c_tel = ttk.Entry(lbl_frame_cli, width=15)
txt_c_tel.grid(row=0, column=3, padx=5, pady=5)

# Subframe UX/Dev
lf_ux_dev = ttk.LabelFrame(aba4, text=" Informações Técnicas (Módulos UX / Tech / Dev) ")
lf_ux_dev.pack(padx=10, pady=10, fill="both", expand=True)

info_tech = (
    "• UX (Interface): Mudança do terminal para abas Tkinter para reduzir a carga\n"
    "  cognitiva e otimizar o tempo de atendimento do operador.\n\n"
    "• Dev/Tech (Código): Lógica modularizada por funções estruturadas.\n"
    "  Campos limpos automaticamente após as inserções de dados bem-sucedidas.\n\n"
    "• QA: Validações de tipos implementadas por tratamento de exceção (try/except)."
)

# CERTIFIQUE-SE DE QUE ESTA LINHA ESTÁ EXATAMENTE ASSIM:
lbl_tech_info = ttk.Label(lf_ux_dev, text=info_tech, justify="left")
lbl_tech_info.pack(padx=10, pady=10, anchor="nw")

# Inicia o loop da interface gráfica
janela.mainloop()