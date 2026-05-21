nota1=float(input('digite sua primeira nota: '))
nota2=float(input('digite sua segunda nota: '))
media= (nota1 + nota2) / 2
if media <= 5 and >= 6:
  print('sua média é {}, você está de recuperação' .format(media))
elif media >= 6:
  print('sua média é {}, você está aprovado' .format(media))
elif media <= 4:
  print('sua média é {}, você está reprovado' .format(media))