import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# Connect to the SQLite database
conn = sqlite3.connect('bmi.db')
cursor = conn.cursor()
def insert_measurement(weight, height,bmi):

    # Create a table to store weight, height, BMI, and date
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL,
            height REAL,
            bmi REAL,
            date TEXT
        )
    ''')

    # Get the current date
    current_date = date.today().strftime("%Y-%m-%d")

    # Insert the measurements into the database
    cursor.execute('''
        INSERT INTO measurements (weight, height, bmi, date)
        VALUES (?, ?, ?, ?)
    ''', (weight, height, bmi, current_date))

    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

