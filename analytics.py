import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect("warehouse.db")

df = pd.read_sql(
    "SELECT * FROM student_performance",
    connection
)

connection.close()

plt.figure(figsize=(10,5))

plt.bar(
    df["name"],
    df["average_score"]
)

plt.title("Average Student Scores")

plt.xlabel("Student")
plt.ylabel("Average Score")

plt.show()