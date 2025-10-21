'''
Write a program to design a app for Retail Store , Calculate Final Bill and Discount on Multiple
Brands according to the given choice
Woodland - 20% Discount
Levis - 30% Discount
VeroModa - 35% Dicount
US Polo - 40% Dicount
User can shop from multiple brands, also with amount Exceeding 5000 , offer a Gift Voucher of Rs500
'''

print("Welcome to the Retail Store!")
print("Available Brands:")
print("1. Woodland - 20% Discount")
print("2. Levis - 30% Discount")
print("3. VeroModa - 35% Discount")
print("4. US Polo - 40% Discount")

brand_prices = { 
    1: ("Woodland", 2000, 0.20), 
    2: ("Levis", 3000, 0.30),
    3: ("VeroModa", 2500, 0.35),
    4: ("US Polo", 4000, 0.40)
}

total_amount = 0

while True: # Loop to allow multiple brand selections
    brand_choice = int(input("Enter choice of Brand (1/2/3/4) or 0 to finish shopping: ")) 
    if brand_choice == 0: 
        break # Exit loop if user is done shopping
    if brand_choice in brand_prices: 
        brand_name, price, discount = brand_prices[brand_choice]
        total_amount += price * (1 - discount)
        print(f"Added {brand_name} to cart. Price after discount: Rs{price * (1 - discount)}") 
    else:
        print("Invalid choice of brand.")
      
print(f"Total amount after discounts: Rs{total_amount:.2f}") 
if total_amount > 5000:
    print("Congratulations! You are eligible for a Gift Voucher of Rs500.")
    final_amount = total_amount - 500 # Assuming the voucher is applied as a discount
else:
    final_amount = total_amount
print(f"Final amount to be paid: Rs{final_amount:.2f}")
print("Thank you for shopping with us!😊")
