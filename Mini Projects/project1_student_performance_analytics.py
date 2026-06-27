# ==========================================
# MINI PROJECT 1
# Student Performance Analytics using NumPy
# ==========================================

import numpy as np

# Generate random marks
np.random.seed(25)
marks = np.random.randint(10, 101, size=(20, 5))

print("=" * 60)
print("STUDENT MARKS DATASET")
print("=" * 60)
print(marks)

# ---------------------------------------------------
# 1. Average by Subject and Student
# ---------------------------------------------------
average_by_subject = np.mean(marks, axis=0)
average_by_student = np.mean(marks, axis=1)

print("\n1. Average Marks")
print("-" * 60)
print("Average by Subject :", average_by_subject)
print("Average by Student :", average_by_student)

# ---------------------------------------------------
# 2. Highest and Lowest Marks per Subject
# ---------------------------------------------------
highest = np.max(marks, axis=0)
lowest = np.min(marks, axis=0)

print("\n2. Highest & Lowest Marks")
print("-" * 60)
print("Highest Marks :", highest)
print("Lowest Marks  :", lowest)

# ---------------------------------------------------
# 3. Overall Class Topper
# ---------------------------------------------------
total = np.sum(marks, axis=1)
topper = np.argmax(total)

print("\n3. Overall Class Topper")
print("-" * 60)
print(f"Student Index : {topper}")
print(f"Total Marks   : {total[topper]}")

# ---------------------------------------------------
# 4. Pass Count per Subject
# ---------------------------------------------------
pass_count = np.sum(marks >= 40, axis=0)

print("\n4. Pass Count per Subject")
print("-" * 60)
print(pass_count)

# ---------------------------------------------------
# 5. Most Difficult Subject
# ---------------------------------------------------
difficult_subject = np.argmin(average_by_subject)

print("\n5. Most Difficult Subject")
print("-" * 60)
print(f"Subject Index : {difficult_subject}")
print(f"Average Marks : {average_by_subject[difficult_subject]:.2f}")

# ---------------------------------------------------
# 6. Student Ranking
# ---------------------------------------------------
ranking = np.argsort(-total)

print("\n6. Student Ranking")
print("-" * 60)
print(ranking)

print(f"\n🏆 First Rank : Student Index {ranking[0]}")


