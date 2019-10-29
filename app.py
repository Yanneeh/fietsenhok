from flask import Flask, render_template, request, redirect, url_for, session
import datetime

app = Flask(__name__)

kluizen = [
    {
    'nummer': 1,
    'begintijd': datetime.datetime.now(),
    'user_id': 123
    }
]

user = {
    'id': 123,
    'naam': 'testuser',
    'email': 'test@gmail.com',
    'password': '123'
}

# Haalt login form op
@app.route('/')
def get_login():
    return render_template('login.html')

# Verstuurd Login Form
@app.route('/login', methods=['POST'])
def post_login():
    email = request.form['email']
    password = request.form['password']

    if email == user['email'] and password == user['password']:

        print('user is ingelogd')
        session['logged_in'] == True
        # Tijdelijk
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('get_login'))

    # todo 1. bekijk of email bestaat
    # todo 2. bekijk of password matched met password van email, anders redirect terug naar login
    # todo 3. Bij match aanmaken van sessie en redirect naar dashboard.html met juiste parameters

@app.route('/dashboard')
def dashboard():

    if session['logged_in']:
        

        return render_template('dashboard.html')
    else:
        return redirect(url_for('get_login'))

@app.route('/check_kluis')
def check_kluis():

    data = request.get_json()

    print(data)

    return 'succes'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
