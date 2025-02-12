#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. (usar ELIF)
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
oper = input('Digite qual operação deseja fazer (+ - / *): ')
if oper == '+':
    print('O resultado da operaçâo é:', num1 + num2,'\nMatheus Eduardo')
elif oper == '-':
     print('O resultado da operaçâo é:', num1 - num2,'\nMatheus Eduardo')
elif oper == '*':
      print('O resultado da operaçâo é:', num1 * num2,'\nMatheus Eduardo')
elif oper == '/':
      print('O resultado da operaçâo é:', num1 / num2,'\nMatheus Eduardo')
