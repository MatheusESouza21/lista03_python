#Peça ao usuário para inserir um número inferior a 20. Se ele inserir um número 20 ou mais, exiba a mensagem "Muito alto", caso contrário, exiba "Obrigado".
num = int(input('Insira um número inferior a 20: '))
if num < 20:
    print('Obrigado')
else:
    print('Muito alto')