from flask import Flask
from flask import Markup
from flask import request, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'yurii' and request.form['password'] == 'fallout':
            return 'Hello World' #log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run()
