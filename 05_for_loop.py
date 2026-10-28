# Task 5: For Loop

# 1. Roll a six-sided die at least 20 times
# A fixed sequence is used so the output is reproducible.
rolls = [6, 2, 1, 4, 6, 3, 6, 1, 5, 2,
         6, 4, 1, 6, 3, 2, 6, 5, 1, 4]

six_count = 0
one_count = 0
two_sixes_in_row = 0

for i in range(len(rolls)):
    if rolls[i] == 6:
        six_count += 1
    if rolls[i] == 1:
        one_count += 1
    if i > 0 and rolls[i] == 6 and rolls[i - 1] == 6:
        two_sixes_in_row += 1

print("Number of 6s:", six_count)
print("Number of 1s:", one_count)
print("Two 6s in a row:", two_sixes_in_row)


# 2. Jumping jacks
completed = 0

while completed < 100:
    completed += 10
    print(f"You completed {completed} jumping jacks.")

    if completed == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired in ("yes", "y"):
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ("yes", "y"):
            print(f"You completed a total of {completed} jumping jacks.")
            break
    else:
        print(f"{100 - completed} jumping jacks are remaining.")
