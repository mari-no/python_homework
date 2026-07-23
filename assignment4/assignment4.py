# #Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# Create a DataFrame from a dictionary:

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
}
task1_data_frame = pd.DataFrame(data)

print("DataFrame for Task1: ", task1_data_frame)


# Make a copy of the dataFrame you created named task1_with_salary 
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

print("DF with salary: ", task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older["Age"] += 1
print("Age modified: ", task1_older)


# Save the DataFrame as a CSV file:

task1_older.to_csv("employees.csv", index=False)



# Task 2: Loading Data from CSV and JSON

# Read data from a CSV file:
task2_employees = pd.read_csv("employees.csv")
print("Read from csv : ", task2_employees)

# Read data from a JSON file:
json_employees = pd.read_json("additional_employees.json")
print("Read from json: ", json_employees)


# Combine DataFrames:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("Combined DF:", more_employees)


# #Task 3: Data Inspection - Using Head, Tail, and Info Methods

# Assign the first three rows of the more_employees
#  DataFrame to the variable first_three

first_three = more_employees.head(3)
print("First 3 employees:", first_three)


# Assign the last two rows of the more_employees 
# DataFrame to the variable last_two

last_two = more_employees.tail(2)
print("Last 2 employees:", last_two)


# Get the shape of a DataFrame
employee_shape = more_employees.shape
print("Shape: ", employee_shape)

# Print a concise summary of the DataFrame using the info() 
# method to understand the data types and non-null counts.

print("Info: ")
more_employees.info()


# Task 4: Data Cleaning
# Create a DataFrame from dirty_data.csv
#  file and assign it to the variable dirty_data.
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)

# Create a copy of the dirty data 
clean_data = dirty_data.copy()

# Remove any duplicate rows from the DataFrame
clean_data.drop_duplicates(inplace=True)
print("Clean data: ", clean_data)


# Convert Age to numeric and handle missing values

clean_data["Age"]=pd.to_numeric(clean_data["Age"], errors="coerce")
print(clean_data)

# Convert Salary to numeric and replace known 
# placeholders (unknown, n/a) with NaN
clean_data["Salary"]=pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

# Fill missing numeric values (use fillna). 
#  Fill Age with the mean and Salary with the median

mean_age=clean_data["Age"].mean()
clean_data["Age"]=clean_data["Age"].fillna(mean_age)
median_salary=clean_data["Salary"].median()

clean_data["Salary"]=clean_data["Salary"].replace(["unknown","n/a","N/A"], pd.NA)
clean_data["Salary"]=clean_data["Salary"].fillna(median_salary)
print(clean_data)


# Convert Hire Date to datetime
clean_data["Hire Date"]=pd.to_datetime(clean_data["Hire Date"], format = "mixed", errors="coerce")
print(clean_data)


# Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"]=clean_data["Name"].str.strip()
clean_data["Name"]=clean_data["Name"].str.upper()

clean_data["Department"]=clean_data["Department"].str.strip()
clean_data["Department"]=clean_data["Department"].str.upper()

