import os
from dataclasses import dataclass
os.system("cls")

# Estrutua de dados: classe.
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso : float
    altura : float



# Exemplo de uso da classe.
pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 idade=int(input("Digite sua idade: ")), 
                 peso=float(input("Digite seu peso: ")) , 
                 altura=float(input("Digite sua altura: ")))
                 


print("Exibindo dados da Pessoa.")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\npeso: {pessoa1.peso}\naltura: {pessoa1.altura}")

