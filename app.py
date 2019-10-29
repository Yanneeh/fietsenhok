from flask import Flask, render_template, request
app = Flask(__name__)

kluis = {
    'nummer': 1,
    'begintijd': datetime.datetime.now(),
    'user_id': 123
}

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

    # Tijdelijk
    return render_template('dashboard.html')

    # todo 1. bekijk of email bestaat
    # todo 2. bekijk of password matched met password van email, anders redirect terug naar login
    # todo 3. Bij match aanmaken van sessie en redirect naar dashboard.html met juiste parameters

@app.route('/dashboard')
def get_register():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
