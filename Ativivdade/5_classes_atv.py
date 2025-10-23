import os
from dataclasses import dataclass
os.system("cls")

# Estrutua de dados: classe.
@dataclass
class Cliente:
    nome: str
    email: str
    endereco : str
    

    def dados_entrega(self):
         print(f"Nome: {self.nome}")
         print(f"Endereço: {self.endereco}")

    def dados_email_marketing(self):
         print(f"Nome: {self.nome}")
         print(f"E-mail: {self.email}")
         


print("Solicitando os dados da  pessoa.")
Cliente1 = Cliente(nome = input("Digite seu nome: "),
                  email = input("Digite seu e-mail:"), 
                  endereco = input("Digite seu endereço: "))



print("\nExibindo dados de entrega.")
Cliente1.dados_entrega()
print("\nExibindo dados de e-mail de marketing.")
Cliente1.dados_email_marketing()




