#online shopping discount calculator

total_amount = float(input("Enter the total amount of your purchase: "))

if total_amount >= 100:
    discount = total_amount * 0.2
    print(f"You are eligible for a 20% discount! Your discount is ${discount:.2f}.")
else:
    print("You are not eligible for a discount.")