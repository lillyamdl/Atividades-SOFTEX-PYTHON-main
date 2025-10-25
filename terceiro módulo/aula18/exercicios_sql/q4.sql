CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    cidade VARCHAR(100)
);

CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    valor DECIMAL(10,2),
    data_pedido DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- ======= INSERTS para tabela clientes =======
INSERT INTO clientes (id_cliente, nome, cidade) VALUES
(1, 'Ana Silva', 'Fortaleza'),
(2, 'Bruno Alves', 'São Paulo'),
(3, 'Carla Souza', 'Rio de Janeiro'),
(4, 'Diego Martins', 'Fortaleza'),
(5, 'Elisa Pereira', 'Belo Horizonte');

-- ======= INSERTS para tabela pedidos =======
INSERT INTO pedidos (id_pedido, id_cliente, valor, data_pedido) VALUES
(1, 1, 150.00, '2025-01-15'),
(2, 1, 75.50,  '2025-02-02'),
(3, 2, 320.00, '2025-03-20'),
(4, 3, 45.00,  '2025-04-10'),
(5, 2, 85.30,  '2025-05-05'),
(6, 3, 120.00, '2025-06-12'),
(7, 1, 200.00, '2025-07-01'),
(8, 5, 500.00, '2025-08-18'),
(9, 2, 15.00,  '2025-09-03');

SELECT 
    c.nome AS nome,
    COALESCE(SUM(p.valor), 0) AS total_gasto
FROM 
    clientes c
LEFT JOIN 
    pedidos p ON p.id_cliente = c.id_cliente
GROUP BY 
    c.nome
ORDER BY 
    total_gasto DESC;