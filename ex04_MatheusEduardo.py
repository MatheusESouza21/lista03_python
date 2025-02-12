#- Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", 
# caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor = input('Insira sua cor favorita: ')
(cor.lower())
if cor == 'vermelho':
    print('Eu também gosto de vermelho')
else:
    print('Eu não gosto de', cor,'eu prefiro vermelho')