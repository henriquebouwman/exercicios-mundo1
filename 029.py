v = int(input('Qual a velocidade atual do carro? '))
if v <= 80:
    print('\033[32mTenha um bom dia! Dirija com segurança!')
else:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('\033[31mVocê deve pagar uma multa de\033[m \033[33mR${:.2f}!'.format((v-80)*7))
    print('\033[32mTenha um bom dia! Dirija com segurança!')
