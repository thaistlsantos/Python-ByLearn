#Manipulação de String

# Caractere é uma letra só
char = 'c'

# String é um 'conjunto' de carecteres
string_palavra = 'Felipe'
string_frase = 'Seja um ByLearner'

# Vetor (Array) => Sequencia de elementos do mesmo tipo
# String é um Vetor (array) de caracteres


string = "ByLearn"
#---------0123456
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])

#Strings são imutáveis

palavra = "teste"

nova_palavra = palavra[:2] + 'z' + palavra[3:]
print(nova_palavra)


palavra = 'abcdef'
print(palavra[-1])
print(palavra[-2])
print(palavra[:]) # print(palavra)

#Pesquisar em Strings

'b' in 'abc'

'd' in 'abc'

'b' not in 'abc'

'd' not in 'abc'

#Concatenar Strings (somar)

string = 'Fe' + 'Li' + 'Pe'
print(string)

print('Fe'+'li'+'pe')

#Alterar entre minúsculo e maiúsculo

string = 'Fe' + 'Li'.lower() + 'Pe'.lower()
print(string)

string = 'Felipe'.upper()
print(string)

#Tamanho da string


s = 'teste'
print(len(s))

#Checar se todos os caracteres são letras


print("abc".isalpha()) 
print("1fg".isalpha())
print("123".isalpha())
print("++;-/".isalpha())
#True
#False
#False
#False

#Remover espaços em branco tanto inicio quanto no fim


" sobrando espaços ".strip()

#'sobrando espaços'

'   sobrando espaços   '.strip()

#'sobrando espaços'

#Juntar os itens da string através de um delimitador


",".join("abc") # Aqui faz sentido

#'a,b,c'

" , ".join("abc") # Aqui faz sentido

#'a , b , c'

'|letra: '.join("abc") # Não faz sentido

#'a|letra: b|letra: c'


#Separar uma string através de um delimitador


s = "n o m e"

s.split()

#['n', 'o', 'm', 'e']


s = "n,o,m,e"
s.split(",")

#['n', 'o', 'm', 'e']

s = 'nome'
s.split()

#['nome']


#Listas dentro de listas
#Podemos criar quantas listas quisermos dentro de outras listas, 
# bastando o elemento ser também uma lista ( Utilizando as barras [] )


lista_dentro_de_lista = [[1,2],[3,4]]

lista_dentro_de_lista[0]
#[1, 2]

lista_dentro_de_lista[0][0]
#1

lista_dentro_de_lista[1][0]
#3

