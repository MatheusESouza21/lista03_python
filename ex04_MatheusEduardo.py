#- Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", 
# caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor = input('Insira sua cor favorita: ')
if cor != 'vermelho' or 'VERMELHO' or 'Vermelho':
    print('Eu não gosto de', cor, ', eu prefiro vermelho\n Matheus Eduardo')
else:
    print('Eu também gosto de vermelho\n Matheus Eduardo')