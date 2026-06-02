somaidade= 0
mediaidade= 0
maioridadehomem= 0
nomevelho=''
totmulher20= 0
for p in range(1,5):
  print('====={}ª pessoa=====' .format(p))
  nome=str(input('nome: ')).strip()
  idade=int(input('idade: '))
  sexo=str(input('sexo [F/M]: '))
  somaidade += idade
  mediaidade= somaidade / 4
  if p == 1 and sexo in 'Mm':
    maioridadehomem= idade
    nomevelho= nome
  if sexo in 'Mm' and idade > maioridadehomem:
    maioridadehomem= idade
    nomevelho= nome
  if sexo in 'Ff' and idade < 20:
    totmulher20 += 1
print('a média de idade do grupo é de {:.1f} anos' .format(mediaidade))
print('o homem mais velho do grupo é {}, \n e tem {} anos' .format(nomevelho, maioridadehomem))
print('ao todo tem {} mulheres, \n com menos de vinte anos' .format(totmulher20))