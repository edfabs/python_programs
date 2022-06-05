dia = int(input("Ingresa el dia (numerico): "))
mes = int(input("Ingresa el mes (numerico): "))
year = int(input("Ingrea el mes (Numerico): "))

if (dia <= 31 and mes <= 12):
    if dia == 31:
        dia = 1
        mes = mes + 1
        if mes > 12:
            mes = 1
            year = year + 1
    else:
        dia = dia + 1
    fecha = str(dia) +"/"+ str(mes) +"/"+ str(year)
    print(f"El día siguiente es: {fecha}")
else:
    print("Fecha imposible")