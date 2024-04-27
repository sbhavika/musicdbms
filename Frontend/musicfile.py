import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('music.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute SQL command to create the music table
cursor.execute('''CREATE TABLE IF NOT EXISTS music (
                    id INTEGER PRIMARY KEY,
                    Title TEXT,
                    Artist TEXT,
                    Genre TEXT,
                    ReleaseYear INTEGER,
                    Duration TEXT
                  )''')

# Commit the changes and close the connection
conn.commit()
conn.close()

# Print a message indicating that the database and table have been created
print("music.db file created successfully with a music table.")
