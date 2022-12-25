velocidade = float(input("Qual é a velocidade do carro? "))
if velocidade > 80:
    print("Você foi multado! o limite permitido é 80 km\h")
    print("A sua multa é de $10,00 a cada km")
    multa = (velocidade - 80) * 10
    print("\033[31mA sua multa foi de $ {:.2f}.".format(multa))
    
else:
    print("Siga com segurança")