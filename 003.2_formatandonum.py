# Podemos modificar a saídas dos números sem modificar os valores reais
# Ex: Número 2 => Valor é 2. Saída => 2.00 => Valor ainda é 2
# Número 2.5 => Valor é 2.5 Saída => 2 => Valor ainda é 2.5

numero = 1.61
print(numero)

# Para inteiros uso o 'd' e para floats uso o 'f'
# para numeros quebrados ele arredonda

print('{:.2f}'.format(numero))
print('{:.1f}'.format(numero))
print('{:.0f}'.format(numero))

print(f'{numero:.2f}')
print(f'{numero:.1f}')
print(f'{numero:.0f}')
