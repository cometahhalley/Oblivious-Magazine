import os
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('revista.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/team')
def equipo():
    conn = get_db_connection()
    members = conn.execute('SELECT * FROM team').fetchall()
    conn.close()
    return render_template('team.html', members=members)

@app.route('/issues')
def numeros():
    conn = get_db_connection()
    issues = conn.execute('SELECT * FROM issues').fetchall()
    conn.close()
    return render_template('issues.html', issues=issues)

@app.route('/collaboration')
def colaboracion():
    return render_template('collaboration.html')

@app.route('/publication')
def publicacion():
    return render_template('publication.html')

@app.route('/contact')
def contacto():
    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
