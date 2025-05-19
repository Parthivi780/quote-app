from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there.",
    "Keep going. Everything you need will come to you.",
    "You are stronger than you think.",
    "Do it with passion or not at all.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts."
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
