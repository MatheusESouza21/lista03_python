#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#  Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
vel = float(input('Qual a velocidade do seu carro? '))
if vel > 80:
    multa = (vel - 80) * 5
    print('Você foi multado em R$',multa,)
else:
    print('Você não foi multado')