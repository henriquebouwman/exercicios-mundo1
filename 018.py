from math import radians, sin, cos, tan
an = float(input('Digite o valor do angulo: '))
ar = radians(an)
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangete é {:.2f}.'.format(sin(ar), cos(ar), tan(ar)))
