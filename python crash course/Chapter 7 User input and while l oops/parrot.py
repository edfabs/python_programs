# message = input("Tell me something, and I will repeat in back to you:")
# print(message)

# using while loop

prompt = "\nTell me something, and I will repeat in back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
active = True
while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
    else:
        active = False
