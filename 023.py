num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade é {}, a dezena é {}, a centena é {} e a milhar é {}.'.format(u, d, c, m))