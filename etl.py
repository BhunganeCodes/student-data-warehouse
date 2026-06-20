import pandas as pd
import sqlite3

# Extract data from CSV files -> Extract stage
students = pd.read_csv("data/students.csv")
math = pd.read_csv("data/math.csv")
science = pd.read_csv("data/science.csv")
attendance = pd.read_csv("data/attendance.csv")


# Merge Data on student_id -> Transform stage
warehouse = students.merge(
    math,
    on="student_id"
)

warehouse = warehouse.merge(
    science,
    on="student_id"
)

warehouse = warehouse.merge(
    attendance,
    on="student_id"
)

warehouse["average_score"] = (warehouse["math_score"] + warehouse["science_score"]) / 2
warehouse["rank"] = (warehouse["average_score"].rank(ascending=False))
warehouse["status"] = (warehouse["average_score"].apply(lambda x: "Pass" if x >= 50 else "Fail"))


# Load to database -> Load stage
connection = sqlite3.connect("warehouse.db")

warehouse.to_sql(
    "student_performance",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Warehouse loaded!")

# Export data to csv file & excel file
warehouse.to_csv("student_report.csv", index=False)
warehouse.to_excel("student_report.xlsx", index=False)
print("Warehouse Data Exported to CSV & Excel files.")