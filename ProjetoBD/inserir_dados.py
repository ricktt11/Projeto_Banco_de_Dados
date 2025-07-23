import sqlite3
banco = sqlite3.connect('vendas.db') # Conecta ao banco de dados 'vendas.db'
cursor = banco.cursor() # Cria um cursor para executar comandos

# Lista de 30 lientes com dados pessoais
clientes = [
    ('Rick Theo', 'rickk11theo@gmail.com', 'Tururu-CE', '123', 'Centro', '85994265451'),
    ('Silas Eufrásio', 'silas.oficial.prof@gmail.com', 'Itapajé-CE', '456', 'Boa Vista', '85992528574'),
    ('Kayron Henrique', 'khmt10@gmail.com', 'Tururu-CE', '789', 'Centro', '85991046599'),
    ('Pedro Nick', 'nick09pedro@gmail.com', 'Tururu-CE', '321', 'Vila Nova', '85992425583'),
    ('Heitor Braga', 'heitorbragadealmeida@gmail.com', 'Itapajé-CE', '654', 'Brasília', '85992112193'),
    ('João Silva', 'joao@gmail.com', 'São Paulo', '1001', 'Mooca', '11999999999'),
    ('Maria Oliveira', 'maria.oliveira@hotmail.com', 'Rio de Janeiro', '202', 'Copacabana', '21988887777'),
    ('Carlos Souza', 'carlos.souza@yahoo.com', 'Belo Horizonte', '303', 'Savassi', '31977776666'),
    ('Ana Paula', 'ana.paula@gmail.com', 'Curitiba', '404', 'Batel', '41966665555'),
    ('Bruno Santos', 'bruno.santos@hotmail.com', 'Porto Alegre', '505', 'Moinhos de Vento', '51955554444'),
    ('Fernanda Lima', 'fernanda.lima@yahoo.com', 'Fortaleza', '606', 'Aldeota', '85944443333'),
    ('Ricardo Alves', 'ricardo.alves@gmail.com', 'Recife', '707', 'Boa Viagem', '81933332222'),
    ('Patrícia Costa', 'patricia.costa@hotmail.com', 'Salvador', '808', 'Pituba', '71922221111'),
    ('Lucas Pereira', 'lucas.pereira@yahoo.com', 'Florianópolis', '909', 'Trindade', '4832123456'),
    ('Juliana Martins', 'juliana.martins@gmail.com', 'Goiânia', '111', 'Setor Bueno', '6231234567'),
    ('Eduardo Rocha', 'eduardo.rocha@hotmail.com', 'Manaus', '222', 'Centro', '9239876543'),
    ('Sofia Mendes', 'sofia.mendes@yahoo.com', 'Brasília', '333', 'Asa Norte', '6138765432'),
    ('Gustavo Fernandes', 'gustavo.fernandes@gmail.com', 'Natal', '444', 'Ponta Negra', '8497654321'),
    ('Camila Nunes', 'camila.nunes@hotmail.com', 'João Pessoa', '555', 'Tambaú', '8354321098'),
    ('Rafael Dias', 'rafael.dias@yahoo.com', 'São Luís', '666', 'Renascença', '9898765432'),
    ('Isabela Moreira', 'isabela.moreira@gmail.com', 'Maceió', '777', 'Pajuçara', '8297654321'),
    ('Thiago Gonçalves', 'thiago.goncalves@hotmail.com', 'Cuiabá', '888', 'Centro Norte', '6531234567'),
    ('Mariana Rodrigues', 'mariana.rodrigues@yahoo.com', 'Campo Grande', '999', 'Jardim dos Estados', '6731234567'),
    ('Felipe Castro', 'felipe.castro@gmail.com', 'Vitória', '1010', 'Praia do Canto', '2798765432'),
    ('Aline Cardoso', 'aline.cardoso@hotmail.com', 'Aracaju', '1111', '13 de Julho', '7998765432'),
    ('Daniel Oliveira', 'daniel.oliveira@yahoo.com', 'Teresina', '1212', 'Ilhotas', '8632123456'),
    ('Priscila Souza', 'priscila.souza@gmail.com', 'Belém', '1313', 'Marco', '9198765432'),
    ('André Lima', 'andre.lima@hotmail.com', 'Porto Velho', '1414', 'Centro', '6897654321'),
    ('Carla Ribeiro', 'carla.ribeiro@yahoo.com', 'Boa Vista', '1515', 'Mecejana', '9532123456'),
    ('Marcelo Fernandes', 'marcelo.fernandes@gmail.com', 'Macapá', '1616', 'Santa Rita', '9698765432')
]
# Insere todos os clientes no banco de dados
cursor.executemany(
    "INSERT INTO Clientes (nome, email, cidade, numero, bairro, telefone) VALUES (?,?,?,?,?,?)", clientes)

# Lista de produtos com nome, preço e categoria
produtos = [
    ("iPhone 13", 5000.00, "Smartphone"),
    ("iPhone 14", 6000.00, "Smartphone"),
    ("Samsung Galaxy S22", 4000.00, "Smartphone"),
    ("Samsung Galaxy A54", 2800.00, "Smartphone"),
    ("Xiaomi Redmi Note 12", 1700.00, "Smartphone"),
    ("Motorola Edge 40", 2500.00, "Smartphone"),
    ("Realme 11 Pro", 2300.00, "Smartphone"),
    ("Asus ROG Phone 6", 4200.00, "Gamer"),
    ("iPhone SE", 2800.00, "Compacto"),
    ("Samsung Z Flip", 6500.00, "Dobrável"),
    ("Nokia G60", 1400.00, "Smartphone"),
    ("LG K62", 1300.00, "Smartphone"),
    ("Huawei P40", 3500.00, "Smartphone"),
    ("Xiaomi Poco X5", 2000.00, "Gamer"),
    ("Motorola G73", 1800.00, "Smartphone"),
    ("Samsung Galaxy M14", 1600.00, "Smartphone"),
    ("iPhone 11", 3500.00, "Smartphone"),
    ("Realme C55", 1600.00, "Smartphone"),
    ("Motorola Edge 20", 2200.00, "Smartphone"),
    ("Asus Zenfone 9", 3200.00, "Compacto"),
    ("Xiaomi Mi 11", 3000.00, "Smartphone"),
    ("Samsung A23", 1500.00, "Smartphone"),
    ("iPhone 12 Mini", 3800.00, "Compacto"),
    ("Redmi Note 10", 1400.00, "Smartphone"),
    ("Sony Xperia 5", 4200.00, "Smartphone"),
    ("Samsung S21 FE", 3600.00, "Smartphone"),
    ("iPhone XR", 3300.00, "Smartphone"),
    ("Motorola G32", 1200.00, "Smartphone"),
    ("Nokia C30", 1000.00, "Básico"),
    ("Galaxy Note 20", 4500.00, "Gamer")
]
# Insere todos os produtos no banco de dados
cursor.executemany("INSERT INTO Produtos (nome, preco, categoria) VALUES (?, ?, ?);", produtos)

# Lista de pedidos com data, vendedor, nome do produto e ID do cliente
pedidos = [
    ("2025-07-10", "Rick", "iPhone 13", "1"),
    ("2025-07-11", "Silas", "Motorola G32", "4"),
    ("2025-07-12", "Rick", "Galaxy Note 20", "5"),
    ("2025-07-13", "Rick", "iPhone 13", "6"),
    ("2025-07-14", "Silas", "Samsung Galaxy A54", "10"),
    ("2025-07-15", "Silas", "iPhone 13", "25"),
    ("2025-07-16", "Silas", "iPhone 12 Mini", "30"),
    ("2025-07-17", "Rick", "Realme 11 Pro", "14"),
    ("2025-07-18", "Rick", "Phone XR", "12"),
    ("2025-07-19", "Silas", "Xiaomi Mi 11", "12")
]
# Insere todos os pedidos no banco de dados
cursor.executemany("INSERT INTO Pedidos (data_compra, vendedor, compra, clientes) VALUES (?, ?, ?, ?);", pedidos)

# Lista de itens dos pedidos (pedido_id, produto_id, quantidade, valor_unitário)
itens_pedido = [
    # Pedido 1
    (1, 1, 1, 5000.00),
    (1, 5, 1, 1700.00),

    # Pedido 2
    (2, 2, 2, 6000.00),
    (2, 10, 1, 6500.00),
    (2, 14, 1, 2000.00),

    # Pedido 3
    (3, 3, 1, 4000.00),
    (3, 13, 2, 3500.00),

    # Pedido 4
    (4, 4, 1, 2800.00),
    (4, 6, 1, 2500.00),
    (4, 7, 1, 2300.00),

    # Pedido 5
    (5, 8, 1, 4200.00),
    (5, 9, 1, 2800.00),

    # Pedido 6
    (6, 11, 1, 1400.00),
    (6, 12, 1, 1300.00),

    # Pedido 7
    (7, 15, 1, 1800.00),
    (7, 16, 2, 1600.00),

    # Pedido 8
    (8, 17, 1, 3500.00),
    (8, 18, 1, 1600.00),
    (8, 19, 1, 2200.00),

    # Pedido 9
    (9, 20, 1, 3200.00),
    (9, 21, 1, 3000.00),

    # Pedido 10
    (10, 25, 2, 3600.00),
    (10, 28, 1, 1200.00)
]
# Insere todos os itens dos pedidos no banco de dados
cursor.executemany("""INSERT INTO ItensPedido (pedido, produto, quantidade, valor_unitario)VALUES (?, ?, ?, ?);""", itens_pedido)

banco.commit() # Salva todas as alterações no banco
banco.close() # Fecha a conexão com o banco

