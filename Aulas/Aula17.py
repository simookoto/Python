'''num= [6, 9, 20, 4]
num[1]= 2
num[2]= 10
num.append(8)
num.sort()
num.insert(0, 0)
num.sort()
print(num)
print(f'nessa lista temos {len(num)} elementos.')'''
valores= []
#valores.append(5)
#valores.append(7)
#valores.append(3)
for contador in range(0, 5):
  valores.append(int(input('digite um valor: ')))
for cont, valor in enumerate(valores):
  print(f'na posição {cont} encontrei o valor {valor}! ')