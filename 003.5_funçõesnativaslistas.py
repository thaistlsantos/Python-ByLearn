# Primeira função: append() => Insere um elemento no final na lista

numeros = ['um']
numeros.append("dois")
numeros.append("tres")
numeros.append("quatro")

print(numeros)


#Segunda função: index() => Retorna o índice de um determinado elemento

bylearners = ['Felipe','Alisson','Haynes','ByLearner <3']
#--Indices------ 0 ------- 1 ------ 2 -------- 3 --------
indice_haynes = bylearners.index('Haynes')

print(indice_haynes)

print(bylearners.index('ByLearner <3'))


# Terceira função: insert() => Inseri um elemento na lista em uma determinada posição

animais = ['Gato','Cachorro','Hamster']
animais.append('Furão')
print(animais)

animais = ['Gato','Cachorro','Hamster']
#------------0--------1---------2------
animais.insert(1,'Furão')
print(animais)


# Quarta Função: Remove => Remove um determinado elemento

animais.remove('Cachorro')
print(animais)


# Quinta Função: Pop => Remove um elemento em um determinado indice
# Pop interage com a lista, apenas removendo o elemento do indice enviado por parâmetro

animais = ['Gato','Furão','Cachorro','Hamster']
animais.pop(2)
print(animais)


# Sexta Função: Del => Remove um elemento em um determinado indice
# Remove o elemento passado por parâmetro (envio um elemento)

animais = ['Gato','Furão','Cachorro','Hamster']
del(animais[2])
print(animais)


# Sétima Função: Sort => Ordena os nossos números. 
# Também temos a função inter Sorted

lista = [2, 1, 4]
print(lista)
lista.sort()
print(lista)


lista = [2, 1, 4]
print(sorted(lista))


lista = [2, 1, 4]
print(lista.sort()) # Interage diretamente na lista... Não retorna nada
lista2 = lista.sort() # Não da para atribuir
print(lista2)

lista = ["c",'b','a']
print(sorted(lista)) # Sorted me retorna uma lista já ordenada
lista2 = sorted(lista) # Consigo atribuir a lista
print(lista2)


# Oitava Função: Len => Retorna o tamanho da lista

ls = ['t','e','s','t','e']
print(len(s))
5