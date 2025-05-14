# Kimberly Simmons
# 04/18/2025
# P4LAB2
# This program asks for an integer and displays a multiplication table if the number is non-negative.
# No if/else statements are used. It uses both a while loop and a for loop.

# Pseudocode:
# 1. Loop (while) asking for an integer.
# 2. If number is non-negative, show multiplication table (1 to 12) using a for loop.
# 3. If number is negative, show error message.
# 4. Repeat while user types "yes".
# 5. Exit message at the end.

run_again = "yes"

while run_again.lower() == "yes":
    number = int(input("Enter an integer: "))

    # Create a list of items to "run" — either the table or the message, then loop through that
    table_lines = [f"{number} * {i} = {number * i}" for i in range(1, 13)]
    error_message = ["This program does not handle negative numbers."]

    # Slicing logic: if number >= 0, use table_lines; if < 0, use error_message
    results = table_lines * (number >= 0) + error_message * (number < 0)

    for line in results:
        print(line)

    run_again = input("\nWould you like to run the program again? ")

print("\nExiting program...")
