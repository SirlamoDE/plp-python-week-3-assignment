
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Test the function
print(calculate_discount(150, 22))  # Expected output: 80

"""Using the calculate_discount function, prompt the user to enter the original price of 
an item and the discount percentage. Print the final price after applying the discount, 
or if no discount was applied, print the original price.

Note: The discount percentage should be a positive integer less than or equal to 25."""

price = float(input("Enter the original price of the item: "))

while True:
    try:
        discount_percent = int(input("Enter the discount percentage (1-20): "))
        if 1 <= discount_percent <= 20:
            break
        else:
            print("Invalid discount percentage. Please enter a positive integer between 1 and 20.")
    except ValueError:
        print("Invalid input. Please enter a valid discount percentage.")

final_price = calculate_discount(price, discount_percent)

if final_price != price:
    print(f"The final price after applying the {discount_percent}% discount is {final_price}.")
    print("Thank you for using my discount calculator!")