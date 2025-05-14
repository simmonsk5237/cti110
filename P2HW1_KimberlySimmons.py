# Kimberly Simmons
# 03/15/2025
# P2HW1
# This program calculates and displays travel expenses. It collects user input for budget, 
# travel destination, and estimated expenses. The output is formatted so all values align neatly.

# Get user inputs
print("This program calculates and displays travel expenses\n")

budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")

fuel_cost = float(input("\nHow much do you think you will spend on gas? "))
accommodation_cost = float(input("\nApproximately, how much will you need for accomodation/hotel? "))
food_cost = float(input("\nLast, how much do you need for food? "))

# Calculate remaining balance
total_expense = fuel_cost + accommodation_cost + food_cost
remaining_balance = budget - total_expense

# Display formatted output
print("\n------------Travel Expenses------------")
print(f"{'Location:':<18}{destination}")
print(f"{'Initial Budget:':<18}${budget:,.2f}")
print(f"{'Fuel:':<18}${fuel_cost:,.2f}")
print(f"{'Accomodation:':<18}${accommodation_cost:,.2f}")
print(f"{'Food:':<18}${food_cost:,.2f}")
print("---------------------------------------")
print(f"\n{'Remaining Balance:':<18}${remaining_balance:,.2f}")
