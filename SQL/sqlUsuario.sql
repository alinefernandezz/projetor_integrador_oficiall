use bd_medidor;

create table usuario(
	id int(10) not null auto_increment,
    nome varchar(100) not null, 
    email varchar(100) not null,
    senha varchar(100) not null,
    primary key (id)
);

INSERT INTO usuario (nome, email, senha) VALUES ('Felipe Fonseca', 'felipe@email.com', 'adm123');
INSERT INTO usuario (nome, email, senha) VALUES ('Ana Paula', 'AnaB@email.com', 'adm123');
INSERT INTO usuario (nome, email, senha) VALUES ('Aline Fernandes', 'Aline@email.com', 'adm123');
INSERT INTO usuario (nome, email, senha) VALUES ('Victor Costa', 'Victor@email.com', 'adm123');

select * from usuario;