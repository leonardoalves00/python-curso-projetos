from math import sin, radians, cos, tan

angulo = float(input('digite o angulo'))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangete = tan(radians(angulo))

print('O angulo e {} tem o seno de {:.2f}'.format(angulo, seno))
print('O angulo e {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O angulo e {} tem o tangente de {:.2f}'.format(angulo, tangete))
