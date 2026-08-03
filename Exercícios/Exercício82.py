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
for i, v in enumerate(numeros):
  if v % 2 == 0:
    pares.append(v)
  elif v % 2 == 1:
    impares.append(v)
print(f'os números na lista são {numeros}')
print(f'os números pares da lista são {pares}')
print(f'e os números ímpares são {impares}')