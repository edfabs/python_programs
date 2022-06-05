from cgi import print_environ


my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]
my_foods.append('cannoli')
friend_food.append('ice cream')
my_foods.append('ice cream')
# print('My favourite food are:')
print(my_foods)
# print('\nMy friend favorite food are:')
# print(friend_food)


print('The first three items of may favorite food are:')
print(my_foods[-3:])
