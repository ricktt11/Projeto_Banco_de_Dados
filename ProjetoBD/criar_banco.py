import sqlite3  # Importa a biblioteca para usar SQLite

# Cria o banco de dados 'vendas.db'
banco = sqlite3.connect('vendas.db')
cursor = banco.cursor()  # Cria um cursor para executar comandos SQL

# Cria a tabela de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    cidade TEXT NOT NULL,
    numero TEXT NOT NULL,
    bairro TEXT NOT NULL,
    telefone TEXT NOT NULL
);
""")

# Cria a tabela de produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
);
""")

# Cria a tabela de pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_compra TEXT NOT NULL,
    vendedor TEXT NOT NULL,
    compra TEXT NOT NULL,
    clientes INTEGER NOT NULL,
    FOREIGN KEY (clientes) REFERENCES Clientes(id)
);
""")

# Cria a tabela de itens dos pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS ItensPedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido INTEGER NOT NULL,
    produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_unitario REAL NOT NULL,
    FOREIGN KEY (pedido) REFERENCES Pedidos(id),
    FOREIGN KEY (produto) REFERENCES Produtos(id)
);
""")

# Salva as alterações no banco
banco.commit()
# Fecha a conexão com o banco
banco.close()

print("Banco de dados criado com sucesso!")
