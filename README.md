# Student Performance Data Warehouse

A beginner-friendly Data Engineering project built with Python, Pandas, SQLite, and Matplotlib.

This project simulates a real-world data warehouse that collects student information from multiple data sources, transforms the data, loads it into a database, and generates analytics reports.

---

## Project Overview

Educational institutions often store data in separate systems:

- Student information
- Subject marks
- Attendance records

This project demonstrates how a Data Engineer can combine these data sources into a centralized data warehouse for reporting and analysis.

---

## Architecture

```text
CSV Files
│
├── students.csv
├── math.csv
├── science.csv
└── attendance.csv
      │
      ▼
Extract
      │
      ▼
Transform
      │
      ▼
SQLite Data Warehouse
      │
      ▼
Analytics & Reporting
```

---

## Features

- Extract data from multiple CSV files
- Transform and clean data using Pandas
- Merge datasets into a centralized warehouse
- Calculate average student scores
- Generate student rankings
- Create pass/fail classifications
- Analyze attendance vs performance
- Store processed data in SQLite
- Export reports to CSV and Excel
- Create visual analytics dashboards

---

## Technologies Used

- Python 3
- Pandas
- SQLite
- Matplotlib
- OpenPyXL

---

## Project Structure

```text
student-data-warehouse/
│
├── data/
│   ├── students.csv
│   ├── math.csv
│   ├── science.csv
│   └── attendance.csv
│
├── create_data.py
├── etl.py
├── analytics.py
├── warehouse.db
├── student_report.csv
├── student_report.xlsx
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/student-data-warehouse.git

cd student-data-warehouse
```

### Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Generate Sample Data

This creates sample student records and subject scores.

```bash
python create_data.py
```

Output:

```text
Data created!
```

Generated files:

```text
data/students.csv
data/math.csv
data/science.csv
data/attendance.csv
```

---

## Run ETL Pipeline

This extracts data from the CSV files, transforms the data, calculates metrics, and loads everything into SQLite.

```bash
python etl.py
```

Output:

```text
Warehouse loaded!
```

Generated:

```text
warehouse.db
```

---

## Run Analytics Dashboard

Generate visual reports and charts.

```bash
python analytics.py
```

The dashboard includes:

- Average student scores
- Attendance vs performance analysis
- Student rankings

---

## Database Schema

### student_performance

| Column | Description |
|----------|----------|
| student_id | Unique student identifier |
| name | Student name |
| math_score | Mathematics score |
| science_score | Science score |
| attendance_percent | Attendance percentage |
| average_score | Average score |
| rank | Student rank |
| status | Pass or Fail |

---

## Example Analytics

### Top Students

Identify the highest-performing students based on average scores.

### Attendance Analysis

Determine whether attendance correlates with academic performance.

### Pass/Fail Report

Categorize students according to academic thresholds.

---

## Export Reports

The ETL process can export reports to:

### CSV

```python
warehouse.to_csv(
    "student_report.csv",
    index=False
)
```

### Excel

```python
warehouse.to_excel(
    "student_report.xlsx",
    index=False
)
```

---

## Future Improvements

- Add more subjects
- Add multiple semesters
- Add student demographics
- Build a star schema data warehouse
- Add PostgreSQL support
- Containerize using Docker
- Schedule ETL jobs with Airflow
- Build an interactive dashboard with Streamlit

---

## Learning Outcomes

This project demonstrates key Data Engineering concepts:

- ETL Pipelines
- Data Cleaning
- Data Transformation
- Data Warehousing
- Data Modeling
- SQL Databases
- Reporting & Analytics
- Data Visualization

---

## Author

Thamsanqa Hadebe

Aspiring Data Engineer | Web Developer | AI Enthusiast