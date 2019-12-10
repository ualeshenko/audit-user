from flask import Flask, redirect, url_for
from flask import Markup, request, render_template
import mysql.connector

def mysql_table():
    connect = mysql.connector.connect(
      host="localhost",
      user="dev",
      passwd="fallout",
      database="audit"
    )

    cur = connect.cursor()

    cur.execute("SELECT * FROM hosts") # (hostname, users) VALUES (%s, %s)"
    data = cur.fetchall()
    return render_template('table_hosts.html', data=data)



app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'yurii' and request.form['password'] == 'fallout':
            return mysql_table()
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error) #mysql_table()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)
