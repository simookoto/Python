valores= list()
while True:
  valor= int(input('digite um valor: '))
  if valor not in valores:
    valores.append(valor)
    print('valor adicionado com sucesso!')
  else:
   print('valor ja esxistente, não registrado')
  continuar= str(input('você quer continuar? [N/S]'))
  if continuar in 'Nn':
    break
valores.sort()
print('=='*13)
print(f'você digitou os valores {valores}')