from flask import Flask,render_template,url_for
import sys




app= Flask(__name__)


@app.route('/')
def index():
    return "Hello"


@app.route('/hello/<name>',
    methods=["GET","POST"],
    endpoint="hello-endpoint"
)
def hello(name):
    return f'Hello,{name}!'

@app.route('/name/<name>')
def show_name(name):
    return render_template("text.html",name=name)

with app.text_request_context():
    print(url_for("index"))
    #/hello/world
    print(url_for("hello-endpoint",name='world'))
    #/name/ichiro?page=1
    print(url_for("show_name",name="ichiro",page='1'))














app.run()