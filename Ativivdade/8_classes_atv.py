import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Cliente:
    nome: str
    cpf: str
    telefone : str

    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f" \nCPF: {self.cpf}")
        print(f" \nTelefone: {self.telefone}")
        


    def dados_sms_marketing(self):
        print(f"\n Telefone: {self.telefone}")

        

lista_clientes = []

for i in range(3):
    dados_cliente = Cliente (nome=input("Digite seu nome: "), 
                 cpf=(input("Digite seu CPF: ")), 
                 telefone=(input("Digite seu telefone: ")))
    lista_clientes.append(dados_cliente)

for cliente in lista_clientes:
    cliente.mostrar_dados()

print("Telefones pro marketing.")
for cliente in lista_clientes:
    cliente.dados_sms_marketing()