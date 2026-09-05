## Task 1: Complex JOINs with Aggregation
#Find the total price of each of the first 5 orders.  
#
import sqlite3
import os

try:
    #Connect to DB
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()

    # Execute the query
    query = """
    SELECT o.order_id, 
    SUM(p.price* l.quantity) AS total_price
    FROM orders AS o 
    JOIN line_items AS l ON o.order_id = l.order_id
    JOIN products AS p ON p.product_id = l.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5
    """
    cursor.execute(query)
    print(cursor.fetchall())


    conn.close()

except sqlite3.Error as error:
    print(f"An error occurred: {error}")


## Task 2: Understanding Subqueries
#For each customer, find the average price of their orders. 
#  This can be done with a subquery. 

try:
    #Connect to DB
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()
    # Execute the query
    query = """


    SELECT customer_name, AVG(total_price) AS average_total_price
     
    FROM customers AS cus
    LEFT JOIN (SELECT o.customer_id AS customer_id_b, 
    SUM(p.price* l.quantity) AS total_price
    FROM orders AS o 
    JOIN line_items AS l ON o.order_id = l.order_id
    JOIN products AS p ON p.product_id = l.product_id
    GROUP BY o.order_id) AS order_totals
    ON cus.customer_id = order_totals.customer_id_b
    GROUP BY customers.customer_id

    """
    cursor.execute(query)
    print(cursor.fetchall())

    conn.close()

except sqlite3.Error as error:
    print(f"An error occurred: {error}")


##Task 3: An Insert Transaction Based on Data
# create a new order for the customer named Perez 
# and Sons.  
# The employee creating the order is Miranda Harris. 
#  The customer wants 10 of each of the 5 least expensive 
# products. 
# 
try:
    #Connect to DB
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = 1")
    cursor.execute(  """
                SELECT customer_id FROM customers WHERE
                customer_name LIKE 'Perez and Sons' """)
    customer_id = cursor.fetchone()[0]
    cursor.execute("""
                SELECT product_id FROM products 
                ORDER BY price
                LIMIT 5
            """)
    product_ids = cursor.fetchall()
    cursor.execute("""
                SELECT employee_id FROM employees WHERE
                first_name LIKE 'Miranda' 
                AND last_name LIKE 'Harris'""")
    employee_id = cursor.fetchone()[0]
    cursor.execute("""INSERT INTO orders (customer_id, employee_id , date) 
                   VALUES (?, ?, ?)
                   RETURNING order_id""",
                   (customer_id, employee_id , '2026-08-06'))
    order_id = cursor.fetchone()[0]


    for product in product_ids:

        cursor.execute(  "INSERT INTO line_items(order_id, product_id, quantity) VALUES (?, ?, ?)",
                   (order_id, product[0], 10)
                   )
    conn.commit()  # Commit transaction

    query = ("""SELECT o.order_id, l.line_item_id,  l.quantity, p.product_name
    FROM orders AS o 
    JOIN line_items AS l 
    ON o.order_id = l.order_id
    JOIN products AS p
    ON l.product_id = p.product_id
     WHERE o.order_id = ? """)
    cursor.execute(query, (order_id,))
    print(f"Here is all the info we added for order {order_id}: {cursor.fetchall()}")
    
    
    conn.close()
# print out the list of line_item_ids for the order
#  along with the quantity and product name for each.


except Exception as e:
    conn.rollback()  # Rollback transaction if there's an error
    print("Error:", e)



## Task 4: Aggregation with HAVING
# Find all employees associated with more than 5 orders. 

try:
    #Connect to DB
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()
    query_empl = ( """
                SELECT e.employee_id,
                e.first_name, e.last_name, 
                COUNT(o.order_id) AS order_count
                FROM employees AS e 
                JOIN orders AS o
                ON e.employee_id = o.employee_id
                GROUP BY e.employee_id
                HAVING COUNT(o.order_id)>5 """)

    cursor.execute(query_empl)
    print(f" Here are all the employees with more than 5 orders: {cursor.fetchall()}")
    
    conn.close()
    
except sqlite3.Error as error:
    print(f"An error occurred: {error}")