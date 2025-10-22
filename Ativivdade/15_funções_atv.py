import os
os.system("cls")


def calcular_imc(peso, altura):
    return peso / (altura ** 2) # = (altura * altura)

def verificar_classificacao(imc):
    if imc < 18.5:
        return "Abaixo do peso \nrecomendação: consulte um nutricionista para orientação. "
    elif imc < 24.9:
        return "Peso normal \nrecomendação: Mantenha hábitos saudáveis!. "
    elif imc < 29.9:
        return "Sobrepeso \nrecomendação: considere uma dieta balanceada e atividade física. "
    elif imc < 34.9:
        return "Obesidade grau 1 \nrecomendação: procure orientação de um profissional de saúde. "
    elif imc < 39.9:
        return "Obesidade grau 2 \nrecomendação: consulte um médico para avaliação e orientação. "
    else:
        return "Obesidade grau 3 \nrecomendação: busque assistência médica imediatamente. "

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = calcular_imc(peso, altura)
classificacao = verificar_classificacao(imc)

print("\n= Exibindo resultados=")
print(f"\nSeu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")
