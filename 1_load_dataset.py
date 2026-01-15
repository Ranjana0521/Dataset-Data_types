import pandas as pd
import numpy as np

# Load Titanic dataset
titanic = pd.read_csv("titanic.csv")
print("First 5 rows of Titanic Dataset:")
print(titanic.head())

print("\nLast 5 rows of Titanic Dataset:")
print(titanic.tail())

# Load Students Performance dataset
students = pd.read_csv("StudentsPerformance.csv")
print("\nFirst 5 rows of Students Performance Dataset:")
print(students.head())

print("\nLast 5 rows of Students Performance Dataset:")
print(students.tail())
