print("Programa que ordena dos numeros ingresados por el usuario")
a = int(input("Ingresa el primer numero a ordenar: "))
b = int(input("Ingresa el segundo numero a ordenar: "))
list = []
if(a > b):
    list.append(a)
    list.append(b)
else:
    list.append(b)
    list.append(a)
print(f"El orden de lo numeros es la siguiente: {list}")