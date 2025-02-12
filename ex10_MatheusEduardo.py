#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salario = float(input('Qual o seu salário? '))
if salario > 1250:
    nsalario = salario + (salario * 0.10)
    print('Seu aumento foi de R$', salario * 0.10,'e agora você receber R$', nsalario)
elif salario <= 1250:
    nsalario = salario + (salario * 0.15)
    print('Seu aumento foi de R$', salario * 0.15,'e agora você recebe R$', nsalario)