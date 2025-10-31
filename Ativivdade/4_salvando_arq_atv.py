import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Livros:
    nome : str
    autor : str
    categoria : str
    preco: float


QUANTIDADE_LIVROS = 3
lista_livros = []


for i in range(QUANTIDADE_LIVROS):
    livro=Livros (nome= input("Digite o nome do livro: "),
                 autor=input("Digite o nome do autor: "),
                 categoria=input("Digite a categoria do livro: "),
                 preco=float(input("Digite o preço do livro: ")))
                 
    
    lista_livros.append(livro)

print()
print("Salvando dados.")
arquivo = "catalogo_livros.text"


with open(arquivo, "a") as arquivo_aluno:
    for livro in lista_livros:
        arquivo_aluno.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preco}\n")
        print("Salvo com sucesso!")

