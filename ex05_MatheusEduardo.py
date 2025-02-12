#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando. 
# Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva". 
# Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
resposta = input('Está chovendo? ')
(resposta.lower())
if resposta == 'sim':
    resposta2 = input('Está ventando? ')
    (resposta2.lower())
    if resposta2 == 'sim':
        print('Está ventando muito para um guarda-chuva\nMatheus Eduardo')
    else:
        print('Pegue um guarda-chuva\nMatheus Eduardo')
else:
    print('Aproveite seu dia\nMatheus Eduardo')