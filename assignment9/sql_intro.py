## Task 1: Create a New SQLite Database

import sqlite3

# Connect to a new SQLite database

# The "with" statement commits successful transactions and rolls back transactions which cause exceptions within the block.  
# You must close the connection explicitly with conn.close().


with  sqlite3.connect("../db/magazines.db") as conn:  # Create the file here, so that it is not pushed to GitHub!
    print("Database created and connected successfully.")
# Connect to the database

    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = 1")

## Task 2: Define Database Structure
# Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER ,
        FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL,
        subscriber_address TEXT NOT NULL 
   )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
        
        FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
            
   ) 
   """)

    print("Tables created successfully.")




##Task 3: Populate Tables with Data


    def add_publisher(cursor, name):
        try:
            cursor.execute(
                "INSERT INTO Publishers (name) VALUES (?)",
                (name,)
            )
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")


    def add_magazine(cursor, magazine_name, publisher_name):
        try:
# Find publisher_id
            cursor.execute(
                "SELECT publisher_id FROM Publishers WHERE name = ?",
                ( publisher_name,)
                )
            result = cursor.fetchone()

            if len(result) > 0:
                publisher_id = result[0]
            else:
                print(f"There was no publisher named {publisher_name}.")
                return

            cursor.execute(
                "INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?, ?)",
                (magazine_name, publisher_id)
            )
        except sqlite3.IntegrityError:
            print(f"{magazine_name} is already in the database.")


    def add_subscriber(cursor, subscriber_name, subscriber_address):
        try:
            cursor.execute(
                    """
                    SELECT *
                    FROM Subscribers
                    WHERE subscriber_name = ? AND subscriber_address = ?
                    """,
                    (subscriber_name, subscriber_address)
                )

            if cursor.fetchone():
                print(f"{subscriber_name}, {subscriber_address} is already in the database.")
                return

            cursor.execute(
                    """
                    INSERT INTO Subscribers (subscriber_name, subscriber_address)
                    VALUES (?, ?)
                    """,
                    (subscriber_name, subscriber_address)
                )
        except sqlite3.IntegrityError:
                print(f"{subscriber_name}, {subscriber_address} is already in the database.")


    def add_subscription(cursor, subscriber_name, magazine_name, expiration_date): 

# Find subscriber 
        cursor.execute( "SELECT * FROM Subscribers WHERE subscriber_name = ?", 
                       (subscriber_name,) )
        results = cursor.fetchall() 
        if len(results) > 0: 
            subscriber_id = results[0][0] 
        else:
            print(f"There was no subscriber named {subscriber_name}.") 
            return 
# Find magazine 
        cursor.execute( "SELECT * FROM Magazines WHERE magazine_name = ?",
                        (magazine_name,) )
        results = cursor.fetchall() 
        if len(results) > 0:
            magazine_id = results[0][0]
        else: 
            print(f"There was no magazine named {magazine_name}.") 
            return 
# Check if this subscription already exists 
        cursor.execute( """ SELECT * FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ? """, 
                       (subscriber_id, magazine_id) ) 
        results = cursor.fetchall() 
        if len(results) > 0:
            print( f"{subscriber_name} is already subscribed to {magazine_name}." )
            return
# Create subscription 
        cursor.execute( """ INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?) """,
                        (subscriber_id, magazine_id, expiration_date) )
    


 ###filling Publisher table with data
    add_publisher(cursor, "Lee Cooper"),
    add_publisher(cursor, "Mary Styr"),
    add_publisher(cursor, "Leo Tolstoj"),
    add_publisher(cursor, "Fedor Dostoevskij"),

## filling Magazines data
   
    add_magazine(cursor, "World", "Lee Cooper")
    add_magazine(cursor, "Sun","Mary Styr")
    add_magazine(cursor, "Rain", "Lee Cooper")
    add_magazine(cursor, "Rainbow", "Lee Cooper")
    add_magazine(cursor, "Terrace", "Fedor Dostoevskij")
    add_magazine(cursor, "Times", "Leo Tolstoj")


## filling Subscribers data

    add_subscriber(cursor, "Jihn Doe", "123 Kyla str")
    add_subscriber(cursor, "John Smith", "123 Main str")
    add_subscriber(cursor, "Mary Monro", "23 Byron str")
    add_subscriber(cursor, "Ken Smith", "23 Astee str")

##filling Subscriptions data
    add_subscription(cursor, "Jihn Doe", "World", "02/08/2027")
    add_subscription(cursor, "Jihn Doe", "Sun", "07/10/2027")
    add_subscription(cursor, "Jihn Doe", "Rainbow", "12/18/2027")
    add_subscription(cursor, "John Smith", "World", "09/08/2027")
    add_subscription(cursor, "Mary Monro", "Terrace", "11/01/2028")
    add_subscription(cursor, "Mary Monro", "Times", "11/11/2028")
    add_subscription(cursor, "Ken Smith", "Rain", "12/11/2027")

    conn.commit()
## Task 4: Write SQL Queries
# a query to retrieve all information from the subscribers table.

    cursor.execute("SELECT * FROM Subscribers;")
    query_one = cursor.fetchall()
    print(query_one)
# a query to retrieve all magazines sorted by name.
    cursor.execute("SELECT * FROM Magazines ORDER BY magazine_name desc;")
    query_two = cursor.fetchall()
    print(query_two)

# a query to find magazines for a particular publisher
    cursor.execute("""SELECT * FROM Magazines 
                    JOIN Publishers 
                    ON Magazines.publisher_id = Publishers.publisher_id
                    WHERE Publishers.name = 'Fedor Dostoevskij';""")
    query_three = cursor.fetchall()
    print(query_three)



conn.close()

