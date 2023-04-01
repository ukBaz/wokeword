from flask import Flask, render_template

import word_generator

app = Flask(__name__)

# export FLASK_APP=hello
# export FLASK_DEBUG=true


@app.route('/')
def index():
    data = {'wokeword': word_generator.new()}
    return render_template('index.html', data=data)
