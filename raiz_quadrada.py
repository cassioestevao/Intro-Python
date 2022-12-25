from math import floor, sqrt #os importes são bem simples e intuitivos
num = int(input("Digite um numero :"))
raiz = math.sqrt(num)  #contem especificações da variavel, função propria pra raiz quadrada.
print("A Raiz de {} é igual a {}.".format(num,math.ceil(raiz))) #.format padrão como sempre. mas posso especificar o valor usando math.