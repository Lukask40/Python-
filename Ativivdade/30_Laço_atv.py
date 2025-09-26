import os
os.system("cls")

maior_salario = 0
menor_salario = 0
soma_salario = 0
soma_filhos = 0
total_familias = 0
primeira = True

while True:
    print("\nMenu:")
    print("1 - Adicionar família")
    print("2 - Sair e exibir resultados")
    opcao = int(input("Escolha: "))

    match opcao:
        case 1:
            salario = float(input("Digite o salário da família: "))
            filhos = int(input("Digite o número de filhos: "))

            total_familias += 1
            soma_salario += salario
            soma_filhos += filhos

            if primeira:
                maior_salario = salario
                menor_salario = salario
                primeira = False
            else:
                if salario > maior_salario:
                    maior_salario = salario
                if salario < menor_salario:
                    menor_salario = salario

        case 2:
            if total_familias > 0:
                media_salario = soma_salario / total_familias
                media_filhos = soma_filhos / total_familias

                print("\n--- RESULTADOS ---")
                print("a) Total de famílias:", total_familias)
                print(f"b) Média do salário: R$ {media_salario:.2f}")
                print(f"c) Média do número de filhos: {media_filhos:.2f}")
                print(f"d) Maior salário: R$ {maior_salario:.2f}")
                print(f"e) Menor salário: R$ {menor_salario:.2f}")
            else:
                print("Nenhuma família registrada.")
            break

        case _:
            print("Opção inválida!")
