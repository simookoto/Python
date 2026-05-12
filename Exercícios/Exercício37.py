número=int(input('digite um número inteiro'))
print('=='*10)
print('digite um dos 3 números')
print('  abaixo para converter:')
print('=='*10)
print('[1] binário')
print('[2] octal')
print('[3] hexadecimal')
escolha=int(input('sua opção:'))
if escolha== 1:
  print('{} convertido para BINÁRIO é {}' .format(número, bin(número)[2:]))
elif escolha== 2:
  print('{} convertido para OCTAL é {}' .format(número, oct(número)[2:]))
elif escolha== 3:
  print('{} convertido para HEXADECIMAL é {}' .format(número, hex(número)[2:]))
else:
  print('{} é INVALIDO!' .format(escolha))