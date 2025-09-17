import os
os.system("cls")

login_correto = "adm"
senha_correta = "123"

while True:
    for i in range(3):
        print(f"\nTentativas: {i+1}")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login == login_correto and senha == senha_correta:
            print("Login realizado com sucesso!")
            break
        else:
            print("Login ou senha incorretos!" \
            "")
    break
            
        