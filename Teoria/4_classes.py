import os
from dataclasses import dataclass
os.system("cls")

# Estrutua de dados: classe.
@dataclass
class Pessoa:
    nome: str
    idade : int
    

    def mostrar_dados(self):
         print(f"Nome: {self.nome}")
         print(f"Idade: {self.idade}")


print("Solicitando os dados da 1ª pessoa.")
pessoa1 = Pessoa(nome = input("Digite seu nome: "),
                 idade = int(input("Digite sua idade:")))

print("\nSolicitando os dados da 2ª pessoa.")
pessoa2 = Pessoa(nome = input("Digite seu nome: "),
              idade = int(input("Digite sua idade:")))
                 

print("\nExibindo dados da 1ª Pessoa.")
pessoa1.mostrar_dados()
print("\nExibindo dados da 2ª Pessoa.")
pessoa2.mostrar_dados()
                 



