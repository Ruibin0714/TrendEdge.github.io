from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)#
@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hello')
def hello():
    return 'Hello world'
    





app.run()