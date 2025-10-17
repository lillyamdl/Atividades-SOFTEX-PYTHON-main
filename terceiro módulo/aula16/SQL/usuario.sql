CREATE DATABASE escola;

USE escola;

CREATE TABLE alunos (
    id int AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    serie VARCHAR(50) not NULL
);

INSERT INTO alunos(nome, idade, serie) VALUES
('lila', 9, '4 serie'),
('ana', 10, '8 serie'),
('bia', 11, '5 serie'),
('carlos', 12,'8 serie'),
('joao', 13, '7 serie');


select nome from alunos where serie = '8 serie';

UPDATE alunos
SET idade = 10
WHERE nome = 'lila';

select nome from alunos where idade = 10;

DELETE from alunos where idade = 13;

select * from alunos;


