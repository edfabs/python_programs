print("Programa qe determina el costo de n viaje dependiendo los dias del viaje y la distancia rcorrida")
dias = int(input("Ingresa el numero de días que durará tuu estancia: "))
distancia = int(input("Ingresa la distancia en km que rrecorreras en el viaje: "))
price = distancia * 2.5
if (dias > 7 and distancia > 800):
    price = price - (price * 0.3)
print(f"El precio del viaje es: {price}")
    