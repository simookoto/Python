while True:
  n= int(input('digite um número \npara ver sua tabuada: '))
  if n < 0:
    break
  print('=='*7)
  for c in range(1, 11):
    print(f'  {n} x {c} = {n*c}')
  print('=='*7)
print('fim do pograma')