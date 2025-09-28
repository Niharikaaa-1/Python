'''
Write a program to accept choice from user and print result 
S print Sunday
M print Monday
T print Tuesday
W print Wednesday
Th print Thursday
F print Friday
Sa Print Saturday
'''

choice = input("Enter choice (S, M, T, W, Th, F, Sa): ")

if choice == 'S':
    print("Sunday")
elif choice == 'M':
    print("Monday")
elif choice == 'T':
    print("Tuesday")
elif choice == 'W':
    print("Wednesday")
elif choice == 'Th':
    print("Thursday")
elif choice == 'F':
    print("Friday")
elif choice == 'Sa':
    print("Saturday")
else:
    print("Invalid choice")
