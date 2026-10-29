
students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")

    marks = []
    for j in range(1, 6):
        mark = int(input(f"Enter marks in subject {j}: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = int(input("Enter annual family income: "))

    aggregate = sum(marks) / len(marks)

    if (aggregate >= 75 and min(marks) >= 60
            and attendance >= 75 and income <= 250000):
        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

students.sort(key=lambda s: (
    -s["aggregate"], -s["attendance"], s["income"]
))

print("\n--- SCHOLARSHIP ELIGIBLE STUDENTS ---")

if students:
    for rank, s in enumerate(students, start=1):
        print(
            rank, s["name"],
            "| Aggregate:", round(s["aggregate"], 2),
            "| Attendance:", s["attendance"],
            "| Income:", s["income"]
        )
else:
    print("No eligible students found.")

