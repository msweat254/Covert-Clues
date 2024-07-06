import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('game_lobby.db')

# Create a cursor
c = conn.cursor()

# Create the game table
c.execute('''
CREATE TABLE game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_code TEXT NOT NULL,
    word1 TEXT,
    word1color TEXT,
    word1status BOOLEAN,
    word2 TEXT,
    word2color TEXT,
    word2status BOOLEAN,
    word3 TEXT,
    word3color TEXT,
    word3status BOOLEAN,
    word4 TEXT,
    word4color TEXT,
    word4status BOOLEAN,
    word5 TEXT,
    word5color TEXT,
    word5status BOOLEAN,
    word6 TEXT,
    word6color TEXT,
    word6status BOOLEAN,
    word7 TEXT,
    word7color TEXT,
    word7status BOOLEAN,
    word8 TEXT,
    word8color TEXT,
    word8status BOOLEAN,
    word9 TEXT,
    word9color TEXT,
    word9status BOOLEAN,
    word10 TEXT,
    word10color TEXT,
    word10status BOOLEAN,
    word11 TEXT,
    word11color TEXT,
    word11status BOOLEAN,
    word12 TEXT,
    word12color TEXT,
    word12status BOOLEAN,
    word13 TEXT,
    word13color TEXT,
    word13status BOOLEAN,
    word14 TEXT,
    word14color TEXT,
    word14status BOOLEAN,
    word15 TEXT,
    word15color TEXT,
    word15status BOOLEAN,
    word16 TEXT,
    word16color TEXT,
    word16status BOOLEAN,
    word17 TEXT,
    word17color TEXT,
    word17status BOOLEAN,
    word18 TEXT,
    word18color TEXT,
    word18status BOOLEAN,
    word19 TEXT,
    word19color TEXT,
    word19status BOOLEAN,
    word20 TEXT,
    word20color TEXT,
    word20status BOOLEAN,
    word21 TEXT,
    word21color TEXT,
    word21status BOOLEAN,
    word22 TEXT,
    word22color TEXT,
    word22status BOOLEAN,
    word23 TEXT,
    word23color TEXT,
    word23status BOOLEAN,
    word24 TEXT,
    word24color TEXT,
    word24status BOOLEAN,
    word25 TEXT,
    word25color TEXT,
    word25status BOOLEAN
)
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Database and game table created successfully.")
