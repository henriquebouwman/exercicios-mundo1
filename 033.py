print('Digite três valores qualquer para saber qual o maior e o menor:')

n1 = float(input('Primeiro número:'))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))

'''n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))'''
