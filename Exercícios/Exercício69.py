tot18= totH= totM20= 0
while True:
  idade= int(input('idade: '))
  sexo=' '
  while sexo not in 'MF':
    sexo= str(input('sexo: [M/F]')).strip().upper()[0]
  if idade >= 18:
    tot18+= 1
  if sexo == 'M':
    totH+= 1
  if sexo == 'F' and idade < 20:
    totM20+= 1
  continuar= ' '
  while continuar not in 'SN':
    continuar= str(input('você quer continuar? [S/N]')).strip().upper()[0]
  if continuar == 'N':
    break
print(f'total de pessoas com mais de 18 anos: {tot18}')
print(f'ao todo temos {totH} homens cadastrados,')
print(f'e {totM20} mulheres com menos de 20 anos cadastradas.')