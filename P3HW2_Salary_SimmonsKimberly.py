# Kimberly Simmons
# Date: 03/30/2025
# Assignment: P3HW2 – Salary Calculator
# This program calculates the gross pay of an employee based on regular and overtime hours worked.

"""
Pseudocode:
1. Ask user to enter employee name.
2. Ask user to enter number of hours worked this week.
3. Ask user to enter employee's pay rate.
4. If hours worked > 40:
   a. Calculate overtime hours = hours worked - 40
   b. Calculate overtime pay = overtime hours * pay rate * 1.5
   c. Calculate regular pay = 40 * pay rate
5. Else:
   a. Overtime hours = 0
   b. Overtime pay = 0
   c. Regular pay = hours worked * pay rate
6. Gross pay = regular pay + overtime pay
7. Display employee name, hours worked, pay rate, overtime hours, overtime pay, regular pay, and gross pay.
"""

# Input from user
emp_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Initialize variables
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    reg_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    reg_pay = hours_worked * pay_rate

gross_pay = reg_pay + overtime_pay

# Output
print("---------------------------------------------")
print(f'Employee name:  {emp_name}')
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<10}{"OverTime":<10}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<10}')
print("--------------------------------------------------------------------------")
print(f'{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${reg_pay:<14.2f}${gross_pay:<10.2f}')
