-- SCRIPT SQL QUE DEMOSTRA OS COMANDOS SQL PARA CRIAÇÃO DA TABEALA CONTATOS QUE PERTENCE AO BANCO DE DADOS AGENDA

CREATE TABLE tbl_Contatos (
    id_Contato       INTEGER      PRIMARY KEY AUTOINCREMENT,
    nome_Contato     VARCHAR (30),
    telefone_Contato VARCHAR (15),
    email_Contato    VARCHAR (30) 
);