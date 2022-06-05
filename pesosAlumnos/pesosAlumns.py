n = 0
media = 0
pesoTotal = 0
active = True
n_40=0
peso_40 = 0
media_40 = 0
n_4050=0
peso_4050 = 0
media_4050 = 0
n_5060=0
peso_5060 = 0
media_5060 = 0
n_60=0
peso_60 = 0
media_60 = 0
print("Ingresa q si quieres salir del programa")
while (active):
    peso = int(input("Ingresa el peso del alumno: "))
    if(peso < 40):
        n_40 = n_40 + 1
        peso_40 = peso_40 + peso
        media_40 = peso_40 / n_40
    if(peso >= 40 and peso <50 ):
        n_4050 = n_4050 + 1
        peso_4050 = peso_4050 + peso
        media_4050 = peso_4050 / n_4050
    if(peso >= 50 and peso <60 ):
        n_5060 = n_5060 + 1
        peso_5060 = peso_5060 + peso
        media_5060 = peso_5060 / n_5060
    if(peso >= 60):
        n_60 = n_60 + 1
        peso_60 = peso_60 + peso
        media_60 = peso_60 / n_60

    n = n + 1
    pesoTotal = pesoTotal+peso
    media = pesoTotal / n
    print(f"El peso total  promedio de {n} Alumnos es {media}")
    print(f"El peso promedio de menos de 40kg de {n_40} Alumbnos es {media_40}")
    print(f"El peso promedio de 40kg a 50kg de  {n_4050} Alumbnos es {media_4050}")
    print(f"El peso promedio de 50kg a 60kg de {n_5060} Alumbnos es {media_5060}")
    print(f"El peso promedio de mas de 60kg de {n_60} Alumbnos es {media_60}")

    validate = input("¿Quieres seguir agregando peso de otro alumno? (yes/no): ")

    if validate == "no":
        active = False
    else:
        active = True
