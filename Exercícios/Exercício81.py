numeros=[]
while True:
  numero=int(input('digite um número: '))
  numeros.append(numero)
  resposta=str(input('quer continuar? [S/N] ')).strip().upper()
  while resposta not in ('S', 'N'):
    resposta=str(input('opção inválida. quer continuar? [S/N] ')).strip().upper()
  if resposta == 'N':
    break
totalnumeros= len(numeros)
print(f'você digitou {totalnumeros} números')
numeros.sort(reverse=True)
print(f'os números em \nordem decresente fica {numeros}')
if 5 in numeros:
  print('o número 5 faz parte da lista')
else:
  print('o número 5 não faz parte da lista')