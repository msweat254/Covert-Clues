from flask import Flask, jsonify, render_template, send_from_directory
import random
import string

# Helper functions

def generate_game_id():
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(characters, k=4))
    return code

# App definition
app = Flask(__name__)

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
    data = {'message': 'Hello, World!'}
    return jsonify(data)

@app.route('/test')
def test():
    return generate_game_id()

if __name__ == '__main__':
    app.run(debug=True)
