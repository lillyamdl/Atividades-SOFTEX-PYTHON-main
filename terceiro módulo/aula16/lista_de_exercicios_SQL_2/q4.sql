CREATE TABLE Alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    idade INT,
    cidade VARCHAR(50)
);

INSERT INTO Alunos (nome, idade, cidade)
VALUES 
('Maria Silva', 20, 'São Paulo'),
('João Santos', 22, 'Rio de Janeiro'),
('Ana Souza', 19, 'Belo Horizonte'),
('Carlos Pereira', 25, 'Curitiba');

CREATE TABLE Cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_curso VARCHAR(50),
    carga_horaria INT
);

INSERT INTO Cursos (nome_curso, carga_horaria)
VALUES 
('Banco de Dados', 40),
('Lógica de Programação', 60),
('Desenvolvimento Web', 80);


select nome, idade  from Alunos where idade < 22;