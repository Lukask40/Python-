import os
os.system("cls")


def calcular_media(lista_notas):
    return sum(lista_notas) / 2

def verificar_aprovacao():
    lista_notas = []
    for i in range(2):
        while True:
            nota = float(input(f"Digite a {i+1}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                lista_notas.append(nota)
                break
            else:
                print("Nota inválida! Digite entre 0 e 10.")
    media = calcular_media(lista_notas)
    print(f"A média é {media}")
    if media >= 7:
        print("Aprovado ")
    else:
        print("Reprovado ")

verificar_aprovacao()