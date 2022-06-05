days = {1:"Lunes", 2:"Martes",3:"Miercoles",4:"Jueves",5:"Viernes",6:"Sabado",7:"Domingo"}
day = int(input("Ingresa un día de la semana: "))
if day in days.keys():
    print(f"El día seleccionado es: {days[day]}")