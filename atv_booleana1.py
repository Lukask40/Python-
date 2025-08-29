import os
os.system("cls")

login_salvo = "Lucas"
senha_salva = "123"

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == login_salvo and senha == senha_salva:
    print("Bem vindo")
else:
    print("Login ou senha incorretos")