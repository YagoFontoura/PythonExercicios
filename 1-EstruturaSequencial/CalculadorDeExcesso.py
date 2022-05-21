Quilos_Trazidos = int(input("Quantos quilos de peixe você trouxe?:"))
Maximo_Quilos = 50
Multa_Por_Quilo = 4
Excedente = Quilos_Trazidos - Maximo_Quilos
Total_a_Pagar = Excedente * Multa_Por_Quilo

print(f"O total a ser pago por {Excedente} Quilos excedente é de R${Total_a_Pagar} Reais.")
