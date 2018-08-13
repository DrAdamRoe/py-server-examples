## hello world server example
## adapated mostly from http://flask.pocoo.org/docs/1.0/quickstart/

# Import Flask itself
from flask import Flask
# single module version of application name, read "About the First Parameter': http://flask.pocoo.org/docs/1.0/api/#flask.Flask
app = Flask (__name__)

# decorate,  a bit of an explanation at: https://medium.com/jsguru/javascript-decorators-dac7d4b6bba3
@app.route('/')
def hello_world():
    return 'hello, flask.'

# needed for full-fledged HTML
from flask import render_template

# simple HTML page returned from external file.
@app.route('/test')
def test():
    return render_template('test.html')

# import URL library to resolve templates pointing to static resources
from flask import url_for


# simple page with inline CSS
@app.route('/csstest')
def csstest():
    return render_template('css-test.html')

# simple page with inline JS
@app.route('/jstest')
def jstest():
    return render_template('js-test.html')

# page with CSS and JS taken from external file
@app.route('/filetest')
def statictest():
    return render_template('file-test.html')