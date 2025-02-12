#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
distancia = float(input('Qual distância você deseja percorrer? (KM/h) '))
if distancia <= 200:
    passagem = 0.50 * distancia
    print('O preço da passagem é R$',passagem,'\nMatheus Eduardo')
elif distancia > 200:
    passagem = 0.45 * distancia
    print('O preço da passagem é R$',passagem,'\nMatheus Eduardo')