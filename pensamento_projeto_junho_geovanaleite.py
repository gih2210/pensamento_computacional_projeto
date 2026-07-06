'''
 Um Bloco de Comentarios.
 Para explicar o que o código faz, ou para deixar anotações para o programador.
 >>projeto açaiteria:

 >PO (Como dono do negocio: Quero um sistema de vendas para minha açaiteria, 
 para que eu possa controlar as vendas e os produtos.)

 >QA (Como cliente: Quero um sistema de vendas para minha açaiteria,
 para que eu possa comprar meus produtos favoritos de forma rápida e fácil.)

 >Tech (Como programador: Quero um sistema de vendas para minha açaiteria, 
 para que eu possa desenvolver um software eficiente e funcional para o negócio.)

 >Dev (Como programador: Quero um sistema de vendas para minha açaiteria, para
 que eu possa implementar as funcionalidades necessárias para atender as 
 necessidades do negócio e dos clientes.)

 >UX (Como designer de experiência do usuário: Quero um sistema de vendas para minha 
 açaiteria, para que eu possa criar uma interface intuitiva e agradável para os
 usuários, garantindo uma experiência de compra satisfatória.)

 >IA (Como analista de dados: Quero um sistema de vendas para minha açaiteria, para que 
 eu possa coletar e analisar os dados de vendas, ajudando a identificar padrões de consumo
 e otimizar as estratégias de marketing e estoque.)

'''
while True:
   print('\n----------------------------------------------------------\n')
   print('Bem-vindo ao sistema de vendas da Açaiteria!')
   print('1 - Cadastrar produto')
   print('2 - Listar produtos')
   print('3 - Realizar venda')
   print('4 - Listar vendas')
   print('5 - Analisar dados de vendas')
   print('6 - Criar interface de usuário')
   print('7 - Implementar funcionalidades')
   print('8 - Otimizar estratégias de marketing')
   print('9 - Cadastrar cliente')
   print('0 - Sair')
   print('\n----------------------------------------------------------\n')
   
opcao = input('digite a opção desejada: ')

if opcao == '1':
   print('opção 1 - cadastrando produtos')
   codigo_produto = input('Digite o código do produto: ')
   nome_produto = input('Digite o nome do produto: ')
   marca_produto = input('Digite a marca do produto: ')
   quantidade_estoque = int(input('Digite a quantidade em estoque: '))
   estoque_minimo = int(input('Digite o estoque mínimo: '))
   preco_custo = float(input('Digite o preço de custo: '))
   validade_produto = input('Digite a validade do produto: ')
   lote_produto = input('Digite o lote do produto: ')
   descricao_produto = input('Digite a descrição do produto: ')
elif opcao == '2':
   print ('opção 2: - listando produtos')
   nome_produto = input('Digite o nome do produto: ')
   codigo_produto = input('Digite o código do produto: ')
   marca_produto = input('Digite a marca do produto: ')
   categoria_produto = input('Digite a categoria do produto: ')
   fornecedor_produto = input('Digite o fornecedor: ')
   validade_produto = input('Digite a validade do produto: ')
   lote_produto = input('Digite o lote do produto: ')
elif opcao == '3':
   print ('opção 3: - realizando venda') 
   codigo_venda = input('Digite o código da venda: ')
   nome_cliente = input('Digite o nome do cliente: ')
elif opcao == '0':
   print ('opção 0: - saindo do sistema')

   
   #break
else:
    print('Opção inválida. Por favor, selecione uma opção válida.')