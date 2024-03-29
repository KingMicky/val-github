from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

# Romantic quotes for Valentine's Day
romantic_quotes = [
    "Love is not just looking at each other, it's looking in the same direction. - Antoine de Saint-Exupéry",
    "The best and most beautiful things in the world cannot be seen or even touched. They must be felt with the heart. - Helen Keller",
    "I have waited for this opportunity for more than half a century, to repeat to you once again my vow of eternal fidelity and everlasting love. - Gabriel Garcia Marquez",
    "Love is an endless mystery, for it has nothing else to explain it. - Rabindranath Tagore",
    "You know you're in love when you can't fall asleep because reality is finally better than your dreams. - Dr. Seuss",
]

NonRomantic_quotes = [
    "Are you sure? you know you can go back and pick the right answer rii?",
    "I think you picked the wrong answer",
    "LoL"
     ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/valentine', methods=['GET'])
def get_valentine_quote():
    initial_quote = random.choice(romantic_quotes)
    different_quote = random.choice(NonRomantic_quotes)
    return jsonify({'quote': initial_quote})

@app.route('/will_you_be_my_valentine', methods=['POST'])
def ask_valentine():
    answer = request.form.get('answer')

    if answer == 'yes':
        response = "You said 'Yes'! 💖"
    elif answer == 'no':
        response = "You said 'No'! 😢"
        different_quote = random.choice(NonRomantic_quotes)
        return render_template('no_response.html', response=response, different_quote=different_quote)
    else:
        response = "Invalid answer. Please choose 'Yes' or 'No'."
        
    print("Received answer:", answer)
    
    initial_quote = random.choice(romantic_quotes)
    return render_template('response.html', response=response, initial_quote=initial_quote)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True ,port=80)