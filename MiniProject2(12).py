import numpy as np
np.random.seed(42)
marks = np.random.randint(0, 51, (100, 5))

student_ids = np.arange(1, 101).reshape(100, 1)

data = np.hstack((student_ids, marks))

headers = ["Student_ID", "Finance", "HR", "Marketing", "BA", "Operations"]

print(headers)
for row in data:
    print(row)

total = np.sum(marks, axis=1)
mean_marks = np.mean(marks, axis=1)
median_marks = np.median(marks, axis=1)
variance_marks = np.var(marks, axis=1)
std_marks = np.std(marks, axis=1)

print("\n---- First 5 Students Statistics ----")
for i in range(5):
    print(f"Student {i+1} Total: {total[i]}, Mean: {mean_marks[i]:.2f}, Median: {median_marks[i]}, Variance: {variance_marks[i]:.2f}, Std Dev: {std_marks[i]:.2f}")


subject_mean = np.mean(marks, axis=0)
subject_median = np.median(marks, axis=0)
subject_variance = np.var(marks, axis=0)
subject_std = np.std(marks, axis=0)

print("\n---- Subject-wise Statistics ----")
for i, sub in enumerate(headers[1:]):
    print(f"{sub} - Mean: {subject_mean[i]:.2f}, Median: {subject_median[i]}, Variance: {subject_variance[i]:.2f}, Std Dev: {subject_std[i]:.2f}")
