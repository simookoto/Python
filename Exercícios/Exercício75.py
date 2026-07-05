n= (int(input('digite o 1ª valor')), int(input('digite o 2ª valor')), int(input('digite o 3ª valor')), int(input('digite o 4ª valor')))
print(f'você digitou os valores {n}')
print(f'o valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
  print(f'o valor 3 apareceu na {n.index(3)+1}ª posição')
else:
  print('o 3 não foi digitado em nenhuma posição')
print('os valores pares digitados foram', end=' ')
for num in n:
  if num % 2 == 0:
    print(num, end=' ')
print('.')
print('fim do programa')