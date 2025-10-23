import os
from dataclasses import dataclass
os.system("cls")

# Estrutua de dados: classe.
@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    endereco : str



# Exemplo de uso da classe.
pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 email=input("Digite seu e-mail: "), 
                 telefone=input("Digite seu telefone: ") , 
                 endereco=input("Digite seu endereco: "))
                 


print("Exibindo dados da Pessoa.")
print(f"Nome: {pessoa1.nome}\nemail: {pessoa1.email}\ntelefone: {pessoa1.telefone}\nendereco: {pessoa1.endereco}")
