# Copiando uma lista para outra (atribuindo o valor)
# A lista B passa a Referenciar a lista A, então, uma alteração na B também altera a A (e vice-versa)

lista_a = [1,2,3]
lista_b = lista_a
lista_b.append(4)

print(lista_a)
print(lista_b)
