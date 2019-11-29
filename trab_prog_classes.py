from peewee import *
import os

arq = 'biblioteca.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Livro(BaseModel):
  titulo = CharField()
  numero_paginas = IntegerField()

class Genero(BaseModel):
  tipo_genero = CharField()

class Categoria(BaseModel):
  tipo_categoria = CharField()

class Editora(BaseModel):
  nome_editora = CharField()

class Autor(BaseModel):
  nome_autor = CharField()

class Emprestimo(BaseModel):
  data_locacao = DateTimeField()
  data_devolucao = DateTimeField()

class Estoque(BaseModel):
  qtd_livro = IntegerField()
  livro = ForeignKeyField(Livro)

class Estante(BaseModel):
  local = CharField()
  livro = ForeignKeyField(Livro)

class Bibliotecario(BaseModel):
  nome = CharField()
  login = CharField()
  senha = CharField()

class Cliente(BaseModel):
  nome = CharField()
  login = CharField()
  senha = CharField()
  contato = CharField()

cartasdeamor = Livro.create(titulo = "Cartas de Amor aos Mortos", numero_paginas = 337)
gen1 = Genero.create(tipo_genero = "Drama")
cat1 = Categoria.create(tipo_categoria = "Mais Lidos")
edit1 = Editora.create(nome_editora = "Seguinte")
aut1 = Autor.create(nome_autor = "Ava Dellaira")
emp1 = Emprestimo.create(data_locacao = datetime(2019, 11, 25), data_devolucao = datetime(2019, 12, 09))
estoq1 = Estoque.create(qtd_livro = 1, livro = cartasdeamor)
estan1 = Estante.create(local = "2° estante, 1° prateleira", livro  = cartasdeamor)
alexia = Bibliotecario.create(nome = "Aléxia Santos", login = "alexiatai", senha = "5678")
hylson = Cliente.create(nome = "Hylson Vescovi", login = "hylson", senha = "1234", contato = "47993029427")


