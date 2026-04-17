from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

def load_data(filename):
    """Load JSON data from the data/ directory."""
    path = os.path.join(os.path.dirname(__file__), '../data', filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/books')
def get_books():
    """Return all books."""
    books = load_data('books.json')
    return jsonify(books)

@app.route('/music')
def get_music():
    """Return all music tracks."""
    music = load_data('music.json')
    return jsonify(music)

@app.route('/')
def index():
    return jsonify({"service": "FlexFlix", "version": "0.1.0"})

if __name__ == '__main__':
    app.run(debug=True)
