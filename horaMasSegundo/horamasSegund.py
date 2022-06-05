print("programa que suma un segundo a la hora ingresada")
h = int(input("Ingresa la hora: "))
m = int(input("ingresa los minutos: "))
s = int(input("Ingresa los segundos: "))
def formato(var):
    r = ''
    if var < 10:
        r = '0'+ str(var)
    return r
if(h < 24 and m < 60 and s < 60):
    s = s + 1
    if(s == 60):
        s = 0
        m = m +1
        if(m == 60):
            m = 0
            h = h + 1
            if(h == 24):

                h = 0
hh = formato(h)
mm = formato(m)
ss = formato(s)
print(f"La hora calculada es: {hh}:{mm}:{ss}")
