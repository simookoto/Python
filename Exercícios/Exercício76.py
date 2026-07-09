listagem= ('lápis', 2.00, 
'borracha', 1.50,
'caderno', 30.00, 
'caneta', 2.50, 
'lapiseira', 5.00, 
'estojo', 15.00, 
'corretivo', 4.50)
print('=='*13)
print(f'{"LISTA DE PREÇOS":^40}')
print('=='*13)
for pos in range(0, len(listagem)):
  if pos % 2 == 0:
    print(f'{listagem[pos]:.<30}', end='')
  else:
    print(f'R${listagem[pos]:>3.2f}')
print('=='*13)