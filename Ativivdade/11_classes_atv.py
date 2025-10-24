import os
os.system("cls")
from dataclasses import dataclass


import os
from dataclasses import dataclass
os.system("cls")


@dataclass
class Cliente:
    nome: str
    idade: int
    peso : float
    altura : float


    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        



lista_clientes = []

for i in range(4):
    dados_cliente = Cliente(nome=input("Digite seu nome: "), 
                 idade=int(input("Digite sua idade: ")), 
                 peso=float(input("Digite seu peso: ")) , 
                 altura=float(input("Digite sua altura: ")))
    lista_clientes.append(dados_cliente)
    
    
print("\nMostrando dados dos clientes.")
for cliente in lista_clientes:
    cliente.mostrar_dados()