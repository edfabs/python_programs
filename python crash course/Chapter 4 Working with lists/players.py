players = ['charles', 'martina', 'michel', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("\nHere is the three players in my team")
for value in players[:3]:
    print(value.title())
