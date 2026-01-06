students = {
    "A": 85,
    "B": 78,
    "C": 92,
    "D": 88,
    "E": 76
}
print("Student Names:")
for name in students.keys():
    print(name)
print("\nMarks:")
for marks in students.values():
    print(marks)
average = sum(students.values()) / len(students)
print("\nAverage Marks:", average)
students["F"] = 81
print("\nAfter adding new student:", students)
students["Bob"] = 82
print("\nAfter updating Bob's marks:", students)
