import os
os.system("cls")

# texto que desejo usar.
texto = input("Digite seu aequivo: ")


# Definir nome do arquivo para salvar.
nome_arquivo = "exemplo.txt"

# Comando para salvar.
with open(nome_arquivo, "a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")
    print("Salvo com sucesso!")


