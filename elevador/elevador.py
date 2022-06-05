"""Es elevador el programa"""

nivel = 0
max = 25
min = 0
msg = ''
btnUp = 0
btnDown = 0

while(msg != 'quit'):
    msg = input("Escribe 'quit' para salir")
    print(f"Estas en el nivel {nivel}")
    if nivel == 0:
        btn = int(input("Ingresa 1 para subir un nivel: "))
    elif nivel == 25:
        btn = int(input("Ingresa 2 para bajar un nivel: "))
    else:
        btn = int(input("Ingresa 1 para subir un nivel o 2 para bajar un nivel: "))
    if btn == 1 and nivel < 26:
        nivel = nivel + 1
    if btn == 2 and nivel > 0:
        nivel = nivel - 1
    elif btn != 1 and btn != 2:
        btn = 0
    print(f"El llegaste al nivel {nivel}")
    