import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro : str
    numero : int

@dataclass
class Pessoa:
    nome : str
    idade : int
    endereco : Endereco

    def mostrar_dados(self):
        print(f"Nome : {self.nome}")
        print(f"Idade : {self.idade}")
        print(f"Endereço : {self.endereco.logradouro}")
        print(f"Número do endereço : {self.endereco.numero}")

   

pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 idade= int(input("Digite sua idade:")),
                 endereco=Endereco(logradouro=input("Digite seu endereço:"), numero=int(input("Digite o número do seu endereço:"))))


pessoa1.mostrar_dados()

#Feito sem pesca po consulta e sem ultilizar ctrl c e ctrl v.

