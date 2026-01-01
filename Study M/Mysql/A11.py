
import mysql.connector

# Connect to MySQL Database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root@123",
            database='Jenish'
        )
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)

# Delete existing table and recreate it
def recreate_table(connection):
    try:
        cursor = connection.cursor()

        # Drop existing table
        cursor.execute("DROP DATABASE ")

        
        print("Table dropped successfully")

        # Recreate table with desired schema


        cursor.close()
        connection.commit()
    except mysql.connector.Error as error:
        print("Error recreating table:", error)

# Main function
def main():
    connection = connect_to_mysql()
    if connection:
        recreate_table(connection)
        connection.close()

if __name__ == "__main__":
    main()
