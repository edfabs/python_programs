"""El programa captura una fecha haciendo validaciones"""
mes = int(input("Intruduzca un mes (1 para Enero, 2 para Febrero ...): "))
dia = int(input("Intoduzca un día del mes: "))
year = int(input("Introduce el año: "))
# print(type(mes))
# print(type(dia))
if type(mes) is int and type(dia) is int:
    True
else:
    print("El mes o el dia estan en formato incorrecto")
    quit()
if mes < 0 or mes > 12:
    print("El mes seleccionado es incorrecto")
    quit()

if year % 4 == 0 and year % 100 != 0 and mes == 2:
    if dia < 0  or dia > 29:
        print("El número seleccionado para día esta fuera de rango bisiesto")
        quit()
elif mes ==2 and (dia < 0  or dia > 28):
    print("El dia seleccionado es incorrecto")
    quit()

meses_31={1:"Enero", 3:"Marzo", 5:"Mayo", 7:"Julio", 9:"Agosto", 11:"Octubre", 12:"Diciembre"}
meses_30={2:"Febrero", 4:"Abril", 6:"Junio", 8:"Septiembre", 10:"Nobiembre"}

if mes in meses_31:
    if dia < 0  or dia > 31:
        print("El número seleccionado para día esta fuera de rango")
        quit()

if mes in meses_30:
    if dia < 0  or dia > 30:
        print("El número seleccionado para día esta fuera de rango")
        quit()


print(f"{dia}/{mes}/{year}")