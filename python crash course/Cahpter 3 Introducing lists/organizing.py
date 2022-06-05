cars = ['bmw', 'audio', 'toyota', 'subaru']
# cars.sort(reverse=True)
print('Here is the original list:')
print(cars)

print('Here is the sorted list:')
print(sorted(cars))

print('Here is the reverse')
cars.reverse()
print(cars)

print('the lenght of the list is '+str(len(cars)))

places = ['USA', 'Canada', 'Inglaterra', 'Suiza', 'Irlanda', 'Holanda']

print('Lugars que necesito visitar')
print(sorted(places))

print('Lugars que necesito visitar al reves')
print(sorted(places, reverse=True))

print('Lugars que necesito visitar listados originalmente')
print(places)

print('Lugars que necesito visitar listados al revez')
places.reverse()
print(places)

print('Lugars que necesito visitar listados al revez de nuevo')
places.reverse()
print(places)

print('Lista ordenada alfabeticamente')
places.sort()
print(places)

print('Lista ordenada alfabeticamente al revez')
places.sort(reverse=True)
print(places)

print('El numero de lugares que quiero visitar son :' + str(len(places)))
