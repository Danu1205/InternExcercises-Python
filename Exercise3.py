total = 0
for i in range(1, 6):
    marks = int(input(f"Enter marks for subject {i}: "))
    total += marks
percentage = total / 5
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"
print("Total Marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)
