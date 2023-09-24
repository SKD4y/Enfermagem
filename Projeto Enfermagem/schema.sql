CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- ID do usuário
    nome VARCHAR(100) NOT NULL, -- Nome do usuário
    idade INT NOT NULL, -- Idade do usuário
    sexo VARCHAR(50) NOT NULL -- Sexo do usuário
);