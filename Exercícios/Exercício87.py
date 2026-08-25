matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par= mai= socol= 0
for lin in range(0, 3):
  for col in range(0, 3):
   matriz[lin][col]= int(input(f'digite um valor para [{lin}, {col}]'))
print('=='*15)
for lin in range(0,3):
  for col in range(0, 3):
    print(f'[{matriz[lin][col]:^5}]', end='')
    if matriz[lin][col] % 2 == 0:
      par+= matriz[lin][col]
print()
print('=='*15)
print(f'a soma de todos os números pares é {par}')
for lin in range(0, 3):
  socol+= matriz[lin][2]
print(f'a soma dos números da terceira coluna é {socol}')
for col in range(0, 3):
  if col == 0:
    mai= matriz[1][col]
  elif matriz[1][col] > mai:
    mai = matriz[1][col]
print(f'o maior número da segunda linha é {mai}')