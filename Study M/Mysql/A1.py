import mysql.connector
from mysql.connector import Error

def delete_database(db_name):
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='root@123'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
            print(f"Database '{db_name}' deleted successfully.")
        
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


delete_database('jenish')
