# Kimberly Simmons
# 03/09/2025
# Assignment: P2LAB2
# This program stores vehicle MPG values, prompts the user for input, 
# and calculates the fuel needed for a given distance.

# Create the dictionary with automobile names as keys and MPG as values
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Create a variable that holds all the keys
keys = vehicle_mpg.keys()

# Print the available vehicle keys
print(keys)

# Prompt the user to enter a vehicle name
vehicle = input("\nEnter a vehicle to see its mpg: ").strip()

# Check if vehicle exists in the dictionary
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"\nThe {vehicle} gets {mpg} mpg.")

    # Prompt the user to enter miles to be driven
    miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

    # Calculate the gallons of gas needed
    gallons_needed = miles / mpg

    # Display the result using an f-string, rounded to 2 decimal places
    print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
