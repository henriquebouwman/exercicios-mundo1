# co = float(input('Qual o valor do cateto oposto? '))
# ca = float(input('Qual o valor do cateto adjacente? '))
# h = (co **2 + ca **2) ** (1/2)
# print('O valor da hipotenusa é {:.2f} .'.format(h))
from math import hypot
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
h = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}. '.format(h))