import csv
import mysql.connector
from datetime import datetime
import random

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="User"
)
cursor = conn.cursor()

# Open the CSV file and read data
with open('Movies.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)  # Handle quoted fields properly
    next(reader)  # Skip header if present
    
    for row in reader:
        if len(row) != 10:  # Ensure row has exactly 10 columns
            print(f"Skipping row due to incorrect column count: {row}")
            continue
        
        # Strip spaces and convert empty values to None
        row = [col.strip() if col.strip() else None for col in row]

        # Convert rating format (9,9 → 9.9)
        if row[6]:  
            row[6] = float(row[6].replace(',', '.'))  # Convert to float properly

        # Convert start_to_end_time to total minutes
        if row[5]:  
            try:
                h, m, s = map(int, row[5].split(':'))  # Convert "HH:MM:SS" to integers
                row[5] = h * 60 + m + (s / 60)  # Convert to total minutes
            except ValueError:
                print(f"Skipping row due to invalid time format: {row}")
                continue

        # Convert release_at to an integer (only year)
        if row[7]:  
            try:
                row[7] = int(row[7])  # Ensure it's an integer
            except ValueError:
                print(f"Skipping row due to invalid release year: {row}")
                continue

        sql = """
        INSERT INTO drf_api_content (id, title, description, image_url, trailer_url, 
        start_to_end_time, rating, release_at, created_at, updated_at) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(sql, tuple(row))
        except mysql.connector.Error as err:
            print(f"Error inserting row: {err}")

# Commit changes
conn.commit()

# Verify inserted data
cursor.execute("SELECT * FROM drf_api_content LIMIT 10")  # Fetch 10 records as sample
data = cursor.fetchall()

print("Inserted Data:")
for row in data:
    print(row)

# Close connection
cursor.close()
conn.close()

print("Data inserted and verified successfully!")
