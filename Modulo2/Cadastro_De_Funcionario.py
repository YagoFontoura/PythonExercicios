from datetime import datetime
import random


cartoes = ['R$50,00', 'R$250,00', 'R$120,00']

print('Bem vindo ao Sistema de Cadastro para novos funcionários.')
nome = input('Digite seu nome:')
idade = input('Digite sua idade: ')
data_registro = datetime.now()
cardReceive = random.choice(cartoes)

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_registro.day}/{data_registro.month}/{data_registro.year}.\n Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cardReceive}.')
