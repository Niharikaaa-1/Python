'''
Write a program to accept characters  from user and print characters are in capital 
 or small letter
'''
char = input("Enter a character: ")
if char.isupper():
    print(f"{char} is a capital letter.")
elif char.islower():
    print(f"{char} is a small letter.")
else:
    print("Invalid input. Please enter an alphabetic character.")
