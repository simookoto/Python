'''teste= list()
teste.append('Daniel')
teste.append(15)
galera= list()
galera.append(teste[:])
teste[0]= 'Maria'
teste[1]= 20
galera.append(teste[:])
print(galera)'''

'''pessoal=[['Daniel', 15],['Natan', 14],['Pedro', 14],['Kauã', 15]]
#print(pessoal[2][1])
for pessoa in pessoal:
  print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')'''
pessoal= list()
dado= list()
for cont in range(0, 5):
  dado.append(str(input('nome: ')))
  dado.append(int(input('idade: ')))
  pessoal.append(dado[:])
  dado.clear()
  
print(pessoal)