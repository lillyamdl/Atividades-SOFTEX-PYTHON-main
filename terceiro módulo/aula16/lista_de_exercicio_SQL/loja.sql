create database loja;

use loja;

create table produtos(
    id int auto_increment primary key,
    nome varchar(100),
    preco decimal(10,2),
    estoque int
);

insert into produtos(nome, preco, estoque) values
('camisa', 59.90, 30),
('calça jeans', 120.00, 15),
('tênis', 250.00, 10);

select * from produtos;

select nome, preco from produtos;

select nome from produtos where preco > 100;

update produtos
set estoque = estoque + 5
where nome = 'calça jeans';

delete from produtos where nome = 'tênis';

select * from produtos;