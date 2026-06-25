opção= 0
numero=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze')
while True:
  opção= int(input('digite um número entre 0 ou 15: '))
  if 0 <= opção <= 15:
    break
  print('tente novamente. ', end='')
print(f'você escolheu o número {numero[opção]}')