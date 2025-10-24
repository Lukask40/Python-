import os
os.system("cls")
from dataclasses import dataclass



@dataclass
class Endereco:
    logradouro : str
    numero : int
    cidade : str

@dataclass
class Cliente:
    nome: str
    email: str
    endereco :  Endereco

    def mostrar_dados(self):
        print("\nMostrando dados do cliente.")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco.logradouro}")
        print (f"Número: {self.endereco.numero}")
        print (f"Cidade: {self.endereco.cidade}")


  


cliente1 = Cliente(nome=input("Digite seu nome: "), 
                   email=input("Digite seu e-mail: "),
                    endereco=Endereco(logradouro=input("Digite o seu logradouro: "), 
                                      numero=int(input("Digite o número do logradouro: ")), 
                                      cidade=input("Digite a sua cidade: ")))

cliente1.mostrar_dados()


