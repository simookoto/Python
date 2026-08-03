numeros=[]
pares=[]
impares=[]
while True:
  numero=int(input('digite um número: '))
  numeros.append(numero)
  resposta=str(input('quer continuar? [S/N]')).strip().upper()
  while resposta not in ('S', 'N'):
    resposta=str(input('quer continuar? [S/N]')).strip().upper()
  if resposta == 'N':
    break
if numero % 2 == 0:
  pares.append(numero)
elif numero % 2 == 1:
  impares.append(numero)
print(f'os números na lista são {numeros}')
print(f'os números pares da lista são {pares}')
print(f'e os números ímpares são {impares}')