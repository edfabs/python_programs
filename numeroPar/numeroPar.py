num = int(input("Ingresa el numero a verificar: "))
def resultado(num, msj):
    print(f"El numero {num} es :{msj}")

if num % 2 == 0:
    resultado(num, "Par")
else:
    resultado(num, "Impar")
if num & 1 == 0:
    resultado(num, "Par")
else:
    resultado(num, "impar")