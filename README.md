# Dataset-Data_types

## Project Overview
This project performs an initial exploratory data analysis (EDA) on two datasets:
- *Titanic Dataset*
- *Students Performance Dataset*

## Tools and Technologies Used
- Python 3
- Pandas
- NumPy
- Jupyter Notebook / VS Code / PyCharm

## Steps Performed

### 1. Loading the Dataset
- The datasets were loaded using the `pandas.read_csv()` function.
- The first few records were displayed using `df.head()` to understand column names and initial data.
- The last few records were displayed using `df.tail()` to verify data consistency and row structure.

### 2. Identification of Feature Types
By manually inspecting column names and sample values, features were classified into:
- **Numerical features** (e.g., Age, Fare, Math Score)
- **Categorical features** (e.g., Sex, Embarked, Gender)
- **Ordinal features** (e.g., Education Level, Class)
- **Binary features** (e.g., Survived)

### 3. Dataset Information and Statistical Summary
- `df.info()` was used to inspect:
  - Data types of columns
  - Non-null counts
  - Presence of missing values
- `df.describe()` was used to generate statistical summaries such as:
  - Minimum and maximum values
  - Standard deviation

### 4. Analysis of Categorical Columns
- Unique values in categorical columns were examined using:
  `python
  df['column_name'].unique()
  
### 5. Target Variable and Input Features
-The target variable was identified based on the dataset objective:
-Titanic Dataset: Survived
-Students Performance Dataset: Performance / Score
-The datasets were evaluated for supervised machine learning suitability.

### 6. Dataset Size and ML Suitability
-The number of rows and columns were checked using df.shape.
-Both datasets have sufficient records and feature diversity to:
-Train basic machine learning models and Perform classification or regression tasks

### 7. Observations on Data Quality
-Presence of missing values in some columns
-Potential class imbalance in target variables
-Some categorical features require encoding
-Numerical features may need scaling
-These issues should be addressed during data preprocessing before applying machine learning models.
