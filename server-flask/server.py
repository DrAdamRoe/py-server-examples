## hello world server example
## adapated mostly from http://flask.pocoo.org/docs/1.0/quickstart/

# Import Flask itself
from flask import Flask
# single module version of application name, read "About the First Paramter': http://flask.pocoo.org/docs/1.0/api/#flask.Flask
app = Flask (__name__)


# decorate,  read first part of: https://medium.com/jsguru/javascript-decorators-dac7d4b6bba3
@app.route('/')
def hello_world():
    return 'hello, flask.'

from flask import render_template

@app.route('/test')
def test():
    return render_template('test.html')

# import URL library to resolve templates pointing to static resources
from flask import url_for

@app.route('/csstest')
def csstest():
    return render_template('css-test.html')

@app.route('/jstest')
def jstest():
    return render_template('js-test.html')

@app.route('/filetest')
def statictest():
    return render_template('file-test.html')