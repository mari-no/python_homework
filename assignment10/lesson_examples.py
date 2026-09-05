##10.1 Understanding Subqueries
# 
# Subquery for MAX salary within department. 
# e.department_id specifically means the department
# of the employee currently being considered by the
#  outer query. FROM Employees AS e        -- outer Employees

import sqlite3
import os

try:
    conn = sqlite3.connect("db/company.db")
    cursor = conn.cursor()

    # Execute the query
    query = """
    SELECT department_id, employee_id, salary
    FROM Employees AS e
    WHERE salary = (
        SELECT MAX(salary)
        FROM Employees
        WHERE department_id = e.department_id
    );
    """
    cursor.execute(query)
    print(cursor.fetchall())



    ## 10.2 Complex JOINs

    # List employees working 
    # in departments responsible 
    # for a specific project:

    # Execute the query 
    query1 = """
    SELECT (e.first_name || ' ' || e.last_name) AS employee_name,
        p.name AS project_name
    FROM Employees AS e
    JOIN Projects  AS p ON e.department_id = p.department_id
    WHERE p.name = 'Project A';
    """
    cursor.execute(query1)
    print(cursor.fetchall())

    query = """
    SELECT (e.first_name || ' ' || e.last_name) AS employee_name,
        p.name AS project_name
    FROM Employees AS e
    JOIN Projects  AS p ON e.department_id = p.department_id
    WHERE p.name = 'Project B';
    """
    cursor.execute(query)
    print(cursor.fetchall())

    query = """
    SELECT (e.first_name || ' ' || e.last_name) AS employee_name,
        p.name AS project_name
    FROM Employees AS e
    JOIN Projects  AS p ON e.department_id = p.department_id
    WHERE p.name = 'Project C';
    """
    cursor.execute(query)
    print(cursor.fetchall())



    ## 10.3 Aggregation

    #Aggregation functions like MIN(), MAX(), COUNT(), 
    # and AVG() allow you to summarize data across groups.

    # Calculate the minimum and maximum salaries and the number 
    # of employees in each department.
    query = """
    SELECT department_id, 
        MIN(salary) AS min_salary, 
        MAX(salary) AS max_salary, 
        COUNT(employee_id) AS num_employees
    FROM Employees
    GROUP BY department_id;
    """
    cursor.execute(query)
    print(cursor.fetchall())

    #example which uses Inner Join so department name is used:
    query = """
    SELECT d.department_name AS department,
        MIN(e.salary)  AS min_salary,
        MAX(e.salary)  AS max_salary,
        COUNT(e.employee_id) AS num_employees
    FROM Employees AS e
    JOIN Departments AS d
    ON e.department_id = d.department_id
    GROUP BY d.department_id, d.department_name
    ORDER BY d.department_name;
    """

    cursor.execute(query)
    print(cursor.fetchall())

    ## 10.4 Aggregation with HAVING

    #The HAVING clause filters aggregated results after 
    # the GROUP BY operation.


    query = """
    SELECT d.department_name, 
        d.manager_id, 
        AVG(e.salary) AS avg_salary
    FROM Departments AS d
    JOIN Employees AS e ON d.department_id = e.department_id
    GROUP BY d.department_id
    HAVING AVG(e.salary) > 70000;
    """
    cursor.execute(query)
    print(cursor.fetchall())

    #Example which lists the manager by name
    # This version reports the manager's name instead of id 
    query = """
    WITH dept_avg AS (
    SELECT e.department_id, AVG(e.salary) AS avg_salary
    FROM Employees AS e
    GROUP BY e.department_id
    )
    SELECT d.department_name,
        (m.first_name || ' ' || m.last_name) AS manager_name,
        da.avg_salary
    FROM dept_avg AS da
    JOIN Departments AS d
    ON d.department_id = da.department_id
    LEFT JOIN Employees AS m
    ON m.employee_id = d.manager_id
    WHERE da.avg_salary > 70000;
    """
    cursor.execute(query)
    print(cursor.fetchall())


    #Key Notes: Use HAVING instead of WHERE to filter aggregated results


    ## 10.6 Transactions and Rollbacks

    #Transactions ensure that multiple database operations 
    # are completed successfully before committing them. 
    # If an error occurs, you can roll back the changes 
    # to keep the database in a consistent state.
    try:
        cursor.execute("INSERT INTO Employees (name, department_id) VALUES ('Mario Rossi', 2)")
        cursor.execute("INSERT INTO Employees (name, department_id) VALUES ('Yamada Hanako', 3)")
        conn.commit()  # Commit transaction
    except Exception as e:
        conn.rollback()  # Rollback transaction if there's an error
        print("Error:", e)


    ## 10.7 Parameterized Queries to Prevent SQL Injection
    #SQL injection is an attack where malicious input is crafted to 
    # alter the structure of a SQL query — potentially allowing 
    # an attacker to read, modify, or delete data they shouldn't 
    # have access to. Parameterized queries prevent this by 
    # treating user input as data rather than as executable SQL.


    #Vulnerable approach:
    #cursor.execute(f"SELECT * FROM Employees WHERE department_id = {department_id};")
    # or equivalently:
    #cursor.execute("SELECT * FROM Employees WHERE department_id = " + department_id + ";")

    #Secure approach
    #Parameterized queries use a ? placeholder, and the value is passed 
    # separately.
    #The database driver handles the substitution and ensures the value
    #  is always treated as data — never as SQL. Any part of a query
    #  that originates from user input or an untrusted source should
    #  be passed as a parameter this way:
    #cursor.execute("SELECT * FROM Employees WHERE department_id = ?;", 
    #            (department_id,))


    ## 10.8 Window Functions

    #SQL window functions allow for advanced analysis over a
    #  specified range of rows. For example, calculating the rank of
    #  employees within a department based on salary.

    #For each department separately, rank employees 
    # from highest salary to lowest salary.
    query = """
    SELECT (e.first_name || ' ' || e.last_name) AS employee_name,
        e.salary,
        e.department_id,
        RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS rank
    FROM Employees AS e;
    """
    cursor.execute(query)
    print(cursor.fetchall())

    ## 10.9 Date and Time Functions
    # SQL provides functions for manipulating and querying date and time data, 
    # which are useful when working with time-based analysis.


    query = """
    SELECT (e.first_name || ' ' || e.last_name) AS employee_name,
        e.hire_date,
        ROUND(JULIANDAY('now') - JULIANDAY(e.hire_date), 2) AS tenure_in_days
    FROM Employees AS e;
    """
    cursor.execute(query)
    print(cursor.fetchall())


    conn.close()
except sqlite3.Error as error:
    print(f"An error occurred: {error}")