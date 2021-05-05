from flask import Flask, redirect, url_for
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    out = subprocess.check_output('fortune')
    res = out.decode("utf-8")
    return '<pre>'+res+'</pre>'

@app.route('/cowsay/<message>/')
def cowsay(message):
    t = 'cowsay '+ message
    cow = subprocess.run([t], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = cow.stdout.decode("utf-8")
    return '<pre>'+res+'</pre>'

@app.route('/cowfortune/')
def cowfortune():
    say = subprocess.run(['fortune'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    mi = say.stdout.decode("utf-8")
    t = 'cowsay '+ mi
    cow = subprocess.run([t], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = cow.stdout.decode("utf-8")
    return '<pre>'+res+'</pre>'

