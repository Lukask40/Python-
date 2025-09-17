import os
os.system("cls")

login_correto = "adm"
senha_correta = "123"

while True:
     login = input("Digite seu login: ")
     senha = input("Digite sua senha: ")

     if login == login_correto and senha == senha_correta:
       print("Login realizado com sucesso!")
       break
     
     else:
       print("login ou senha incorreto!")