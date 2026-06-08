from time import sleep
n1=int(input('primeiro valor: '))
n2=int(input('segundo valor: '))
opçao= 0
while opçao != 5:
  print('''  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair''')
  opçao=int(input('>>>qual a sua escolha?<<< '))
  sleep(0.5)
  if opçao== 1:
    soma= n1 + n2
    print('a soma entre {} + {} = {}' .format(n1, n2, soma))
    print(' ')
    sleep(1)
  elif opçao== 2:
    multi= n1 * n2
    print('a multiplicação entre {} x {} = {}' .format(n1, n2, multi))
    print(' ')
    sleep(1)
  elif opçao== 3:
    if n1 < n2:
      print('o maior número é {}' .format(n2))
      print(' ')
      sleep(1)
    elif n2 < n1:
      print('o maior é {}' .format(n1))
      print(' ')
      sleep(1)
    else:
      print('eles são iguais')
      print(' ')
      sleep(1)
  elif opçao== 4:
    print('digite denovo os valores: ')
    n1=int(input('primeiro valor: '))
    n2=int(input('segundo valor: '))
  elif opçao== 5:
    print('encerrando...')
    sleep(2)
  else:
    print('opção inválida, tente novamente')
  print('-='*15)
print('fim do programa, volte sempre!')