'''Write a program to Design a app for Movie Ticket Booking
a.First Accept Choice of Seat(Classic @ Rs100 / Premium @ Rs300 / Recliner @ Rs500)
b. Accept Number of Seats
c. Now according to Amount provide offers
i. Amount between 500 to 1500 
offers include (choice of a Meal worth Rs200 or 2% Discount)
ii. Amount More than 1500 
offers include (choice of a Meal worth Rs500 or 4% Discount)
'''

print("Welcome to Movie Ticket Booking❤️")
print("Available Seat Types:")
print("1. Classic @ Rs100")
print("2. Premium @ Rs300")
print("3. Recliner @ Rs500")

seat_type = int(input("Enter choice of Seat (1/2/3): "))
if seat_type == 1:
    seat_price = 100
    seat_type_name = "Classic"
elif seat_type == 2:
    seat_price = 300
    seat_type_name = "Premium"
elif seat_type == 3:
    seat_price = 500
    seat_type_name = "Recliner"
else:
    print("Invalid choice of seat type.")
    exit()
    
num_seats = int(input("Enter number of seats: "))

total_amount = seat_price * num_seats
print(f"Total amount for {num_seats} {seat_type_name} seats: Rs{total_amount}")
if 500 <= total_amount <= 1500:
    print("You are eligible for an offer!")
    offer_choice = input("Choose your offer - Meal worth Rs200 (M) or 2% Discount (D): ").upper()
    if offer_choice == 'M':
        print("You have chosen a Meal worth Rs200.")
        final_amount = total_amount
    elif offer_choice == 'D':
        discount = total_amount * 0.02
        final_amount = total_amount - discount
        print(f"You have chosen a 2% Discount. Discount Amount: Rs{discount:.2f}")
    else:
        print("Invalid offer choice.")
        final_amount = total_amount
elif total_amount > 1500:
    print("You are eligible for an offer!")
    offer_choice = input("Choose your offer - Meal worth Rs500 (M) or 4% Discount (D): ").upper()
    if offer_choice == 'M':
        print("You have chosen a Meal worth Rs500.")
        final_amount = total_amount
    elif offer_choice == 'D':
        discount = total_amount * 0.04
        final_amount = total_amount - discount
        print(f"You have chosen a 4% Discount. Discount Amount: Rs{discount:.2f}")
    else:
        print("Invalid offer choice.")
        final_amount = total_amount
else:
    final_amount = total_amount
    print("No offers available for the selected amount.")
  
print(f"Final amount to be paid: Rs{final_amount:.2f}")
print("Thank you for booking with us! Enjoy your movie!🎬")
