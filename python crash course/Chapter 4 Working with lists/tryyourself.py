million = []
for value in range(1, 10):
    million.append(value)
print(max(million))
print(min(million))
print(sum(million))

odd_list = list(range(1, 21, 2))
print(odd_list)

threes = list(range(3, 31, 3))
print(threes)

cube = []
for value in range(1, 11):
    cube.append(value**3)
# print(cube)


cube_comprehension = [value**3 for value in range(1, 11)]
# print(cube_comprehension)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]
my_foods.append('cannoli')
friend_food.append('ice cream')
my_foods.append('ice cream')

# print('The first three items of may favorite food are:')
# print(my_foods[-3:])


pizzas = ['Chesee', 'Hawaiana', 'Italianis', 'Peperoni', 'Chili']
friend_pizzas = pizzas[:]
pizzas.append('Al pastor')
pizzas[5] = 'Alpastor'
friend_pizzas.append('De carne')
print('My favorite pizzas are:' + str(pizzas))
print('The pizzas of my friend are: '+str(friend_pizzas))


print('My food: ')
for value in my_foods:
    print(value)
print('\nFood of my friend: ')
for value in friend_food:
    print(value)

# tuples

food = ('sopa', 'enchiladas', 'pambazos', 'chilaquiles', 'chiles rellenos')
print('Restaurante offer the fologin dishes:')
for value in food:
    print(value)

food = ('sopa azteca', 'enchiladas', 'pambazos',
        'chilaquiles', 'chiles en hogada')
print('\nRestaurante offer the fologin dishes:')
for value in food:
    print(value)
