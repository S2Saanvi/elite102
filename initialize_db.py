import sqlite3

DB_NAME = 'accounts.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS your_name
            (id integer primary key, 
            member_name text, 
            account_number integer, 
            balance text)
    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO your_name (your values here) VALUES
        ('Sajida Shaik', 01021190, '100'),
        ('Afifa Nitturu', 20100819, '250'),
        ('Hassete Amsalu', 07200917, '200')
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_database()
