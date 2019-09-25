from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True

name_error = 'Please enter a valid username'
pass1_error = 'Please enter a valid password'
pass2_error = 'Password does not match'
email_error = 'Please enter a valid email'

@app.route('/')
def index():
    return render_template('sign-up.html')

@app.route('/', methods=['POST', 'GET'])
def sign_up():
    username = str(request.form['username'])
    pass1 = str(request.form['pass1'])
    pass2 = str(request.form['pass2'])
    email = str(request.form['email'])

    if (not username) or (username.strip() == ""):
        return render_template('sign-up.html', name_error=name_error)
    
    if (not pass1) or (pass1.strip() == ''):
        return render_template('sign-up.html', pass1_error=pass1_error, username=username)
    
    if (not pass2) or (pass2.strip() == ''):
        return render_template('sign-up.html', pass2_error=pass2_error, username=username)

    if len(username) < 3 or len(username) > 20:
        return render_template('sign-up.html', name_error=name_error, username=username)

    if len(pass1) < 3 or len(pass1) > 20:
        return render_template('sign-up.html', pass1_error=pass1_error, username=username)

    if len(pass2) < 3 or len(pass2) > 20:
        return render_template('sign-up.html', pass2_error=pass2_error, username=username)

    if pass1 != pass2:
        return render_template('sign-up.html', pass2_error=pass2_error, username=username)

    if email != '':
        if len(email) < 7:
            return render_template('sign-up.html', email_error=email_error, username=username)
        if len(email) > 7:
            email_validate = bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
        if email_validate is True:
            return render_template('sign-up.html', email_error=email_error, username=username)

    return redirect('/welcome?username=' + username)

@app.route('/welcome')
def signed_in():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()