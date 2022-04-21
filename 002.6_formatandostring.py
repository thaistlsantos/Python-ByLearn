# Formatando com o format:

from ast import NodeVisitor


numero = 10
letra = 'a'
palavra = 'ByLearn'


print("meu número vale {}, minha letra vale {}, minha palavra vale {}".format(numero,letra,palavra))


# São strings começadas com f antes das aspas.  
# Nelas colocamos o valores das variaveis dentro das {}  

dia = int(28)
mes = str('Nov')
niver = str('Thais')
print(f'Meu dia é: {dia}, meu mês é: {mes}, Aniversariante é:  {niver}')