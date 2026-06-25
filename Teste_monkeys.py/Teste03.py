escolha= 0
cardapio=('hamburguer [0]', 'monster [1]', 'suco [2]', 'pizza [3]', 'pudim [4]', 'bolo de chocolate [5]')
#print(len(cardapio))
for comida in cardapio:
  print(f'{comida}')
print(' ')
while True:
  escolha= int(input('escolha  um número: '))
  if 0 <= escolha <= 6:
    break
print('você escolheu o', (cardapio[escolha]))
print('bom apetite!')