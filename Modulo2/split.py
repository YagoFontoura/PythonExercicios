frase = 'Olá, bem-vindo a este treinamento'

print(frase.split())
print(frase.split(','))
print(frase.split('-'))

nomes = 'jhonatan, rafael, carol, amanda, jefferson'
print(nomes.split())
print(nomes.split(','))

hashtags = 'music #guitar #gamer #coder # python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))

hashtag_separadas_por_espaco = hashtags.split(' ')
print(hashtag_separadas_por_espaco)
print(','.join(hashtag_separadas_por_espaco))
print('.'.join(hashtag_separadas_por_espaco))
print(' '.join(hashtag_separadas_por_espaco))


# DESAFIO

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'

palavras1 = frase1.split(' ')
palavras2 = frase2.split(',')

print(','.join(palavras1))
print('&'.join(palavras2))
