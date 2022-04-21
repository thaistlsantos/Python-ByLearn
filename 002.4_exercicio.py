# Desafio Exercício 2.4
# Fazer uma função que divida dois números entrados pelo usuário

def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resp = num1 / num2

    print("O tipo de A é: ", type(num1))
    print("O tipo de B é: ", type(num2))

    print('O valor da divisão entre {} e {} é: {}'.format(num1, num2, resp))


main()
