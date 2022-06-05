print('Progrma: Calculate the taxes of a salary depend of the number of days and tarifa ')
name = input('nombre del trabajador: ')
hours = int(input('Hours worked: '))
tarifa = int(input('What\'s the tarifa: '))
sbruto = 0
sneto = 0
print(f'nombre: {type(name)}, horas: {type(hours)}, tarifa: {type(tarifa)}, sbruto: {type(sbruto)}, sneto: {type(sneto)}')

if hours <= 35:
    sbruto = hours * tarifa
else:
    sbruto = 35 * tarifa + (hours - 35) * 1.5 * tarifa
if sbruto <= 2000:
    tax = 0
else:
    if sbruto > 2000 and sbruto <= 2220:
        tax = (sbruto - 2000) * 0.20
    else:
        tax = (220 * 0.20) + (sbruto - 2220) * 0.30
sneto = sbruto - tax
print(f'Worker: {name}, salario bruto: {sbruto}, salario neto: {sneto}')
