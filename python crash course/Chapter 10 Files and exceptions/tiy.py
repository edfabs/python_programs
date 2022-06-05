# “10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . .. Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.”

# “10-2. Learning C: You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:”

# file = 'learning_python.txt'
# with open(file) as file_object:
#     content = file_object.readlines()

# for loop in range(3):
#     print(loop)
#     for line in content:
#         line.strip()
#         print(line.replace('Python', 'C').strip())

# “10-3. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.”

# name = input("What's your name?")
# file = 'guest.txt'
# with open(file, 'a') as file_object:
#     file_object.write(f"{name}\n")


# “10-4. Guest Book: Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.”


# print("(This progrma register your visit, type 'q' to out of progrma )")
# while True:
#     name = input("Please enter your name!")
#     if name == 'q':
#         break
#     elif name != '':
#         file = 'guest_book.txt'
#         with open(file, 'a') as file_object:
#             file_object.write(f"{name} \n")
#         print(f"{name.title()} Thank you for visit this place")

# “10-5. Programming Poll: Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.”

# print("(This program is a poll, if you want to out type 'q')")
# while True:
#     name = input("What is your name?")
#     answer = input("Why you like programming?")
#     if name == 'q' or answer == 'q':
#         break
#     elif name != '' and answer != '':
#         file = 'programming_poll.txt'
#         with open(file, 'a') as file_object:
#             file_object.write(f"name: {name.title()} - answer : {answer}\n")
#         print(f"Thank you to answer the poll!")

# “10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

# “10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.”

# print("Givem a two numbers and I divide them (press 'q' to out of progrma)")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number:")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Don't can divide for cero")
#     except ValueError:
#         print("One of the two values or both are incorrect")
#     else:
#         print(answer)

# “10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.”

# “10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if ”

# filenames = ["cats.txt", "dogs.txt"]

# for file in filenames:
#     try:
#         with open(file) as f:
#             print(f"\nfilename: {file}")
#             print(f.read().strip())
#     except FileNotFoundError:
#         #print(f"the file {file} not found")
#         pass

# “10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:”

filename = 'alice_in_wonderland.txt'
with open(filename) as f:
    print(f.read().lower().count('the '))


# “10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file. Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”

# 10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.”

# 10-11 and 10-12 in the favorite_number.py file

# “10-13. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.” “Before printing a welcome back message in greet_user(), ask the user if this is the correct username. If it’s not, call get_new_username() to get the correct username.”
