def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).

    :param peso: Peso em quilogramas (kg).
    :param altura: Altura em metros (m).
    :return: Valor do IMC.
    """
    if peso <= 0 or altura <= 0:
        return "Peso e altura devem ser valores positivos."

    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    """
    Interpreta o valor do IMC de acordo com a classificação padrão.

    :param imc: Valor do IMC.
    :return: String com a interpretação do IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Entrada de dados
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcular o IMC
resultado_imc = calcular_imc(peso, altura)

# Interpretar o IMC
interpretacao = interpretar_imc(resultado_imc)

# Exibir resultados
print(f"Seu IMC é: {resultado_imc:.2f}")
print(f"Classificação: {interpretacao}")
