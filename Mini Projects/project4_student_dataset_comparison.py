print("STUDENTS MARK ANALYSIS PROJECT - DATASET 1")

import numpy as np
np.random.seed(42)

# -------------------Dataset-1------------------
marks = np.random.randint(0, 51, (100, 5))
student_ids = np.arange(1, 101).reshape(100, 1)
data = np.hstack((student_ids, marks))

headers1 = ["Student_ID", "Finance", "HR", "Marketing", "BA", "Operations"]

print(headers1)
for row in data:
    print(row)


# ------------------ DATASET 2 ------------------

print("\nSTUDENTS MARK ANALYSIS PROJECT - DATASET 2 ")

Students_names = [
    "Aarav", "Aadhya", "Ishaan", "Diya", "Arjun", "Nithya", "Saanvi", "Vivaan", "Riya", "Kabir",
    "Aarohi", "Krishna", "Ananya", "Rohan", "Meera", "Yash", "Tanvi", "Rahul", "Sneha", "Vikram",
    "Harini", "Aditya", "Swara", "Siddharth", "Kavya", "Varun", "Lakshmi", "Rithika", "Shreya", "Kiran",
    "Santhosh", "Sahana", "Gowtham", "Aishwarya", "Rakesh", "Bhavya", "Teja", "Vidya", "Akash", "Shruti",
    "Charan", "Shiva", "Veena", "Naveen", "Preethi", "Manoj", "Anu", "Vishal", "Gayathri", "Aravind",
    "Samarth", "Nakul", "Keerthi", "Suresh", "Monika", "Anika", "Surya", "Sujith", "Mahesh", "Priya",
    "Rohit", "Yuvraj", "Deepak", "Pooja", "Ranjith", "Keerthana", "Jeevan", "Sindhu", "Jai", "Pavithra",
    "Ashwin", "Mithra", "Bharath", "Nikita", "Sathish", "Divya", "Abhinav", "Janani", "Harsha", "Revathi",
    "Sudarshan", "Lavanya", "Rajesh", "Sandhya", "Karthik", "Lalitha", "Pranav", "Meghana", "Tarun", "Uma",
    "Dhruv", "Chandana", "Shyam", "Vaishnavi", "Roshan", "Hemalatha", "Vasanth", "Aparna", "Vijay", "Padmini"
]

np.random.seed(24)
marks2 = np.random.randint(0, 51, (100, 5))

names = np.array(Students_names).reshape(100, 1)
data2 = np.hstack((names, marks2))

headers2 = ["Name", "Finance", "HR", "Marketing", "BA", "Operations"]

print(headers2)
for row in data2:
    print(row)

print("\n====== COMPARISON MENU ======\n")

def compare_subject_avg(m1, m2, headers):
    print("\n--- SUBJECT-WISE AVERAGE COMPARISON ---")
    avg1 = np.mean(m1, axis=0)
    avg2 = np.mean(m2, axis=0)

    for i in range(5):
        print(f"{headers[i+1]} → Dataset1 Avg = {avg1[i]:.2f} | Dataset2 Avg = {avg2[i]:.2f}")

def compare_overall_avg(m1, m2):
    print("\n--- OVERALL AVERAGE COMPARISON ---")
    print("Dataset1 Overall Avg:", np.mean(m1))
    print("Dataset2 Overall Avg:", np.mean(m2))

def compare_subject_total(m1, m2, headers):
    print("\n--- SUBJECT TOTAL COMPARISON ---")
    total1 = np.sum(m1, axis=0)
    total2 = np.sum(m2, axis=0)

    for i in range(5):
        print(f"{headers[i+1]} → Dataset1 Total = {total1[i]} | Dataset2 Total = {total2[i]}")

def compare_overall_total(m1, m2):
    print("\n--- OVERALL TOTAL COMPARISON ---")
    print("Dataset1 Overall Total:", np.sum(m1))
    print("Dataset2 Overall Total:", np.sum(m2))

def compare_subject_median(m1, m2, headers):
    print("\n--- SUBJECT MEDIAN COMPARISON ---")
    med1 = np.median(m1, axis=0)
    med2 = np.median(m2, axis=0)

    for i in range(5):
        print(f"{headers[i+1]} → D1 Median = {med1[i]} | D2 Median = {med2[i]}")

def compare_overall_median(m1, m2):
    print("\n--- OVERALL MEDIAN COMPARISON ---")
    print("Dataset1 Overall Median:", np.median(m1))
    print("Dataset2 Overall Median:", np.median(m2))

def compare_pass_percentage(m1, m2, headers):
    print("\n--- PASS PERCENTAGE COMPARISON (>=40) ---")
    p1 = np.sum(m1 >= 40, axis=0)
    p2 = np.sum(m2 >= 40, axis=0)

    for i in range(5):
        print(f"{headers[i+1]} → D1 Passed = {p1[i]} | D2 Passed = {p2[i]}")

def compare_difficulty(m1, m2, headers):
    print("\n--- DIFFICULT SUBJECT COMPARISON ---")
    avg1 = np.mean(m1, axis=0)
    avg2 = np.mean(m2, axis=0)

    hard1 = headers[np.argmin(avg1) + 1]
    hard2 = headers[np.argmin(avg2) + 1]

    print("Dataset1 Most Difficult:", hard1)
    print("Dataset2 Most Difficult:", hard2)

# ---------------- MENU ----------------
while True:
    print("\nCOMPARISON OPTIONS:")
    print("1 - Subject-wise Average")
    print("2 - Overall Average")
    print("3 - Subject Total")
    print("4 - Overall Total")
    print("5 - Subject Median")
    print("6 - Overall Median")
    print("7 - Pass Percentage")
    print("8 - Most Difficult Subject")
    print("9 - Exit Comparison")

    key = int(input("Enter your choice: "))

    if key == 1:
        compare_subject_avg(marks, marks2, headers1)

    elif key == 2:
        compare_overall_avg(marks, marks2)

    elif key == 3:
        compare_subject_total(marks, marks2, headers1)

    elif key == 4:
        compare_overall_total(marks, marks2)

    elif key == 5:
        compare_subject_median(marks, marks2, headers1)

    elif key == 6:
        compare_overall_median(marks, marks2)

    elif key == 7:
        compare_pass_percentage(marks, marks2, headers1)

    elif key == 8:
        compare_difficulty(marks, marks2, headers1)

    elif key == 9:
        print("Exiting comparison menu...")
        break

    else:
        print("Invalid option. Try again.")
