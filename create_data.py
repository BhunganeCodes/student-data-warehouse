import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": [
        "Lebohang",
        "Themba",
        "Rorisang",
        "David",
        "Thamsanqa"
    ]
})

math = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "math_score": [85, 78, 98, 90, 95]
})

science = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "science_score": [78, 88, 73, 92, 90]
})

attendance = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "attendance_percent": [90, 88, 98, 99, 93]
})

# Convert data into csv files

students.to_csv("data/students.csv", index=False)
math.to_csv("data/math.csv", index=False)
science.to_csv("data/science.csv", index=False)
attendance.to_csv("data/attendance.csv", index=False)

print("Data created!")