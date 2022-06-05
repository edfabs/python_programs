print("Programa que calcula jornal diario de un trabajador")
print("Selecciona el dia laborado")

def error():
    print("Valor seleccionado invalido")

d = int(input("1 - Lunes, 2 - Martes, 3 - Miercoles, 4 - Jueves, 5 - Viernes, 6 - Sabado, 7 - Domingo: "))
dias = {1 : "Lunes", 2 : "Martes", 3 : "Miercoles", 4: "Jueves", 5: "Viernes", 6: "Sabado", 7: "Domingo"}
bono = 0
factor = 5
paga = 0
h = 0
if d in dias:
    horario = int(input("Selecciona un horario para Diurno selecciona 1, para Nocturno selecciona 2: "))
    if (horario == 1 or horario == 2):
        h = int(input("Ingresa el numero de horas trabajadas: "))
        if horario == 1:
            if d == 7:
                factor = factor + 2
        if horario == 2:
            factor = 8
            if d == 7:
                factor = factor + 3
        paga = h * factor
        print(f"El suelgo por jornada es {paga}")
    else:
        error()
else:
    error()

