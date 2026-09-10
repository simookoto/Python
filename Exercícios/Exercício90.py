aluno={'pessoa': '', 'media': '',}
aluno['pessoa']= str(input('Nome do aluno: '))
aluno['media']= float(input(f'Média do/da {aluno['pessoa']}: '))
print('=='*15)
print(f'O aluno é {aluno['pessoa']}')
print(f'A média é {aluno['media']}')
if aluno['media'] < 6:
  print(f'A situação é de urgência, \nrecuperação obrigatória')
elif aluno['media'] == 6:
  print(f'A situação é de média, \nrecuperação opcional')
else:
  print(f'A situação é de acima da média, \nnão precisa de recuperação')
print('=='*15)