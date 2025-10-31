import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Aluno:
    nome : str
    idade : int
    email : str
    telefone : str


QUANTIDADE_ALUNOS = 2
lista_aluno = []


for i in range(QUANTIDADE_ALUNOS):
    aluno= Aluno(nome= input("Digite seu nome: "),
                 idade=int(input("Digite sua idade: ")),
                 email=input("Digite seu e-mail: "),
                 telefone=input("Digite seu telefone: ")
                 )
    
    lista_aluno.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_alunos.text"


with open(arquivo, "a") as arquivo_aluno:
    for aluno in lista_aluno:
        arquivo_aluno.write(f"{aluno.nome}, {aluno.idade}, {aluno.email}, {aluno.telefone}\n")
        print("Salvo com sucesso!")

