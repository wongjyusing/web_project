from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('hello.html')

@app.route('/hello/<name>')
def hello_xxxx(name):
    context = f'hello,{name}'
    #return 'Hello, World!'
    #return render_template('hello.html')
    return context
@app.route('/hi/<name>')
def hi_xxxx(name):
    context = f'hi,{name}'
    return render_template('hi.html',context=context)
