from flask import Flask, render_template
from random import randrange
from english_words import english_words_set
from flask.templating import render_template

words = list(english_words_set)
links = ['/numbers', '/letters', '/words']

url = "http://127.0.0.1:5000"

for i in links:
    index = links.index(i)
    links[index] = url+i

    
app = Flask(__name__)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route('/numbers')
def randomjson():
    no = {
    'number':randrange(0,100000000)
    }
    return no

# @app.route('/')
# def hello():
#     return 'Welcome to the randomness API! '

@app.route('/letters')
def letterjson():
    letter = {
        'letter':letters[randrange(0, len(letters))]
    }
    return letter

@app.route('/words')
def wordsjson():
    word = {
        'word':words[randrange(0, len(words))]
    }
    return word

@app.route("/")
def site_map():
    return render_template('index.html', links = links)

if __name__ == '__main__':
    app.run()