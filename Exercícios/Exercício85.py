tempo=[]
par=[]
impar=[]
for conta in range(1, 8):
  num= int(input(f'Digite o {conta}º número: '))
  tempo.append(num)
  if num % 2 == 0:
    par.append(num)
  else:
    impar.append(num)
  par.sort()
  impar.sort()
print(f'a lista dos números são {tempo}')
print(f'Os números pares \nem ordem crescente são {par}')
print(f'Os números ímpares \nem ordem crescente são {impar}')