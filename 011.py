a = float(input('Qual é a altura da parede?'))
l = float(input('Qual é a largura da parede?'))
ar = a * l
t = ar / 2
print('A quantidade de tinta que irá precisar para pintar uma parede de {} m² é de {:.2f} litros'.format(ar, t))
