import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
 nome : str
 idade : int
 cpf : str

@dataclass
class Pet:
 nome: str
 idade: int
 peso : float
# Exemplo de uso da classe 
pessoa1 = Pessoa("Marta", 20, "400022645-69")
pet1 = Pet("Totó", 4, 2.100)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade} , cpf: {pessoa1.cpf}")
print(f"Nome: {pet1.nome}, Idade: {pet1.idade}, peso: {pet1.peso}")



print("\nExibindo dados da Pessoa.")
print (f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\ncpf{pessoa1.cpf}")

print("Exibindo dados do Pet.\n")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\n Peso: {pet1.peso}")