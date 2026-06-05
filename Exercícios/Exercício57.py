s=str(input('digite seu sexo: [M/F]')).strip().upper()[0]
while s not in 'MmFf':
  s=str(input('dados inválidos. \n por favor informe seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso!'.format(s))