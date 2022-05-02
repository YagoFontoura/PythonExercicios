frase = " Meu nome é Yago "
frase2 = "biblioteca"
frase3 = "Desenvolvimento De Aplicações"
print(frase.upper())  # deixa as letras maiusculas
print(frase.lower())  # deixa as letras minusculas
print(frase.strip())  # remove os espaçamentos da frase.
print(frase.lstrip())  # remove os espaçamentos da esquerda da frase
print(frase.rstrip())  # remove os espaçamentos da direita da frase.
# Procura uma palavra ou letra especifica e mostra o index
print(frase.find('Yago'))
# o replace faz a troca da palavra solicitada por outra escolhida
print(frase.replace('Yago', 'Roberta'))

print(frase2.index('o'))

indice_d = frase3.rindex('D')
indice_s = frase3.rindex('s')
print(frase3[indice_d:indice_s+1])
