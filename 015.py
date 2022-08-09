km = float(input('Quantos Km rodados?'))
d = int(input('Quantos dias alugados?'))
pkm = km * 0.15
pd = d * 60
pf = pkm + pd
print('O total a pagar é de R${:.2f}'.format(pf))