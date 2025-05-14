# Kimberly Simmons
# 04/18/2025
# P4HW2
# This program calculates and displays gross pay, overtime pay, and regular pay for multiple employees.
# It terminates when the user enters "Done".

# Pseudocode:
# 1. Initialize counters: emp_count, total_overtime, total_regular, total_gross
# 2. Loop while employee name is not "Done":
#    a. Prompt for hours worked and pay rate
#    b. Calculate overtime hours and pay (if hours > 40)
#    c. Calculate regular pay and gross pay
#    d. Add to totals and increment employee count
#    e. Display formatted pay information
# 3. After loop, display total employees, overtime pay, regular pay, and gross pay

emp_count = 0
total_overtime = 0
total_regular = 0
total_gross = 0

emp_name = input("Enter employee's name or \"Done\" to terminate: ")

while emp_name != "Done":
    hours_worked = float(input(f"How many hours did {emp_name} work? "))
    pay_rate = float(input(f"What is {emp_name}'s pay rate? "))

    overtime_hours = hours_worked - 40 if hours_worked > 40 else 0
    regular_hours = hours_worked if hours_worked <= 40 else 40

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = overtime_pay + regular_pay

    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay
    emp_count += 1

    print(f"\nEmployee name:  {emp_name}\n")
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
    print("-" * 75)
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<10.2f}\n")

    emp_name = input("Enter employee's name or \"Done\" to terminate: ")

# Final summary output
print(f"\nTotal number of employees entered: {emp_count}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
