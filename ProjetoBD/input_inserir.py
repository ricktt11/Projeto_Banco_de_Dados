import sqlite3  # Importa a biblioteca para trabalhar com banco de dados SQLite

banco = sqlite3.connect('vendas.db') # Conecta ao banco de dados 'vendas.db'
cursor = banco.cursor()  # Cria um cursor para executar comandos SQL

# Exibe o menu de opções para o usuário
print("\n--- Você quer: ---")
print("1. Inserir novo cliente")
print("2. Inserir novo produto")
print("3. Inserir novo pedido com itens")
opcao = input("Escolha uma opção (1/2/3 ou Enter para sair): ")

# Opção 1 - Inserir cliente
if opcao == "1":
    # Coleta os dados do cliente
    nome = input("Nome do cliente: ")
    email = input("Email: ")
    cidade = input("Cidade: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    telefone = input("Telefone: ")

    # Insere o cliente no banco de dados
    cursor.execute("""
        INSERT INTO Clientes (nome, email, cidade, numero, bairro, telefone) VALUES (?, ?, ?, ?, ?, ?);
    """, (nome, email, cidade, numero, bairro, telefone))

    banco.commit()  # Salva as alterações
    print("Cliente inserido com sucesso!")

# Opção 2 - Inserir produto
elif opcao == "2":
    # Coleta os dados do produto
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    categoria = input("Categoria: ")

    # Insere o produto no banco de dados
    cursor.execute("""
        INSERT INTO Produtos (nome, preco, categoria) VALUES (?, ?, ?);
    """, (nome, preco, categoria))

    banco.commit()  # Salva as alterações
    print("Produto inserido com sucesso!")

# Opção 3 - Inserir pedido e seus itens
elif opcao == "3":
    # Coleta os dados do pedido
    cliente = int(input("ID do cliente que fez o pedido: "))
    data_compra = input("Data da compra (YYYY-MM-DD): ")
    vendedor = input("Nome do vendedor: ")
    compra = input("Produto Comprado: ")

    # Insere o pedido na tabela Pedidos
    cursor.execute("""
        INSERT INTO Pedidos (data_compra, vendedor, compra, clientes) VALUES (?, ?, ?, ?);
    """, (data_compra, vendedor, compra, cliente))

    pedido = cursor.lastrowid  # Pega o ID do pedido recém-inserido

    print("\nAgora vamos adicionar os itens do pedido.")
    while True:
        # Coleta os dados de cada item
        produto = int(input("ID do produto: "))
        quantidade = int(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: "))

        # Insere o item do pedido
        cursor.execute("""
            INSERT INTO ItensPedido (pedido, produto, quantidade, valor_unitario) VALUES (?, ?, ?, ?);
        """, (pedido, produto, quantidade, valor_unitario))

        # Pergunta se o usuário quer adicionar mais itens
        continuar = input("Deseja adicionar mais itens a este pedido? (s/n): ")
        if continuar.lower() != "s":
            break

    banco.commit()  # Salva o pedido e os itens
    print("Pedido e itens inseridos com sucesso!")

# Se nenhuma opção válida for selecionada
else:
    print("Nenhuma opção selecionada. Saindo...")

# Fecha a conexão com o banco de dados
banco.close()
