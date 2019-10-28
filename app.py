from flask import Flask, render_template, request
app = Flask(__name__)

# Haalt login form op
@app.route('/')
def get_login():
    return render_template('login.html')

# Verstuurd Login Form
@app.route('/login', methods=['POST'])
def post_login():
    email = request.form['email']
    password = request.form['password']

    # Tijdelijk
    return render_template('dashboard.html')

    # todo 1. bekijk of email bestaat
    # todo 2. bekijk of password matched met password van email, anders redirect terug naar login
    # todo 3. Bij match aanmaken van sessie en redirect naar dashboard.html met juiste parameters

@app.route('/register', methods=['GET'])
def get_register():
    return render_template('dashboard.html')
