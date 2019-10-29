from flask import Flask, render_template, request, redirect, url_for, session
import datetime

app = Flask(__name__)

kluizen = [
    {
    'nummer': 1,
    'begintijd': datetime.datetime.now() - datetime.timedelta(days=2),
    'kaart_nummer': 123
    }
]

user = {
    'kaart_nummer': 123,
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
        # Tijdelijk
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('get_login'))

    # todo 1. bekijk of email bestaat
    # todo 2. bekijk of password matched met password van email, anders redirect terug naar login
    # todo 3. Bij match aanmaken van sessie en redirect naar dashboard.html met juiste parameters

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/check_kluis')
def check_kluis():

    # data = request.get_json()
    # print(data)

    # TODO: database find

    data = {
        'nummer': 1,
        'kaart_nummer': 123
    }

    for i in range(len(kluizen)):
        if data['nummer'] == kluizen[i]['nummer']:
            if data['kaart_nummer'] == kluizen[i]['kaart_nummer']:
                tijd = datetime.datetime.now() - kluizen[i]['begintijd']

                print(tijd.total_seconds() / 3600)

                kosten = 3.5 * (tijd.total_seconds() / 3600)

                print('kosten zijn {} euro'.format(kosten))

                # TODO: database update
                kluizen.pop(i)

                print('kluis {} is vrijgegeven.'.format(data['kaart_nummer']))

                return 'uitgecheckt'

    # TODO: database insert
    kluizen.append({
        'nummer': data['nummer'],
        'begintijd': datetime.datetime.now(),
        'kaart_nummer': data['kaart_nummer']
    })

    return 'ingecheckt'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
