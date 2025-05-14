# Kimberly Simmons
# P3HW1 – Debugging Program
# This program takes number grades, determines the average,
# and displays the corresponding letter grade based on the average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display results
print('\n------------Results------------')
print(f'Lowest Grade:     {low:.1f}')
print(f'Highest Grade:    {high:.1f}')
print(f'Sum of Grades:    {total:.1f}')
print(f'Average:          {avg:.2f}')
print('--------------------------------')

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')
