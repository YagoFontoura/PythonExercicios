from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)


# quero escolher uma data
data_do_aniversario = datetime.strptime(
    input('Quando é seu aniversario ? :'), '%d/%m/%Y')

print(type(data_do_aniversario))

data_atual = datetime.now()
tempo = data_do_aniversario - data_atual
print(tempo.days)
