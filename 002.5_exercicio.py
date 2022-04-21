# Desafio Exercício 2.5
# Fazer uma função que subtraia quatro números entrados pelo usuário

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o primeiro número: "))
    num4 = float(input("Digite o segundo número: "))
    resp = num1 - num2 - num3 - num4
    print(
        f'O valor da subtração entre {num1}, {num2}, {num3} e {num4} é: ', resp)


main()
