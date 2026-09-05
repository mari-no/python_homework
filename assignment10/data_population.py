import sqlite3
import os
os.makedirs("db", exist_ok=True)
# Note, you need to create a 'db' directory if it isn't already in your workspace
DB_PATH = "db/company.db"

# Start fresh so results are predictable when re-running this script
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

# --- Schema ---
cur.executescript("""
CREATE TABLE Departments (
  department_id   INTEGER PRIMARY KEY,
  department_name TEXT NOT NULL UNIQUE,
  manager_id      INTEGER  -- (left without FK to avoid circular reference)
);
CREATE TABLE Employees (
  employee_id   INTEGER PRIMARY KEY,
  first_name    TEXT NOT NULL,
  last_name     TEXT NOT NULL,
  department_id INTEGER NOT NULL,
  title         TEXT NOT NULL,
  salary        INTEGER NOT NULL,
  hire_date     TEXT DEFAULT (date('now')),
  FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
""")

# --- Seed data ---
cur.executemany(
    "INSERT INTO Departments(department_id, department_name) VALUES (?, ?);",
    [
        (10, "Engineering"),
        (20, "Sales"),
        (30, "HR"),
        (40, "Finance"),
        (50, "R&D"),
    ],
)

employees = [
    # Engineering (dept 10)
    (1, "Alice", "Nguyen", 10, "Software Engineer",        120000, "2019-05-01"),
    (2, "Bob",   "Smith",  10, "Senior Software Engineer", 135000, "2018-07-15"),
    (3, "Carol", "Zhang",  10, "Staff Engineer",           135000, "2017-03-20"),  # tie
    (4, "David", "Lee",    10, "QA Engineer",               95000, "2021-11-02"),

    # Sales (dept 20)
    (5, "Eve",   "Martinez", 20, "Sales Associate",         90000, "2020-01-10"),
    (6, "Frank", "O'Connor", 20, "Account Executive",      110000, "2016-09-29"),
    (7, "Grace", "Kim",      20, "Sales Manager",          105000, "2015-04-12"),

    # HR (dept 30) -> avg ~68.5k (so it will be filtered out by HAVING > 70000)
    (8, "Heidi", "Brown", 30, "HR Generalist",              65000, "2022-06-03"),
    (9, "Ivan",  "Garcia", 30, "HR Manager",                72000, "2019-08-21"),

    # Finance (dept 40)
    (10, "Judy", "Wilson", 40, "Financial Analyst",        125000, "2017-02-17"),
    (11, "Karl", "Davis",  40, "Finance Director",         130000, "2014-12-09"),

    # R&D (dept 50)
    (12, "Liam", "Patel",  50, "Research Scientist",       150000, "2018-10-31"),
    (13, "Mia",  "Chen",   50, "Principal Scientist",      150000, "2013-05-07"),   # tie
]

cur.executemany(
    """INSERT INTO Employees
       (employee_id, first_name, last_name, department_id, title, salary, hire_date)
       VALUES (?, ?, ?, ?, ?, ?, ?);""",
    employees,
)

# Assign managers by employee_id for each department
cur.executemany(
    "UPDATE Departments SET manager_id = ? WHERE department_id = ?;",
    [
        (2, 10),   # Engineering -> Bob Smith
        (7, 20),   # Sales -> Grace Kim
        (9, 30),   # HR -> Ivan Garcia
        (11, 40),  # Finance -> Karl Davis
        (13, 50),  # R&D -> Mia Chen
    ],
)

print("company.db created with Departments(department_name, manager_id) and Employees.")


## 10.2 Complex JOINs
# Create and Populate a Projects Table

# create Projects table

creation = """
CREATE TABLE Projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
"""
cur.execute(creation)

# add department_ids
insertion = """
INSERT INTO Projects (name, department_id) VALUES
('Project A', (SELECT department_id FROM Departments WHERE department_name = 'HR')),
('Project B', (SELECT department_id FROM Departments WHERE department_name = 'Engineering')),
('Project C', (SELECT department_id FROM Departments WHERE department_name = 'Finance'));
"""
cur.execute(insertion)

conn.commit()
conn.close()

