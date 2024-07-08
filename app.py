from flask import Flask, jsonify, render_template, send_from_directory, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import random
import string
import json

# Helper functions

def generate_game_id():
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(characters, k=4))
    return code

# App definition
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game_lobby.db'
db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_code = db.Column(db.String, nullable=False)
    word1 = db.Column(db.String)
    word1color = db.Column(db.String)
    word1status = db.Column(db.Boolean)
    word2 = db.Column(db.String)
    word2color = db.Column(db.String)
    word2status = db.Column(db.Boolean)
    word3 = db.Column(db.String)
    word3color = db.Column(db.String)
    word3status = db.Column(db.Boolean)
    word4 = db.Column(db.String)
    word4color = db.Column(db.String)
    word4status = db.Column(db.Boolean)
    word5 = db.Column(db.String)
    word5color = db.Column(db.String)
    word5status = db.Column(db.Boolean)
    word6 = db.Column(db.String)
    word6color = db.Column(db.String)
    word6status = db.Column(db.Boolean)
    word7 = db.Column(db.String)
    word7color = db.Column(db.String)
    word7status = db.Column(db.Boolean)
    word8 = db.Column(db.String)
    word8color = db.Column(db.String)
    word8status = db.Column(db.Boolean)
    word9 = db.Column(db.String)
    word9color = db.Column(db.String)
    word9status = db.Column(db.Boolean)
    word10 = db.Column(db.String)
    word10color = db.Column(db.String)
    word10status = db.Column(db.Boolean)
    word11 = db.Column(db.String)
    word11color = db.Column(db.String)
    word11status = db.Column(db.Boolean)
    word12 = db.Column(db.String)
    word12color = db.Column(db.String)
    word12status = db.Column(db.Boolean)
    word13 = db.Column(db.String)
    word13color = db.Column(db.String)
    word13status = db.Column(db.Boolean)
    word14 = db.Column(db.String)
    word14color = db.Column(db.String)
    word14status = db.Column(db.Boolean)
    word15 = db.Column(db.String)
    word15color = db.Column(db.String)
    word15status = db.Column(db.Boolean)
    word16 = db.Column(db.String)
    word16color = db.Column(db.String)
    word16status = db.Column(db.Boolean)
    word17 = db.Column(db.String)
    word17color = db.Column(db.String)
    word17status = db.Column(db.Boolean)
    word18 = db.Column(db.String)
    word18color = db.Column(db.String)
    word18status = db.Column(db.Boolean)
    word19 = db.Column(db.String)
    word19color = db.Column(db.String)
    word19status = db.Column(db.Boolean)
    word20 = db.Column(db.String)
    word20color = db.Column(db.String)
    word20status = db.Column(db.Boolean)
    word21 = db.Column(db.String)
    word21color = db.Column(db.String)
    word21status = db.Column(db.Boolean)
    word22 = db.Column(db.String)
    word22color = db.Column(db.String)
    word22status = db.Column(db.Boolean)
    word23 = db.Column(db.String)
    word23color = db.Column(db.String)
    word23status = db.Column(db.Boolean)
    word24 = db.Column(db.String)
    word24color = db.Column(db.String)
    word24status = db.Column(db.Boolean)
    word25 = db.Column(db.String)
    word25color = db.Column(db.String)
    word25status = db.Column(db.Boolean)

def get_game_by_id(game_code):
    game = Game.query.filter(Game.game_code == game_code).first()
    return game

@app.route('/')
def index():
    return render_template('landing-page.html')

@app.route('/codemaster/<game_code>')
def codemaster(game_code):
    return render_template('hint-giver.html')

@app.route('/words.txt')
def serve_words():
    return send_from_directory('static', 'words.txt')

@app.route('/api/create_game')
def get_data():
    id = generate_game_id()
    word_color_pairs = assign_words_and_colors()
    
    game_data = {
        'game_code': id
    }
    for i, (word, color) in enumerate(word_color_pairs, 1):
        game_data[f'word{i}'] = word
        game_data[f'word{i}color'] = color
        game_data[f'word{i}status'] = False

    new_game = Game(**game_data)
    db.session.add(new_game)
    db.session.commit()
    
    return redirect(url_for('codemaster', game_code=id))

@app.route('/api/get_game_data/<game_code>')
def get_game_data(game_code):
    # Get data from database.
    game = get_game_by_id(game_code)
    info = {
        "id": game_code,
        "word1": game.word1,
        "word1color": game.word1color,
        "word1status": game.word1status,
        "word2": game.word2,
        "word2color": game.word2color,
        "word2status": game.word2status,
        "word3": game.word3,
        "word3color": game.word3color,
        "word3status": game.word3status,
        "word4": game.word4,
        "word4color": game.word4color,
        "word4status": game.word4status,
        "word5": game.word5,
        "word5color": game.word5color,
        "word5status": game.word5status,
        "word6": game.word6,
        "word6color": game.word6color,
        "word6status": game.word6status,
        "word7": game.word7,
        "word7color": game.word7color,
        "word7status": game.word7status,
        "word8": game.word8,
        "word8color": game.word8color,
        "word8status": game.word8status,
        "word9": game.word9,
        "word9color": game.word9color,
        "word9status": game.word9status,
        "word10": game.word10,
        "word10color": game.word10color,
        "word10status": game.word10status,
        "word11": game.word11,
        "word11color": game.word11color,
        "word11status": game.word11status,
        "word12": game.word12,
        "word12color": game.word12color,
        "word12status": game.word12status,
        "word13": game.word13,
        "word13color": game.word13color,
        "word13status": game.word13status,
        "word14": game.word14,
        "word14color": game.word14color,
        "word14status": game.word14status,
        "word15": game.word15,
        "word15color": game.word15color,
        "word15status": game.word15status,
        "word16": game.word16,
        "word16color": game.word16color,
        "word16status": game.word16status,
        "word17": game.word17,
        "word17color": game.word17color,
        "word17status": game.word17status,
        "word18": game.word18,
        "word18color": game.word18color,
        "word18status": game.word18status,
        "word19": game.word19,
        "word19color": game.word19color,
        "word19status": game.word19status,
        "word20": game.word20,
        "word20color": game.word20color,
        "word20status": game.word20status,
        "word21": game.word21,
        "word21color": game.word21color,
        "word21status": game.word21status,
        "word22": game.word22,
        "word22color": game.word22color,
        "word22status": game.word22status,
        "word23": game.word23,
        "word23color": game.word23color,
        "word23status": game.word23status,
        "word24": game.word24,
        "word24color": game.word24color,
        "word24status": game.word24status,
        "word25": game.word25,
        "word25color": game.word25color,
        "word25status": game.word25status
    }
    print(jsonify(info))
    return(jsonify(info))

def assign_words_and_colors():
    with open('./static/words.txt', 'r') as file:
        words = [line.strip() for line in file if line.strip()]

    random.shuffle(words)
    colors = (
        ['blue'] * 8 +
        ['red'] * 8 +
        ['white'] * 8 +
        ['black']
    )
    random.shuffle(colors)

    return list(zip(words[:25], colors))

@app.route('/game_created/<game_code>')
def game_created(game_code):
    return f"Game with code {game_code} has been created."

@app.route('/test')
def test():
    return generate_game_id()

@app.route('/game/<game_code>')
def play_game(game_code):
    return render_template('guesser.html')

@app.route('/api/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    game_code = data.get('game_code')  # Get the game code from the JSON data
    word_id = data.get('value')  # Get the word ID from the JSON data

    # Map word_id to the correct word_status column
    word_column = f'word{word_id}status'

    # Update the word status in the database
    game = get_game_by_id(game_code)
    
    if game:
        setattr(game, word_column, True)
        db.session.commit()
        print(f"Updated word ID {word_id} to status 1 for game {game_code}")

        # Example response
        response = {
            'status': 'success',
            'updated_word_id': word_id,
            'game_code': game_code
        }
    else:
        response = {
            'status': 'error',
            'message': 'Game with code, '+ game_code+' not found'
        }

    return jsonify(response)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
