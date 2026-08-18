tempo=[]
princ=[]
mai= men= 0
while True:
 tempo.append(str(input('nome: ')))
 tempo.append(float(input('peso: ')))
 if len(princ) == 0:
    mai= men= tempo[1]
 else:
    if tempo[1] > mai:
      mai = tempo[1]
    if tempo[1] < men:
      men= tempo[1]
 princ.append(tempo[:])
 tempo.clear()
 resposta= str(input('quer continuar? [S/N] '))
 if resposta in 'Nn':
   break
print(f'ao todo foi  registrado {len(princ)} pessoas')
print(f'o maior peso foi de {mai}Kg,')
for pe in princ:
  if pe[1] == mai:
   print(f'o peso de {pe[0]}')
print(f'o menor peso foi {men}Kg')
for pe in princ:
  if pe[1] == men:
    print(f'o peso de {pe[0]}')