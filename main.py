from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('sign-up.html')

@app.route('/welcome', methods=['POST'])
def signed_in():
    username = request.form['username']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']
    email = request.form['email']
    
    return render_template('welcome.html', username=username)

app.run()