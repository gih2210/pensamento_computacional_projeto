# 🍧 Sistema de Vendas - Açaiteria

Este é um sistema desktop para gerenciamento de vendas e estoque de uma açaiteria, desenvolvido em Python utilizando a biblioteca gráfica **Tkinter**. O projeto foca em uma experiência de usuário (UX) intuitiva dividida em abas, validação robusta de dados e um módulo simulado de inteligência analítica para insights de negócios.

---

## 🚀 Funcionalidades

### 📦 Produtos & Clientes

* **Cadastro de Produtos:** Controle completo com código, nome, marca, estoque atual, estoque mínimo, preço de custo, preço de venda, validade, lote e descrição.
* **Cadastro de Clientes:** Registro rápido de clientes com nome, telefone e preferências de consumo.
* **Tabela de Estoque:** Visualização em tempo real dos produtos cadastrados e quantidade disponível.

### 💰 Realizar Vendas

* Baixa automática no estoque ao confirmar a transação.
* Validação de quantidade (impede vendas se o estoque for insuficiente).
* Registro do valor total e cálculo automático do lucro estimado da transação.

### 📊 Histórico de Vendas

* Tabela dinâmica com o histórico completo de todas as vendas realizadas na sessão, exibindo ID da venda, cliente, produto, quantidade e valor total.

### 🧠 Módulo de Inteligência Analítica (IA) & UX

* **Insights de Negócios:** Painel que calcula o faturamento total, lucro líquido acumulado, total de transações e gera recomendações estratégicas automaticamente.
* **Foco em UX/Dev:** Interface moderna desenvolvida com o tema `clam` do Tkinter, minimizando a carga cognitiva do operador através de uma navegação por abas limpa e organizada.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica:** Tkinter / ttk (com tema `clam` para uma interface mais limpa e moderna)
* **Estrutura de Dados:** Dicionários e listas em memória (simulação de Banco de Dados)

---

## 💻 Como Executar o Projeto

1. **Pré-requisitos:** Certifique-se de ter o Python instalado na sua máquina (versão 3.6 ou superior). O Tkinter já vem instalado por padrão no Python na maioria dos sistemas operacionais.
2. **Clonar o repositório:**
```bash
git clone https://github.com/seu-usuario/sistema-vendas-acaiteria.git

```


3. **Navegar até a pasta do projeto:**
```bash
cd sistema-vendas-acaiteria

```


4. **Executar a aplicação:**
```bash
python main.py

```



---

## ⚙️ Arquitetura e Boas Práticas (QA & Dev)

* **Tratamento de Exceções:** Validações de tipos em tempo de execução via blocos `try/except` para impedir falhas ao inserir valores inválidos (como letras em campos de preço ou quantidade).
* **Modularidade:** Funções com responsabilidades únicas (Single Responsibility Principle) e limpeza automática de campos após operações bem-sucedidas.
* **Interface Responsiva:** Uso de gerenciadores de layout (`grid` e `pack`) combinados para garantir que os elementos se comportem de maneira previsível.

---