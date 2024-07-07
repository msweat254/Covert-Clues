from flask import Flask, jsonify, render_template, send_from_directory, url_for, redirect
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
    word15= db.Column(db.String)
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

@app.route('/')
def index():
    return render_template('landing-page.html')

@app.route('/codemaster')
def codemaster():
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
    
    return redirect(url_for('game_created', game_code=id))

def assign_words_and_colors():
    with open('/Users/michaelsweat1/Documents/Python Scripts/Covert Clues/static/words.txt', 'r') as file:
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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
