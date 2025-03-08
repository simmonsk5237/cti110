# Kimberly Simmons
# 03/08/2025
# Assignment P1HW1
# This program takes user input to perform power calculations and addition/subtraction.

# Power Calculation
print("-----Calculating Exponents----\n")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")

# Addition and Subtraction
print("-----Addition and Subtraction----\n")

start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
sub_num = int(input("Enter an integer to subtract: "))

final_result = start_num + add_num - sub_num
print(f"\n{start_num} + {add_num} - {sub_num} is equal to {final_result}\n")
