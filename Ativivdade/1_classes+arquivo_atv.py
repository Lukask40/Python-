import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome : str
    data_admissao: str
    matricula:str
    endereco:str

    def exibir_dados1(self):
        print(f"\nnome: {self.nome}")
        print(f"Data de admissão: {self.data_admissao}")
        print(f"Matricula: {self.matricula}")
        print(f"Endereço: {self.endereco}")


@dataclass
class Cliente:
    nome: str
    data_nascimento: str
    endereco : str


    def exibir_dados2(self):
        print(f"\nnome: {self.nome}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"Endereço: {self.endereco}")



lista_funcionarios = []
print("Dados funcionarios: ")
for i in range(3):
    dados_funcionarios = Funcionario(nome=input("Digite seu nome: "), 
                 data_admissao=input("Digite a data da sua admissão: ") , 
                 matricula=input("Digite sua matricula: "),
                 endereco=input("Digite seu Endereço: "))
    lista_funcionarios.append(dados_funcionarios)


nome_do_arquivo = "dados_funcionarios.csv"
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_funcionarios:
   for funcionario in lista_funcionarios:
      arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.data_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")
   print("Dados salvos com sucesso.")

print("\nExibindo todos os funcinários: ")
lista1 = []
try:
    # "r" - read leitura
   with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
    # Recebe todos os dados do arquivo de uma só
    lista_todos_funcionarios = arquivo.readlines()
    for funcionario in lista_todos_funcionarios:
        nome, data_admissao, matricula, endereco = funcionario.strip().split(",")
        dados_funcionario = Funcionario(nome =nome, data_admissao=data_admissao, matricula=matricula, endereco=endereco)
        lista1.append(dados_funcionario)
    for funcionario in lista_funcionarios:
        funcionario.exibir_dados1()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")







lista_clientes = []
print("\nDados clientes: ")

for i in range(3):
    dados_cliente = Cliente(nome=input("Digite seu nome: "), 
                 data_nascimento=input("Digite sua data de nascimeto: "), 
                 endereco=input("Digite seu endereço: "))
    lista_clientes.append(dados_cliente)
    



nome_do_arquivo = "dados_clientes.csv"
with open(nome_do_arquivo, "a", encoding="utf-8") as arquivo_clientes:
   for cliente in lista_clientes:
      arquivo_clientes.write(f"{cliente.nome}, {cliente.data_nascimento}, {cliente.endereco}\n")
   print("Dados salvos com sucesso.")




print("\nExibindo todos os clientes: ")
lista2 = []
try:
    # "r" - read leitura
   with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
    # Recebe todos os dados do arquivo de uma só
    lista_todos_clientes = arquivo.readlines()
    for cliente in lista_todos_clientes:
        nome, data_nascimento, endereco = cliente.strip().split(",")
        dados_cliente = Cliente(nome =nome, data_nascimento=data_nascimento, endereco=endereco)
        lista2.append(dados_cliente)
    for cliente in lista_clientes:
        cliente.exibir_dados2()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")










