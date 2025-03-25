# Kimberly Simmons
# 03/25/2025
# Assignment: P3Lab
# This program allows the user to enter a money (float) value with two decimal places. 
# It then calculates the most efficient number of dollars, quarters, dimes, nickels, 
# and pennies needed to make that amount. The program omits any denominations not needed 
# and adjusts singular/plural labels appropriately.

amount = float(input("Enter the amount of money as a float: $"))

# Convert to cents to simplify calculations
cents = int(round(amount * 100))

if cents == 0:
    print("No change")
else:
    if cents >= 100:
        dollars = cents // 100
        cents %= 100
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if cents >= 25:
        quarters = cents // 25
        cents %= 25
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if cents >= 10:
        dimes = cents // 10
        cents %= 10
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if cents >= 5:
        nickels = cents // 5
        cents %= 5
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if cents >= 1:
        print(f"{cents} Penn{'ies' if cents > 1 else 'y'}")
