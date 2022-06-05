from cmath import pi


file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# print(float(pi_string))
# print(len(pi_string))

file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    pi_string += (line.strip())
print(f"\n{pi_string[:52]}...")

birthday = input(
    "Entrt you birthday 'mmddyy' to know if appear in the pi_string")

if birthday in pi_string:
    print('Your birthday appers in the first million digits of pi')
else:
    print("Your birthday does not appers in the first million digits of pi")
