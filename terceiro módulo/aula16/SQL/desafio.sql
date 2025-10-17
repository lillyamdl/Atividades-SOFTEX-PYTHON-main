CREATE DATABASE escola;

USE escola;


create table professores(
    id int auto_increment primary key,
    nome varchar(100),
    materia varchar(100)
);

insert into professores(nome, materia)
values
('lila', 'historia'),
('bia' , 'bio'),
('ana', 'geografia');

select * from professores

