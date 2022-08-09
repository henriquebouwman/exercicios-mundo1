salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario + (salario*10/100)))
else:
    print('Quem ganhava \033[33mR${:.2f}\033[m passa a ganhar \033[1:32mR${:.2f}\033[m agora.'.format(salario, salario + (salario*15/100)))
