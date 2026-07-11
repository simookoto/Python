import random
import math
print('-=-'*5)
print('recaptcha')
print('-=-'*5)
print('captcha:')
print('[1] para robô')
print('[2] humano')
computador=[25, 49, 144, 16, 36]
random.shuffle(computador)
raiz= computador 
print(' ')
robo=int(input('>>>'))
if robo== 1:
  print('robô vagabundo')
elif robo== 2:
  teste=int(input('qual a raiz quadrada de {}? ' .format(computador)))
  if teste== raiz:
    print('você é um robô! adeus')
  elif teste != raiz:
    print('você é um humano')
else:
  print('error 404!')