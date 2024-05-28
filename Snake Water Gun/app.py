from flask import Flask, request, jsonify, send_from_directory
import random

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def styles():
    return send_from_directory('.', 'styles.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('./images', filename)

@app.route('/play')
def play():
    user_choice = request.args.get('choice')
    choices = ['snake', 'water', 'gun']
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)
    return jsonify({'result': result, 'computer_choice': computer_choice})

def determine_winner(user, computer):
    if user == computer:
        return f"It's a tie! Both chose {user}."
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return f"You win! {user} beats {computer}."
    else:
        return f"You lose! {computer} beats {user}."

if __name__ == '__main__':
    app.run(debug=True)
