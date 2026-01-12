print("STUDENTS MARK ANALYSIS PROJECT")

import numpy as np

np.random.seed(42)
marks = np.random.randint(0, 51, (100, 5))
student_ids = np.arange(1, 101).reshape(100, 1)
data = np.hstack((student_ids, marks))

headers = ["Student_ID", "Finance", "HR", "Marketing", "BA", "Operations"]

def display_data():
    print(headers)
    for row in data:
        print(row)

def total_marks(marks):
    total_per_student = np.sum(marks, axis=1)
    total_per_subject = np.sum(marks, axis=0)
    print("Total mark of each student:\n", total_per_student)
    print("Total mark of each subject:\n", total_per_subject)

def average_marks(marks):
    avg_subject = np.mean(marks, axis=0)
    avg_student = np.mean(marks, axis=1)
    print("Average marks per subject:", avg_subject)
    print("Average marks per student:", avg_student)

def highest_lowest(marks):
    highest = np.max(marks, axis=0)
    lowest = np.min(marks, axis=0)
    print("Highest mark per subject:", highest)
    print("Lowest mark per subject:", lowest)

def pass_percentage(marks):
    passed = marks >= 40
    pass_count = np.sum(passed, axis=0)
    print("Pass count per subject:", pass_count)

def difficult_subject(marks, headers):
    avg = np.mean(marks, axis=0)
    index = np.argmin(avg)
    print("Most difficult subject:", headers[index + 1],
          "with average:", avg[index])

def rank_students(marks):
    total = np.sum(marks, axis=1)
    ranks = np.argsort(-total)
    print("Ranking of students (0 means student 1):")
    print(ranks)

def assign_grades(marks):
    print("Grades for each student:")
    total = np.sum(marks, axis=1)
    for i, t in enumerate(total, start=1):
        if t < 100:
            grade = "D"
        elif t < 150:
            grade = "C"
        elif t < 200:
            grade = "B"
        else:
            grade = "A"
        print(f"Student {i}: Total = {t}, Grade = {grade}")

def statistics(marks):
    print("Statistics for each student:")
    print("Median:", np.median(marks, axis=1))
    print("Variance:", np.var(marks, axis=1))
    print("Standard Deviation:", np.std(marks, axis=1))

    print("\nStatistics per subject:")
    print("Subject Median:", np.median(marks, axis=0))
    print("Subject Variance:", np.var(marks, axis=0))
    print("Subject Standard Deviation:", np.std(marks, axis=0))

def toppers_per_subject(marks, headers):
    print("Topper per subject:")
    for i in range(5):
        topper = np.argmax(marks[:, i])
        print(headers[i+1], "Topper → Student", topper + 1,
              "Mark:", marks[topper, i])

display_data()

while True:
    print("\nOPTIONS")
    print("1 - Total marks")
    print("2 - Average")
    print("3 - Highest & lowest")
    print("4 - Pass percentage")
    print("5 - Most difficult subject")
    print("6 - Ranking students")
    print("7 - Grade")
    print("8 - Median, Variance, STD")
    print("9 - Topper per subject")
    print("10 - Exit")

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
        print("Exiting Student Mark Analysis Program...")
        break
    else:
        print("Invalid input. Try again.")
