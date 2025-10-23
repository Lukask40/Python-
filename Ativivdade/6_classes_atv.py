import os
from dataclasses import dataclass
os.system("cls")

# Estrutua de dados: classe.
@dataclass
class Cliente:
    nome: str
    email: str
    endereco : str
    

    def mostrar_dados(self):
         print(f"Nome: {self.nome}")
         print(f"E-mail: {self.email}")
         print(f"Endereço: {self.endereco}")
        

    def mostrar_somente_nome(self):
         print(f"Nome: {self.nome}")
         
         

print("Solicitando os dados da  pessoa.")


Cliente1 = Cliente(nome = input("Digite seu nome: "),
                  email = input("Digite seu e-mail:"), 
                  endereco = input("Digite seu endereço: "))
Cliente2 = Cliente(nome = input("Digite seu nome: "),
                  email = input("Digite seu e-mail:"), 
                  endereco = input("Digite seu endereço: "))



print("\nExibindo dados da 1ª pessoa.")
Cliente1.mostrar_dados()
print("\nExibindo dados da 2ª pessoa.")
Cliente2.mostrar_dados()
print("\nExibindo os nomes.")
Cliente1.mostrar_somente_nome()
Cliente2.mostrar_somente_nome()



# Outro jeito de fazer
# print("Solicitando os dados da pessoa.")
#  # Criando uma lista (vetor)
# lista_pessoas = []

# for i in range(2):
#   pessoa = Pessoa(nome=input("Digite seu nome: "),
#                  email=input("Digite seu e-mail: "),
#                  endereco=input("Digite seu endereço: "))
# lista_pessoas.append(pessoa)
# print("\n= Exibindo dados =")
# for pessoa in lista_pessoas:
#      pessoa.mostrar_dados()


# print("\n= Somente nomes =")
# for pessoa in lista_pessoas:
#      pessoa.mostrar_somente_nome()