sala=[]
while True:
  aluno= str(input('aluno: '))
  nota1= float(input('nota1: '))
  nota2= float(input('nota2: '))
  media= (nota1 + nota2) / 2
  sala.append([aluno, [nota1, nota2], media])
  cont= str(input('quer continuar? [S/N]'))
  if cont in 'Nn':
    break
print('=='*10)
print(f'               boletim')
print('=='*10)
for aluno in sala:
  print(f'aluno: {aluno[0]}      média: {aluno[2]}')
while True:
  busca= input('digite o nome do aluno \npara ver seus dados: \n[digite 999 para parar]')
  if busca == '999':
    break
  for aluno in sala:
    if aluno[0].lower() == busca.lower():
      print(f'aluno: {aluno[0]} notas: {aluno[1]} média:{aluno[2]}')