# Kimberly Simmons
# 03/15/2025
# P2HW2
# This program prompts the user to enter grades for six modules, stores them in a list, 
# and then calculates and displays the lowest grade, highest grade, sum of grades, 
# and the average, formatted exactly as shown in the example.

# Get grades from the user and store in a list
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Perform calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Display results formatted exactly as shown in the example
print("\n------------Results------------")
print(f"Lowest Grade:        {lowest:.1f}")
print(f"Highest Grade:       {highest:.1f}")
print(f"Sum of Grades:       {total:.1f}")
print(f"Average:             {average:.2f}")
print("--------------------------------")
