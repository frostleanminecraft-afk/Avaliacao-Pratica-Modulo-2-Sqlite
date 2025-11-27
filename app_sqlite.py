"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""

import sqlite3 as sq3

conexao = sq3.connect("escola.db")

conexao.execute("""
CREATE TABLE IF NOT EXISTS Alunos(id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER NOT NULL, email TEXT NOT NULL);

""")

conexao.execute("""
INSERT INTO Alunos (nome, idade, email) VALUES
                ("camila cabelo", 99, "joana@gmail.com"),
                ("Hannah tamanduá-bandeira", 400, "tamandua.arroz@gmail.com"),
                ("Samuel hidratantes", 270, "agua.c@gmail.com"),
                ("Meu prefeito", 25, "Fernando@gmail.com");

""")

lista_alunos = conexao.execute("SELECT * FROM Alunos").fetchall()
print("Alunos:",lista_alunos)

Alunos = conexao.execute("SELECT * FROM Alunos WHERE id =2").fetchone()
print("Aluno 3", Alunos)

#atualizar registros
conexao.execute("UPDATE Alunos SET nome = 'Hannah tamanduá-bandeira' WHERE Nome ='Samuel hidratantes'")

lista_alunos = conexao.execute("SELECT * FROM Alunos").fetchall()
print("Alunos:",lista_alunos)

#Deletar registros
conexao.execute("DELETE FROM Alunos WHERE nome = 'camila cabelo'")
lista_alunos = conexao.execute("SELECT * FROM Alunos").fetchall()
print("Alunos:",lista_alunos)