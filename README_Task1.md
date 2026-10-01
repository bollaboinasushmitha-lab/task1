# Task 1: Data Cleaning and Preprocessing

## Objective
Clean and prepare a raw customer dataset containing missing values, duplicate records, inconsistent text, and inconsistent date formats.

## Tools
- Microsoft Excel
- Python
- Pandas

## Dataset
This submission uses a small customer dataset created for practice. It contains the same types of issues specified in the task: nulls, duplicates, inconsistent categorical values, and mixed date formats.

## Cleaning performed
1. Renamed column headers to lowercase with underscores.
2. Removed extra spaces from text values.
3. Standardized Gender values to Male/Female.
4. Standardized city names.
5. Standardized Active values to Yes/No.
6. Converted Join Date to a consistent date type.
7. Converted Age and Annual Income to numeric types.
8. Filled missing Age and Annual Income using the median.
9. Filled missing Gender using the mode.
10. Removed exact duplicate rows.
11. Flagged remaining duplicate Customer IDs for review.

## Deliverables
- `Task1_Data_Cleaning_and_Preprocessing.xlsx`
- `task1_cleaning.py`

## Interview Questions - Short Answers
1. **What are missing values and how do you handle them?**
   Missing values are blank or unavailable data. They can be removed or filled using mean, median, mode, or a suitable business rule.

2. **How do you treat duplicate records?**
   Identify duplicates using a unique key or complete-row comparison, then remove exact duplicates. Possible duplicate IDs should be reviewed before deletion.

3. **Difference between dropna() and fillna() in Pandas?**
   `dropna()` removes rows/columns containing missing values. `fillna()` replaces missing values with a selected value.

4. **What is outlier treatment and why is it important?**
   Outlier treatment means identifying unusually high or low observations and deciding whether to correct, cap, transform, or retain them. It prevents unusual values from distorting analysis.

5. **Explain standardizing data.**
   Standardizing data means putting values into a consistent format, such as Male/Female instead of M/F/male/female.

6. **How do you handle inconsistent date formats?**
   Convert dates to one standard date type using Excel formatting or Pandas `to_datetime()`.

7. **What are common data cleaning challenges?**
   Missing values, duplicates, inconsistent spellings, wrong data types, invalid dates, outliers, and inconsistent units.

8. **How can you check data quality?**
   Check missing values, duplicates, data types, valid ranges, unique values, date validity, and consistency with business rules.
