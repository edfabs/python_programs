computer = 'macintosh'

print("La computadora es macintosh")
print(computer == 'macintosh')

print("La computadora no es macintosh")
print(computer != 'macintosh')

computers = ['macintosh', 'hp', 'dell']

for computer in computers:
    if(computer == 'dell'):
        print(computer.lower())
    else:
        print(computer.title())

if('dell' in computers):
    print('Computers dell is in computers list')
else:
    print('compures dell is not in the compures list')

computer = 'macintosh'
print("\nI predict True")
print(computer == 'macintosh' and computer != 'dell')

number = 18
print("\n I predict True")
print((number == 18 or number > 10))
