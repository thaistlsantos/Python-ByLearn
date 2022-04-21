# Fatia funciona da seguinte maneira:

# Nós queremos da posição X até a posição Y
# Então nós queremos [X:Y] Ou seja... [Inicial : Final]
# Caso não tenha um dos valores na fatia, pegaremos TUDO daquele 'lado' Exemplo:
# Para lista[1:4] -> Pegamos elementos entre 1 e 4
# Para listas[:4] -> Pegamos elementos até 4
# Para listas[2:] -> Pegamos elementos a partir do 2

lista = [0,1,2,3,4,5,6,7,8,9,10]
primeiro_teste = lista[1:4] # Entre 1 e 4 (o que está no meio)
segundo_teste = lista[:4] # Até 4
terceiro_teste = lista[2:] # A partir de 2 (pega tudo)

print(primeiro_teste)
print(segundo_teste)
print(terceiro_teste)
