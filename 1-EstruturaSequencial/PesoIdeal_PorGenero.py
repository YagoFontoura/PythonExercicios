Altura = float(input("Qual é a sua altura?: "))
Genero = input("Qual é seu Genero, Masculino ou Feminino ?: ")

Peso_ideal_Masculino = (72.7 * Altura) - 58
Peso_ideal_Feminino = (62.1 * Altura) - 44.7


if Genero == "Masculino" or Genero == "masculino":
    print(f"Seu peso ideal é {Peso_ideal_Masculino}")
elif Genero == "Feminino" or Genero == "feminino":
    print(f"Seu peso ideal é {Peso_ideal_Feminino}")

else:
    print(f"Genero indefinido.")
