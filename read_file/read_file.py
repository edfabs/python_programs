filename = 'read_file.txt'
number = 0
with open(filename) as f_obj:
    contents = f_obj.read()
    for line in contents:
        if line.isdigit() == True:
            number += int(line)

print(number)
f_obj.close()
