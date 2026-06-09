print('-=-'*5)
print('recaptcha')
print('-=-'*5)
print('captcha:')
print('[1] para robô')
print('[2] humano')
print(' ')
robo=int(input(''))
if robo== 1:
  print('robô vagabundo')
elif robo== 2:
  teste=int(input('qual a raiz quadrada de 144? '))
  if teste== 12:
    print('você é um robô! adeus')
  elif teste != 12:
    print('você é um humano')
else:
  print('error 404!')