trabalho_terminado = False

if trabalho_terminado == True:
    print('Bora dar uma saida')
else:
    print('Não terminei o trabalho ainda.')


numero_atrasos = 2
if numero_atrasos >= 3:
    print("Vá para diretoria")
elif numero_atrasos >= 2:
    print("você ja possui duas faltas, CUIDADO!")
elif numero_atrasos >= 1:
    print("Essa é sua primeira falta, vou reconsiderar.")
else:
    print("Pode entrar.")


velocidade = 55

if velocidade <= 50:
    print("Não foi multado")
elif velocidade >= 51 and velocidade <= 60:
    print("Levou multa de 2 pontos")
elif velocidade >= 61 and velocidade < - 75:
    print("Levou multa de 3 pontos ")
else:
    print("Levou multa de 7 pontos")
