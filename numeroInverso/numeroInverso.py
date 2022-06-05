digitosig = 0
num = int(input("numero a invertir: "))
numero = 0
while num != 0:
    numero = 10*numero+num%10
    num//=10
print(numero)
