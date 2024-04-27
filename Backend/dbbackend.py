# dbbackend.py

import sqlite3

# Function to create the music table
def create_music_table():
    try:
        conn = sqlite3.connect("music.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS music (
                id INTEGER PRIMARY KEY,
                title TEXT,
                artist TEXT,
                genre TEXT,
                release_year INTEGER,
                duration TEXT
            )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error while connecting to SQLite", error)

# Function to add a new music record
def add_music_record(title, artist, genre, release_year, duration):
    try:
        conn = sqlite3.connect("music.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO music (title, artist, genre, release_year, duration) VALUES (?, ?, ?, ?, ?)",
                       (title, artist, genre, release_year, duration))
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        print("Error while connecting to SQLite", error)

# Function to retrieve all music records
def view_data():
    try:
        conn = sqlite3.connect("music.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM music")
        records = cursor.fetchall()
        conn.close()
        return records
    except sqlite3.Error as error:
        print("Error while connecting to SQLite", error)


create_music_table()
