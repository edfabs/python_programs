numero = mayor = 0
print("Programa que mantiene el numero mas grande, si deseas terminar el programa ingresa -99")
while numero != -99:
    numero = input("Ingresa un numero para evaluarlo: ")
    if numero < 0:
        print("Solo se permiten numeros positivos")
        continue
    else:
        if mayor < numero:
            mayor = numero
    print("El numero mas grande hasta el momento es: ", mayor)
print('Adios')
