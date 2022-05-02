# Valores aleatórios com random
import random

print(random.random())  # Gera um valor de 0.0 a 1.0
print(random.uniform(1, 10))  # Gera um valor minimo ao Valor Maximo
print(random.randint(1, 10))


nomes = ['Helena', 'Alice', 'Laura', 'Maria Alice', 'Valentina',
         'Heloísa', 'Maria Clara', 'Maria Cecília', 'Maria Julia', 'Sophia']
print(random.choices(nomes))  # escolher opção aleátoria


print(random.shuffle(nomes))
print(nomes)
