import sqlite3
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_bmi():
    conn = sqlite3.connect('bmi.db')

    # Create a cursor object
    cursor = conn.cursor()
    # Execute a SQL query to fetch all data from the measurements table
    cursor.execute("SELECT * FROM measurements")

    # Fetch all rows
    rows = cursor.fetchall()

    # Convert the fetched data into a pandas DataFrame
    df = pd.DataFrame(rows, columns=['id', 'weight', 'height', 'bmi', 'date'])

    # Create a Figure object and add a subplot to it
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)

    # Plot the 'bmi' column as a bar chart
    plot.bar(df['date'], df['bmi'])
    
    plot.set_facecolor('none')
    # Add x and y labels with white color
    plot.set_title('Your BMI History', color='white')
    plot.set_xlabel('Date', color='white')
    plot.set_ylabel('BMI', color='white')
    
    # Set the color of the axis lines to white
    plot.spines['bottom'].set_color('white')
    plot.spines['left'].set_color('white')
    plot.spines['top'].set_color('#212121')
    plot.spines['right'].set_color('#212121')
    
    # Set the color of the x and y tick labels to white
    plot.tick_params(axis='x', colors='white')
    plot.tick_params(axis='y', colors='white')
    
    
    return fig
    # Close the connection
    conn.close()
