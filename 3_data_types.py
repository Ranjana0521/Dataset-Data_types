import pandas as pd

# Load datasets
titanic = pd.read_csv("titanic.csv")
students = pd.read_csv("StudentsPerformance.csv")

titanic.info()
students.info()

titanic.describe()
students.describe()
