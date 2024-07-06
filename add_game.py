import sqlite3

# Connect to the database
conn = sqlite3.connect('game_lobby.db')
c = conn.cursor()

# Function to add a game
def add_game(game_code, words):
    # Unpack the words list into individual word, color, and status values
    game_values = [game_code]
    for word in words:
        game_values.extend([word['word'], word['color'], word['status']])
    
    # Create the SQL insert statement
    placeholders = ', '.join(['?'] * (1 + len(words) * 3))  # One placeholder for game_code + 3 for each word
    sql = f'INSERT INTO game (game_code, {", ".join([f"word{i+1}, word{i+1}color, word{i+1}status" for i in range(len(words))])}) VALUES ({placeholders})'

    # Execute the insert statement
    c.execute(sql, game_values)
    conn.commit()

# Example usage
words = [
    {'word': 'apple', 'color': 'red', 'status': False},
    {'word': 'banana', 'color': 'yellow', 'status': False},
    {'word': 'cherry', 'color': 'red', 'status': False},
    {'word': 'date', 'color': 'brown', 'status': False},
    {'word': 'elderberry', 'color': 'purple', 'status': False},
    {'word': 'fig', 'color': 'purple', 'status': False},
    {'word': 'grape', 'color': 'green', 'status': False},
    {'word': 'honeydew', 'color': 'green', 'status': False},
    {'word': 'kiwi', 'color': 'brown', 'status': False},
    {'word': 'lemon', 'color': 'yellow', 'status': False},
    {'word': 'mango', 'color': 'orange', 'status': False},
    {'word': 'nectarine', 'color': 'orange', 'status': False},
    {'word': 'orange', 'color': 'orange', 'status': False},
    {'word': 'papaya', 'color': 'orange', 'status': False},
    {'word': 'quince', 'color': 'yellow', 'status': False},
    {'word': 'raspberry', 'color': 'red', 'status': False},
    {'word': 'strawberry', 'color': 'red', 'status': False},
    {'word': 'tangerine', 'color': 'orange', 'status': False},
    {'word': 'ugli fruit', 'color': 'green', 'status': False},
    {'word': 'vanilla', 'color': 'brown', 'status': False},
    {'word': 'watermelon', 'color': 'green', 'status': False},
    {'word': 'xigua', 'color': 'green', 'status': False},
    {'word': 'yellow passion fruit', 'color': 'yellow', 'status': False},
    {'word': 'zucchini', 'color': 'green', 'status': False},
    {'word': 'blueberry', 'color': 'blue', 'status': False}
]

# Add a game with the example words
add_game('ABCD1234', words)

# Close the connection
conn.close()
