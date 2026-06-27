import numpy as np

# ==========================================
# MINI PROJECT 2
# Student Marks Statistical Analysis
# ==========================================

np.random.seed(42)
marks = np.random.randint(0, 51, (100, 5))

student_ids = np.arange(1, 101).reshape(100, 1)
data = np.hstack((student_ids, marks))

headers = ["Student_ID", "Finance", "HR", "Marketing", "BA", "Operations"]

# ----------------------------------------------------
# Display Dataset
# ----------------------------------------------------
print("=" * 80)
print("                 STUDENT MARKS DATASET")
print("=" * 80)

print(f"{headers[0]:<12}{headers[1]:>10}{headers[2]:>8}{headers[3]:>12}{headers[4]:>8}{headers[5]:>14}")

for row in data:
    print(f"{row[0]:<12}{row[1]:>10}{row[2]:>8}{row[3]:>12}{row[4]:>8}{row[5]:>14}")

# ----------------------------------------------------
# Student Statistics
# ----------------------------------------------------
total = np.sum(marks, axis=1)
mean_marks = np.mean(marks, axis=1)
median_marks = np.median(marks, axis=1)
variance_marks = np.var(marks, axis=1)
std_marks = np.std(marks, axis=1)

print("\n")
print("=" * 80)
print("              FIRST 5 STUDENTS STATISTICS")
print("=" * 80)

print(f"{'Student':<10}{'Total':>10}{'Mean':>10}{'Median':>10}{'Variance':>12}{'Std Dev':>12}")

for i in range(5):
    print(f"{i+1:<10}{total[i]:>10}{mean_marks[i]:>10.2f}{median_marks[i]:>10.1f}{variance_marks[i]:>12.2f}{std_marks[i]:>12.2f}")

# ----------------------------------------------------
# Subject Statistics
# ----------------------------------------------------
subject_mean = np.mean(marks, axis=0)
subject_median = np.median(marks, axis=0)
subject_variance = np.var(marks, axis=0)
subject_std = np.std(marks, axis=0)

print("\n")
print("=" * 80)
print("                 SUBJECT-WISE STATISTICS")
print("=" * 80)

print(f"{'Subject':<15}{'Mean':>10}{'Median':>10}{'Variance':>12}{'Std Dev':>12}")

for i, subject in enumerate(headers[1:]):
    print(f"{subject:<15}{subject_mean[i]:>10.2f}{subject_median[i]:>10.1f}{subject_variance[i]:>12.2f}{subject_std[i]:>12.2f}")

print("\n")
print("=" * 80)
print("Analysis Completed Successfully")
print("=" * 80)
