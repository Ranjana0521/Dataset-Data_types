import pandas as pd

titanic = pd.read_csv("titanic.csv")
students = pd.read_csv("StudentsPerformance.csv")

titanic_cat = titanic.select_dtypes(include='object')
students_cat = students.select_dtypes(include='object')

for col in titanic_cat.columns:
    print(f"\nColumn: {col}")
    print(titanic[col].unique())

for col in students_cat.columns:
    print(f"\nColumn: {col}")
    print(students[col].unique())

for col in students_cat.columns:
    print(f"\nValue counts for {col}:")
    print(students[col].value_counts())
