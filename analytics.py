import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect("warehouse.db")

df = pd.read_sql(
    "SELECT * FROM student_performance",
    connection
)

connection.close()

def main():
    print("""
    === Data Analytics ===
          1. Average Student Scores
          2. Attendance vs Performance
          3. Exit
""")
    choice = int(input("ENTER A CHOICE: "))

    while True:
        if choice == 1:
            plt.figure(figsize=(10,5))

            plt.bar(
                df["name"],
                df["average_score"]
            )

            plt.title("Average Student Scores")

            plt.xlabel("Student")
            plt.ylabel("Average Score")

            plt.show()
            break
        
        elif choice == 2:
            plt.figure(figsize=(10,5))

            plt.scatter(
                df["attendance_percent"],
                df["average_score"]
            )

            plt.xlabel("Attendance %")
            plt.ylabel("Average Score")

            plt.title("Attendance vs Performance")

            plt.show()
            break

        elif choice == 3:
            break
        else: 
            continue

if __name__ == "__main__":
    main()