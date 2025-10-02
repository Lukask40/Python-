import os
os.system("cls")

lista_numero = []
soma = 0
qtd_negativo = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}ª número: "))
    lista_numero.append(numero)
    
    if numero < 0:
        qtd_negativo +=1
    else:
        soma += numero
    


for i in range(5):
    print(f"\nNúmero informado: {lista_numero[i]}")


print(f"Quantidade de números negativos: {qtd_negativo}")
print(f"Soma dos positivos: {soma}")



print("FIM")