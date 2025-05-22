import sqlite3

connection = sqlite3.connect('revista.db')

# Crear estructura
with open('schema.sql') as f:
    connection.executescript(f.read())

# Insertar datos de prueba
cur = connection.cursor()
cur.execute(
    "INSERT INTO issues (issue_number, title, description, cover_image, published_date) VALUES (?, ?, ?, ?, ?)",
    (12, '12. War, guilt and regret', 'Stories exploring conflict and its emotional aftermath.', 'PORTADA12.webp', '2025-05-29')
)

cur.execute(
    "INSERT INTO issues (issue_number, title, description, cover_image, published_date) VALUES (?, ?, ?, ?, ?)",
    (11, '11. Fantasy and science fiction', 'A journey into alternate realities and impossible futures.', 'PORTADA11.webp', '2025-02-21')
)

cur.execute("INSERT INTO team (name, role, photo, description) VALUES (?, ?, ?, ?)",
            ('Andrea Falaguera', 'director', 'drea.webp', 'Founding director and main coordinator of Oblivious Magazine. She holds a degree in Modern Languages and Literatures from the University of Valencia with a major in French and a minor in English Studies.')
)

cur.execute("INSERT INTO team (name, role, photo, description) VALUES (?, ?, ?, ?)",
            ('Natalia Hernández', 'vice-director', 'natalia.webp', 'Data science student at UPV. When she is not analyzing data for career work, she is dedicated to collecting information about anything she finds interesting (typical intp). He is also passionate about learning languages, reading and traveling.')
)

cur.execute("INSERT INTO team (name, role, photo, description) VALUES (?, ?, ?, ?)",
            ('Aída Sánchez-Gadeo', 'vice-director', 'aida.webp', 'She is a language and literature student and has dreamed of being a writer since she was a little girl. She is also passionate about cats, potato chips and traveling. One of her favorite hobbies is to contradict the director.')
)

connection.commit()
connection.close()
