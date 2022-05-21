from pickletools import float8


Temperatura_Em_Fahrenheit = float(input("Qual é a temperatura em Fahrenheit?: "))
Resultado_em_Celsius = 5 * ((Temperatura_Em_Fahrenheit - 32)/9)
print(f"Sua temperatura em Celsius é {Resultado_em_Celsius}")