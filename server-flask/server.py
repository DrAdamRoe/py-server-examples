

# Import Flask itself
from flask import Flask
# single module version of application name, read "About the First Paramter': http://flask.pocoo.org/docs/1.0/api/#flask.Flask
app = Flask (__name__)


## hack to set environment variable, not particularly robust but avoids extra setp
## alternative method to issuing 'export FLASK_APP=server.py' at the command line.

# get filename (without complete path)
import os
this_filename=os.path.basename(__file__)

# export FLASK_APP variable, check return code.
# new to python 3.5: https://docs.python.org/3/library/subprocess.html
import subprocess
cmd = "export FLASK_APP=%s" % this_filename
out = subprocess.run(cmd, shell=True )
out.check_returncode()

# decorate,  read first part of: https://medium.com/jsguru/javascript-decorators-dac7d4b6bba3
@app.route('/')
def hello_world():
    return 'hello, flask.'