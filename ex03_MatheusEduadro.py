#Peça ao usuário para inserir um número entre 10 e 20 (inclusive). Se ele inserir um número dentro desse intervalo,
# exiba a mensagem "Obrigado", caso contrário, exiba a mensagem "Resposta incorreta".
num = int(input('Insira um número entre 10 e 20: '))
if num >= 10 and num <= 20:
    print('Obrigado \nMatheus Eduardo')
else:
    print('Resposta incorreta \nMatheus Eduardo')