print("Este programa escribe el dia de la semana segun seleccione el usuario")
dia = int(input("Seleccione un día de la semana 1 - Lunes, 2 - Martes, 3 - Miercoles, 4 - Jueves, 5 - Viernes, 6 - Sabado, 7 - Domingo: "))
semana = {1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves", 5:"Viernes", 6:"Sabado", 7:"Domingo"}
if dia in semana:
    print(f"El dia de la semana es: {semana[dia]}")
else:
    print("Selección invalida")