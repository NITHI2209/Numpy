print("=" * 75)
print("              STUDENT MARK ANALYSIS SYSTEM")
print("=" * 75)

import numpy as np

np.random.seed(42)
marks = np.random.randint(0, 51, (100, 5))
student_ids = np.arange(1, 101).reshape(100, 1)
data = np.hstack((student_ids, marks))

headers = ["Student_ID", "Finance", "HR", "Marketing", "BA", "Operations"]


def display_data():
    print("\n" + "=" * 75)
    print("FIRST 10 STUDENTS DATASET")
    print("=" * 75)

    print(f"{headers[0]:<12}{headers[1]:>10}{headers[2]:>8}{headers[3]:>12}{headers[4]:>8}{headers[5]:>14}")

    for row in data[:10]:
        print(f"{row[0]:<12}{row[1]:>10}{row[2]:>8}{row[3]:>12}{row[4]:>8}{row[5]:>14}")

    print("\nShowing first 10 records out of 100 students.\n")


def total_marks(marks):
    print("\n" + "=" * 75)
    print("TOTAL MARKS")
    print("=" * 75)

    total_per_student = np.sum(marks, axis=1)
    total_per_subject = np.sum(marks, axis=0)

    print("Total Marks (First 10 Students):")
    print(total_per_student[:10])

    print("\nTotal Marks Per Subject:")
    for subject, total in zip(headers[1:], total_per_subject):
        print(f"{subject:<12}: {total}")


def average_marks(marks):
    print("\n" + "=" * 75)
    print("AVERAGE MARKS")
    print("=" * 75)

    avg_subject = np.mean(marks, axis=0)
    avg_student = np.mean(marks, axis=1)

    print("Average Marks Per Subject")
    for subject, avg in zip(headers[1:], avg_subject):
        print(f"{subject:<12}: {avg:.2f}")

    print("\nAverage Marks (First 10 Students)")
    print(np.round(avg_student[:10], 2))


def highest_lowest(marks):
    print("\n" + "=" * 75)
    print("HIGHEST & LOWEST MARKS")
    print("=" * 75)

    highest = np.max(marks, axis=0)
    lowest = np.min(marks, axis=0)

    for i, subject in enumerate(headers[1:]):
        print(f"{subject:<12} Highest: {highest[i]:>3}   Lowest: {lowest[i]:>3}")


def pass_percentage(marks):
    print("\n" + "=" * 75)
    print("PASS COUNT PER SUBJECT")
    print("=" * 75)

    passed = marks >= 40
    pass_count = np.sum(passed, axis=0)

    for subject, count in zip(headers[1:], pass_count):
        print(f"{subject:<12}: {count} Students")


def difficult_subject(marks, headers):
    print("\n" + "=" * 75)
    print("MOST DIFFICULT SUBJECT")
    print("=" * 75)

    avg = np.mean(marks, axis=0)
    index = np.argmin(avg)

    print(f"Subject : {headers[index+1]}")
    print(f"Average : {avg[index]:.2f}")


def rank_students(marks):
    print("\n" + "=" * 75)
    print("TOP 10 STUDENT RANKINGS")
    print("=" * 75)

    total = np.sum(marks, axis=1)
    ranks = np.argsort(-total)

    for rank, student in enumerate(ranks[:10], start=1):
        print(f"Rank {rank:<2} -> Student {student+1:<3} Total = {total[student]}")


def assign_grades(marks):
    print("\n" + "=" * 75)
    print("GRADE REPORT (FIRST 10 STUDENTS)")
    print("=" * 75)

    total = np.sum(marks, axis=1)

    for i, t in enumerate(total[:10], start=1):
        if t < 100:
            grade = "D"
        elif t < 150:
            grade = "C"
        elif t < 200:
            grade = "B"
        else:
            grade = "A"

        print(f"Student {i:<3} Total = {t:<3} Grade = {grade}")


def statistics(marks):
    print("\n" + "=" * 75)
    print("STATISTICAL SUMMARY")
    print("=" * 75)

    print("Median (First 10 Students)")
    print(np.median(marks, axis=1)[:10])

    print("\nVariance (First 10 Students)")
    print(np.round(np.var(marks, axis=1)[:10], 2))

    print("\nStandard Deviation (First 10 Students)")
    print(np.round(np.std(marks, axis=1)[:10], 2))

    print("\nSubject Statistics")
    for i, subject in enumerate(headers[1:]):
        print(
            f"{subject:<12} "
            f"Median={np.median(marks, axis=0)[i]:>5.1f} "
            f"Variance={np.var(marks, axis=0)[i]:>8.2f} "
            f"Std={np.std(marks, axis=0)[i]:>7.2f}"
        )


def toppers_per_subject(marks, headers):
    print("\n" + "=" * 75)
    print("TOPPERS PER SUBJECT")
    print("=" * 75)

    for i in range(5):
        topper = np.argmax(marks[:, i])
        print(f"{headers[i+1]:<12} -> Student {topper+1:<3} Score = {marks[topper, i]}")


display_data()

while True:
    print("\n" + "=" * 75)
    print("MENU")
    print("=" * 75)
    print("1. Total Marks")
    print("2. Average Marks")
    print("3. Highest & Lowest Marks")
    print("4. Pass Count")
    print("5. Most Difficult Subject")
    print("6. Student Ranking")
    print("7. Grade Report")
    print("8. Statistics")
    print("9. Subject Toppers")
    print("10. Exit")
    print("=" * 75)

    key = int(input("Enter your choice: "))

    if key == 1:
        total_marks(marks)
    elif key == 2:
        average_marks(marks)
    elif key == 3:
        highest_lowest(marks)
    elif key == 4:
        pass_percentage(marks)
    elif key == 5:
        difficult_subject(marks, headers)
    elif key == 6:
        rank_students(marks)
    elif key == 7:
        assign_grades(marks)
    elif key == 8:
        statistics(marks)
    elif key == 9:
        toppers_per_subject(marks, headers)
    elif key == 10:
        print("\nThank you for using the Student Mark Analysis System!")
        break
    else:
        print("Invalid choice. Please try again.")
