import os
os.system("cls")

lista_numero = []



for i in range(5):
    numero = int(input(f"Digite o {i+1}ª número: "))
   
    
    if numero < 0:
        lista_numero.append(0)
    else:
     lista_numero.append(numero)
    
    


print(f"valore do vetor {lista_numero}")


print("FIM")