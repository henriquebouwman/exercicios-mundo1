sa = float(input('Qual o seu salário atual?'))
va = sa*(15/100)
sf = sa + va
print('O seu salário com o aumento saiu de R${:.2f} para R${:.2f}'.format(sa, sf))