import json
from flask import session, Flask, render_template, request, redirect
from firebase_admin import credentials, firestore, initialize_app, auth
import requests
from time import time as cur_time

app = Flask(__name__)
cred = credentials.Certificate("key.json")

initialize_app(cred)

session = {}
db = firestore.client()
grid_ref = db.collection('grid').document('grid')


def sign_in_with_email_and_password(email, password):
    url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBup8fN1NiVc008-jxIngqb_Wt1xT9eIIM'
    payload = {
    'email': email,
    'password': password,
    'returnSecureToken': True}

    response = requests.post(url, data=json.dumps(payload))

    if response.status_code == 200:
        return True
    else:
        return response.json()['error']['message']



@app.route('/')
def welcome_page():
    """
    Loads the welcome page
    """
    global session
    session = {}
    return render_template('welcome_page.html')


@app.route('/register', methods = ['POST', 'GET'])
def signup_page():
    """
    Register form
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        try:
            user = auth.create_user(email = email, password = password)
            db.collection('timer').document(email).set({'time': cur_time()})
            session['user'] = email
            success_msg = "Successfully registered!"
            return render_template('register_page.html', success_msg=success_msg)
        except:
            reg_error = "Failed to sign up. Please try again with another email or password"
            return render_template('register_page.html', reg_error=reg_error)

    else:
        return render_template('register_page.html')



@app.route('/login', methods = ['POST', 'GET'])
def login_page():
    """
    Login form
    """
    global session
    session = {}
    if 'user' in session:
        return render_template('login_page.html', success_message='You are already logged in.')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = sign_in_with_email_and_password(email, password)
            if user == True:
                session['user'] = email
                return redirect('/main_page')
            else:
                raise Exception()
        except:
            print(user)
            login_error = "Failed to log in. Please check your email and password and try again."
            return render_template('login_page.html', login_error=login_error)

    return render_template('login_page.html')


@app.route('/main_page', methods=['GET', 'POST'])
def main_page():
    '''
    Loads the main page
    '''
    if 'user' in session:
        user_limit =  db.collection('timer').document(session['user']).get().to_dict()['time']
        if user_limit > cur_time():
            timer_command = user_limit - cur_time()
        else:
            timer_command = True

        return render_template('main_page.html',
                        grid = json.dumps(grid_ref.get().to_dict()), restart_timer=True,
                          access = True, timer_command = timer_command)
    return render_template('main_page.html',
                        grid = json.dumps(grid_ref.get().to_dict()), access = False,
                          timer_command = False)



@app.route('/update_grid', methods=['GET'])
def update_data():
    """
    Sends the updated data
    """
    return json.dumps(grid_ref.get().to_dict())


@app.route('/save_grid', methods=['POST'])
def send_data():
    """
    Receives the updated data
    """
    content = request.get_json()
    grid_ref.set(content)
    return 'OK'


@app.route('/change_timere_in_db', methods=['POST'])
def change_timere_in_db():
    """
    Receives the updated data
    """
    content = request.get_json()
    db.collection('timer').document(session['user']).set({'time': cur_time() + 20})
    return 'OK'


@app.route('/account_page')
def account_page():
    return render_template('account_page.html')



if __name__ == "__main__":
    app.run(debug=True)
