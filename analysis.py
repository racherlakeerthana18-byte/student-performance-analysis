import numpy as np

# Student marks data (rows = students, columns = subjects)
marks = np.array([
    [85, 78, 92],
    [70, 88, 75],
    [90, 95, 89],
    [60, 65, 70],
    [88, 82, 85]
])

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5"]
subjects = ["Math", "Science", "English"]

print("Student Academic Performance Analysis\n")

# Average marks per student
student_avg = np.mean(marks, axis=1)
print("Average Marks per Student:")
for i in range(len(students)):
    print(f"{students[i]}: {student_avg[i]:.2f}")

# Average marks per subject
subject_avg = np.mean(marks, axis=0)
print("\nAverage Marks per Subject:")
for i in range(len(subjects)):
    print(f"{subjects[i]}: {subject_avg[i]:.2f}")

# Highest and lowest performing students
highest = np.argmax(student_avg)
lowest = np.argmin(student_avg)

print(f"\nHighest Performing Student: {students[highest]} ({student_avg[highest]:.2f})")
print(f"Lowest Performing Student: {students[lowest]} ({student_avg[lowest]:.2f})")
