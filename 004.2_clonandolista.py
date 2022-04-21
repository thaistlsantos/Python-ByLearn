# Clonar uma lista (passar os valores dela) para outra
# Quando trabalhamos com colchetes ([]) trabalhamos com os elementos da lista, e não com o objeto dela
# os dois [:] pontos vai copiar os elementos

lista_a = [1,2,3]
lista_b = lista_a[:]
lista_b.append(4)
print(lista_a)
print(lista_b)

lista_b = lista_a[:]
lista_b.append(5)
print(lista_a)
print(lista_b)
