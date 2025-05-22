import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('revista.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/equipo')
def equipo():
    conn = get_db_connection()
    members = conn.execute('SELECT * FROM team').fetchall()
    conn.close()
    return render_template('equipo.html', members=members)

@app.route('/numeros')
def numeros():
    conn = get_db_connection()
    issues = conn.execute('SELECT * FROM issues').fetchall()
    conn.close()
    return render_template('numeros.html', issues=issues)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)