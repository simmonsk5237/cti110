# Kimberly Simmons
# 03/08/2025
# Assignment P1HW2
# This program calculates and displays travel expenses based on user input.

# Pseudocode:
# 1. Ask user to enter their budget
# 2. Ask user to enter travel destination
# 3. Ask user for amount they will spend on gas
# 4. Ask user for amount they will spend on accommodation
# 5. Ask user for amount they will spend on food
# 6. Add expenses
# 7. Subtract expenses from budget
# 8. Display results

# Get user inputs
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate expenses and remaining balance
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

# Display travel expenses summary
print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print("\nFuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("\nRemaining Balance:", remaining_balance)
