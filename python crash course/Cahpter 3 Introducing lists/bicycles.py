bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1].title())
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

names = ['Joel', 'Titino', 'Efren', 'Sean', 'Gabe', 'Juan']

greetings = 'Muchas gracias '

print(greetings + names[0])
print(greetings + names[1])
print(greetings + names[2])
print(greetings + names[3])
print(greetings + names[4])
print(greetings + names[5])

transports = ['Corolita', 'Jetta', 'Bicicleta', 'Skate']

print('Me gusta mucho manejar el ' + transports[0] + ' aunque se que tengo que arreglarle la suspencion. El ' + transports[1] + ' era el mas nuevo pero dejo de serlo cuando lo eche a perder en un viaje. La ' +
      transports[2]+' me gusta mucho pero no tengo, lo que si tengo es '+transports[3]+' y me gusta aunque es un poco cansado andae en ella')

motocycle = ['honda', 'yamaha', 'suzuki']
print(motocycle)
motocycle.append('ducati')
print(motocycle)
motocycle.insert(0, 'triumph')
print(motocycle)

popped_motocycle = motocycle.pop()

print(popped_motocycle)
print(motocycle)

motocycle.remove('suzuki')

print(motocycle)


gest = ['jim morrison', 'steve jobs', 'jimmi hendrix']
invitation = 'Se le invita a formar parte de algo muy tribial y nada fuera de lo norma  a cenar'

print(gest[0].title() + ' ' + invitation)
print(gest[1].title() + ' ' + invitation)
print(gest[2].title() + ' ' + invitation)

gest_cant = gest.pop(1)
print(gest_cant.title() + ' lamentamos profundamente que no puedas asistir')

gest.append('Fabian Suchett')

print(gest)

print(gest[0].title() + ' ' + invitation)
print(gest[1].title() + ' ' + invitation)
print(gest[2].title() + ' ' + invitation)

gest.insert(0, 'Olallo Rubio')
gest.insert(2, 'Diego Ruzarin')
gest.append('Alfredo Jalife')

print(gest)

print('The invitations reduce to 2')

gest.pop(1)
gest.pop(2)
gest.pop(2)
gest.pop(2)

print(gest)

message = ' Uste sigue invitado a la cena'

print(gest[0].title() + message)
print(gest[1].title() + message)

del gest[0]
del gest[0]

print(gest)
