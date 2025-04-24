#Kimberly Simmons
#04/24/2025
#P5LAB
#This program simulates a self-checkout machine calculating change from a random total using a loop and function.

import random

def disperse_change(change):
    change_cents = int(round(change * 100))  # Convert dollars to cents

    dollars = change_cents // 100
    change_cents %= 100

    quarters = change_cents // 25
    change_cents %= 25

    dimes = change_cents // 10
    change_cents %= 10

    nickels = change_cents // 5
    change_cents %= 5

    pennies = change_cents

    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")
    amount_paid = float(input("How much cash will you put in the self-checkout? "))
    change = round(amount_paid - amount_owed, 2)
    print(f"Change is: ${change:.2f}")
    disperse_change(change)

main()
