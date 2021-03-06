from flask import Flask, redirect, url_for
import subprocess
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    try:
        say = subprocess.check_output(['fortune'])
        res = say.decode("utf-8")
        return '<pre>'+res+'</pre>'
    except:
        return 'fail to use fortune'

@app.route('/cowsay/<message>/')
def cowsay(message):
    t = 'cowsay '+ message
    cow = subprocess.run([t], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if len(cow.stderr.decode("utf-8")) != 0:
        return 'type valid text'
    res = cow.stdout.decode("utf-8")
    return '<pre>'+res+'</pre>'

@app.route('/cowfortune/')
def cowfortune():
    say = subprocess.run(['fortune'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if len(say.stdout.decode("utf-8")) != 0:
        cow = subprocess.run(['cowsay'], input=say.stdout, stdout=subprocess.PIPE)
        res = cow.stdout.decode("utf-8")
        return '<pre>' + res + '</pre>'
    return 'fail to use fortune'
