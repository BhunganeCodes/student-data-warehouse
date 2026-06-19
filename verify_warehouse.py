import pandas as pd
import sqlite3

connection = sqlite3.connect("warehouse.db")

df = pd.read_sql(
    "SELECT * FROM student_performance",
    connection
)

print(df)