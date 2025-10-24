import os
from dataclasses import dataclass
os.system("cls")


#Criando uma classe.

 # Cliente é uma pessoa?
 # CPF? Endereço? Nome? Título de eleitor? E-mail? Telefone?
 # Seu sistema precisa de algumas informações.
 # Uma venda.
 # Endereço, nome, telefone. (Mini-mundo)


@dataclass
class Cliente:
    nome: str
    endereco: str
    telefone : str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")

#Criando dois clientes com as características
#definidas na classe.

lista_clientes = []

for i in range(3):
    dados_cliente = Cliente (nome=input("Digite seu nome: "), 
                 endereco=(input("Digite seu endereço: ")), 
                 telefone=(input("Digite seu telefone: ")))
    lista_clientes.append(dados_cliente)

for cliente in lista_clientes:
    cliente.mostrar_dados()
    
                 
