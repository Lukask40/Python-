import os 
from dataclasses import dataclass

os.system("cls")
@dataclass
class Paciente:
    nome:str
    idade:int

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

lista_de_pacientes=[]
QUANTIDADE_DE_PACIENTES = 2

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(
       nome= input("Digite seu nome: "),
       idade=int(input("Digite sua idade: ")))
    lista_de_pacientes.append(paciente)
    print() # Pula uma linha.

nome_do_arquivo = "dados _pacientes.csv"
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_pacientes:
   for paciente in lista_de_pacientes:
      arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")
   print("Dados salvos com sucesso.")

#print("\nExibindo lista de pacientes:")
#for paciente in lista_de_pacientes:
#   paciente.exibir_dados()

# print("\nExibindo todos os pacientes: ")
# try:
#     # "r"= read = leitura
#     with open(nome_do_arquivo, "r", encoding="uft-8") as arquivo:
#         lista_todos_pacientes = arquivo.readlines()
#         for paciente in lista_todos_pacientes:
#             print(f"- {paciente.strip()}")
# except FileNotFoundError:
#     print("O arquivo não foi encontrado.")



print("\nExibindo todos os pacientes: ")
lista = []
try:
    # "r" - read leitura
   with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
    # Recebe todos os dados do arquivo de uma só
    lista_todos_pacientes = arquivo.readlines()
    for paciente in lista_todos_pacientes:
        nome, idade = paciente.strip().split(",")
        dados_paciente = Paciente (nome =nome, idade=int(idade))
        lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")