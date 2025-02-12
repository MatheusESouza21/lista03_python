#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
renda = float(input('Digite a sua renda: '))
if renda <= 2259.20:
    print('Seu imposto de renda é: R$ 0.00\nMatheus Eduardo')
elif renda <= 2828.65:
    aliquota = renda * 0.75
    print('Seu imposto de renda é: R$', aliquota,'\nMatheus Eduardo')
elif renda <= 3751.05:
    aliquota = renda * 0.15
    print('Seu imposto de renda é: R$', aliquota,'\nMatheus Eduardo')
elif renda <= 4664.68:
    aliquota = renda * 0.225
    print('Seu imposto de renda é: R$', aliquota,'\nMatheus Eduardo')
elif renda > 4664.68:
    aliquota = renda * 0.275
    print('Seu imposto de renda é: R$', aliquota,'\nMatheus Eduardo')