Valor_Hora_Trabalhada = int(input("Quanto você ganhar por dia?"))
Horas_Trabalhada = int(input("Quantas horas você trabalha por mes ?"))
Salario_Bruto = Horas_Trabalhada * Valor_Hora_Trabalhada

imposto_de_renda = Salario_Bruto * 0.11
inss = Salario_Bruto * 0.08
Sindicato = Salario_Bruto * 0.05
Desconto_Total = imposto_de_renda + inss + Sindicato

Valor_Liquido = Salario_Bruto - Desconto_Total



print(f"Seu salario bruto é de {Salario_Bruto}")
print(f"Você pagou {inss} para o INSS")
print(f"Você pagou {Sindicato} para o Sindicado")
print(f"O recebeu {Valor_Liquido} Liquido do Salario")

