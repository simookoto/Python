import random
a1=str(input('aluno um:'))
a2=str(input('aluno dois:'))
a3=str(input('aluno três:'))
a4=str(input('aluno quatro:'))
lista=[a1, a2, a3, a4]
random.shuffle(lista)
print('a ordem será:')
print(lista)