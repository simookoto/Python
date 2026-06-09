from random import randint
computador= randint(64, 4, 144, 25, 36, 49)
print('-=-'*5)
print('recaptcha')
print('-=-'*5)
print('captcha:')
print('[1] para robô')
print('[2] humano')
print(' ')
robo=int(input(''))
raiz= computador ** (0.5)
 while robo != 1 or robo != 2: 
  if robo== 1:
    print('robô vagabundo')
  elif robo== 2:
    teste=int(input('qual a raiz quadrada de {}? ' .format(computador)))
  if teste== raiz:
    print('você é um robô! adeus')
  elif teste != raiz:
    print('você é um humano')
