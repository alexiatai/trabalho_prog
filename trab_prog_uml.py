@startuml
class Livro {
     titulo
     numero_paginas
}
Livro--Autor
@enduml



@startuml

class Genero {
tipo_genero
}
Livro -- Genero
@enduml



@startuml
class Categoria {
tipo_categoria
}
Livro--Categoria
@enduml



@startuml

class Editora {
nome_editora
}
@enduml


@startuml

class Autor {
nome_autor
}
Autor--Editora

@enduml


@startuml

class Emprestimo {
data_locacao
data_devolucao
}
Cliente--Emprestimo
Emprestimo *-- Livro

@enduml


@startuml

class Estoque {
qtd_livro
Livro
}
Estoque--Estante
Estoque o-- Livro
@enduml

@startuml

class Estante {
local
Livro
}
@enduml

@startuml

class Bibliotecario {
nome
login
senha
}
@enduml

class Cliente {
nome
login
senha
contato
}
@enduml