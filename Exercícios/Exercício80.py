lista=[]
for c in range(0, 5):
  numero= int(input('digite um valor: '))
  if c == 0 or numero > lista[len(lista)-1]:
    lista.append(numero)
    print('adicionado no final da lista...')
  else:
    pos= 0
    while pos < len(lista):
      if numero <= lista[pos]:
        lista.insert(pos, numero)
        print(f'adicionado na posição {pos} da lista...')
        break
      pos += 1
print('=='*15)
print(f'os valores digitados em ordem foram {lista}')