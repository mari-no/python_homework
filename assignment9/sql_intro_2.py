## Task 5: Read Data into a DataFrame

import sqlite3 
import pandas as pd 

try: 
    with sqlite3.connect("../db/lesson.db") as conn:
    # Read data from DB into DataFrame 
        query = """ SELECT line_items.line_item_id, 
                        line_items.quantity, 
                        line_items.product_id,
                        products.product_name, 
                        products.price 
                        FROM line_items JOIN products
                        ON line_items.product_id = products.product_id """ 

        df = pd.read_sql_query(query, conn) 
        print(df.head()) 

    # Add total column 
        df["total"] = df["quantity"] * df["price"] 
        print(df.head()) 

    # Group by product_id 
        df = df.groupby("product_id").agg({ "line_item_id": "count", 
                                            "total": "sum",
                                            "product_name": "first" }) 

        print(df.head()) 

        df = df.sort_values("product_name") 
        print("Sorted DataFrame: ", df)
        # Write to CSV 
        df.to_csv("order_summary.csv")

        #Print first 10 rows to check sorting
        print(df.head(10))
except sqlite3.Error as error:
    print(f"An unexpected error occurred: {error}")
except Exception as error:
    print(f"An error occurred: {error}")