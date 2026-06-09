n= cont= soma= 0
n= int(input('digite um número \n[999 para parar]: '))
while n != 999:
  soma+= n
  cont+= 1
  n= int(input('digite um número \n[999 para parar]: '))
print('você digitou {} números \ne a soma entre eles é {}' .format(cont, soma))