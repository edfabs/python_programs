i = 1
par = impar = 0
for i in range(201):
    if(i % 2 == 0):
        par = par + i
    else:
        impar = impar + i
print "La suma de los numeros pares es: ", par
print"La suma de los numeros impares es: ", impar
