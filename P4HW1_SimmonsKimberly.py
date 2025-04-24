# Kimberly Simmons
# 04/18/2025
# Assignment: P4HW1
# This program asks the user how many scores they want to enter, uses a loop to collect them with validation,
# drops the lowest score, calculates the average, and displays a letter grade using a lookup list (no branching).

# Pseudocode:
# 1. Ask user how many scores they want to enter.
# 2. Create an empty list called scores.
# 3. Use a loop to collect that number of scores.
# 4. For each score:
#    - While the score is not between 0 and 100, display error and re-prompt.
#    - Append valid score to the list.
# 5. Remove the lowest score from the list.
# 6. Calculate the average from the modified list.
# 7. Use integer division and a grade scale list to assign a letter grade.
# 8. Display results: lowest score, modified list, average, and grade.

num_scores = int(input("How many scores do you want to enter? "))
scores = []
score_number = 1

while len(scores) < num_scores:
    score = float(input(f"Enter score #{score_number}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_number} again: "))
    scores.append(score)
    score_number += 1

lowest = min(scores)
scores.remove(lowest)
average = sum(scores) / len(scores)

grade_scale = ['F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A', 'A']
grade = grade_scale[int(average) // 10]

print("\n----------------Results----------------")
print(f"Lowest Score  : {lowest:.1f}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("----------------------------------------")
