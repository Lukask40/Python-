import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Aluno:
    nome : str
    idade : str

QUANTIDADE_ALUNOS = 2
lista_aluno = []


for i in range(QUANTIDADE_ALUNOS):
    aluno=Aluno(nome= input("Digite seu nome: "),
                idade=int(input("Digite sua idade: ")))
    
    lista_aluno.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_alunos.text"


with open(arquivo, "w") as arquivo_aluno:
    for aluno in lista_aluno:
        arquivo_aluno.write(f"{aluno.nome}, {aluno.idade}\n")
        print("Salvo com sucesso!")

