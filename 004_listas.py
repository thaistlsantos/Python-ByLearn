# Motivação das listas: Trabalhar com vários valores relacionados em uma só variável

# Todos os possiveis alunos
# Felipe, Alisson, Haynes, ByLearner
# As notas respectivas dos alunos
# 8 e 10, 10 e 7, 8 e 9, 10 e 10

# Media de [Primeiro Aluno] = [Notas do 1º] / 2
# Para todos -> Media do [Atual] = [Notas do Atual] /2

def main():
    primeira_lista = ['Felipe', 'Alisson', 'Haynes', 'ByLearner']
    # ------Posição------ 1º ------ 2º ------- 3º ------ 4º ------
    # ------Índice--------0---------1----------2---------3--------

    print(primeira_lista[0])
    print(primeira_lista[1])
    print(primeira_lista[2])
    print(primeira_lista[3])

    primeira_lista.append('Thais')

    print(primeira_lista)
    qtd = len(primeira_lista)
    print("Sua lista possui : ", qtd, "elementos")


main()

# Métodos alternativos de criar listas

lista = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c']
lista3 = ['a', 'b', 2, 3]
lista_alunos = []

print(lista, lista2, lista3, lista_alunos)


# Funções built in são funções externas

lista_built_in = list()  # equivale a lista = []
variavel_para_lista = 12
lista_built_in_cheia = list(['a', 2, variavel_para_lista])

print(lista_built_in_cheia)
