salario=float(input('qual o salario atual do funcionario? R$'))
if salario<=1250:
  aumento1=salario+(salario*15/100)
  print('o salario passara a ser de {:.2f}' .format(aumento1))
else:
  aumento2=salario+(salario*10/100)
  print('o salario passara a ser {:.2f}' .format(aumento2))