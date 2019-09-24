from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

name_error = ''

@app.route('/')
def index():
    return render_template('sign-up.html')

@app.route('/welcome', methods=['POST'])
def signed_in():
    username = request.form['username']
    username= str(username)
    pass1 = request.form['pass1']
    pass1 = str(pass1)
    pass2 = request.form['pass2']
    pass2 = str(pass2)
    email = request.form['email']

    if (not username) or (username.strip() == ""):
        return redirect('/')
    
    if (not pass1) or (pass1.strip() == ''):
        return redirect('/')
    
    if (not pass2) or (pass2.strip() == ''):
        return redirect('/')

    if len(username) < 3 or len(username) > 20:
        return redirect('/')

    if len(pass1) < 3 or len(pass1) > 20:
        return redirect('/')

    if len(pass2) < 3 or len(pass2) > 20:
        return redirect('/')

    if pass1 != pass2:
        return redirect('/')
    
    return render_template('welcome.html', username=username)

app.run()