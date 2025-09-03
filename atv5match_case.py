import os
os.system("cls")


valor= float(input("Digite o valor do produto: "))
print("Escolha a forma de pagamento")
print("1- pagamento a vista")
print("2- pagamento a prazo")
opcao = int(input("Opção: "))

match opcao:
    case 1:
        desconto = valor * 0.10
        total = valor - desconto
        print(f"\nvalor do produto: {valor:.2f}")
        print("Forma de pagamento: a vista")
        print(f"Valor do desconto: {desconto:.2f}")
        print(f"Total a pagar:R${total}")
    case 2:
        parcelas = float(input("Digite o número de parcelas (até 6): "))
        if 1 <= parcelas <= 6:
            valor_parcela = valor / parcelas
            print(f"\nvalor do produto: {valor:.2f}")
            print("Forma de pagamento: a prazo")
            print(f"Quantidade de parcelas: {parcelas:.2f}")
            print(f"Valor por parcela: {valor_parcela:.2f}")
            print(f"Total a pagar:R${valor:.2f}")
        else:
         print("Números de parcelas invalidos! Escolha entre 1 a 6.")
    case _:
        print("Opção invalida")
      
    


