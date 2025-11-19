import os 
from dataclasses import dataclass

os.system("cls")
@dataclass
class Funcionario:
    nome:str
    rg:str
    data_nascimento:str
    cpf:str

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"rg: {self.rg}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"cpf: {self.cpf}")

lista_de_funcionarios=[]
QUANTIDADE_DE_FUNCIONARIOS = 5

for i in range(QUANTIDADE_DE_FUNCIONARIOS):
    funcionario = Funcionario(
       nome= input("Digite seu nome: "),
       rg=input("Digite seu rg: "),
       data_nascimento=input("Digite sua data de nascimento: "),
       cpf=input("Digite seu CPF: "))
    lista_de_funcionarios.append(funcionario)
    print() # Pula uma linha.

nome_do_arquivo = "dados_funcionários.csv"
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_funcionarios:
   for funcionario in lista_de_funcionarios:
      arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.rg}, {funcionario.data_nascimento}, {funcionario.cpf}\n")
   print("Dados salvos com sucesso.")


print("\nExibindo todos os funcinários: ")
lista = []
try:
    # "r" - read leitura
   with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
    # Recebe todos os dados do arquivo de uma só
    lista_todos_funcionarios = arquivo.readlines()
    for funcionario in lista_todos_funcionarios:
        nome, rg, data_nascimento, cpf = funcionario.strip().split(",")
        dados_funcionario = Funcionario(nome =nome, rg=rg, data_nascimento=data_nascimento, cpf=cpf)
        lista.append(dados_funcionario)
    for funcionario in lista:
        funcionario.exibir_dados()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")