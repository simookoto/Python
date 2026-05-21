not1=float(input('digite sua primeira nota:'))
not2=float(input('digite sua segunda nota:'))
media= (not1 + not2) / 2
if media => 5:
  print('sua média é {}, você está de recuperação' .format(media))
elif media =< 6:
  print('sua média é {}, você está aprovado' .format(media))
elif media => 3:
  print('sua média é {}, você está reprovado' .format(media))