from flask import Flask, render_template, jsonify, request
from werkzeug.security import generate_password_hash

from . import db


app = Flask(__name__)

db.init_app(app)

MOVIES = [
    {
    'id': 1,
    'title': 'Frozen Trails in Ottawa',
    'production': 'Canada',
    'year': '2023' 
    },
    {
    'id': 2,
    'title': 'Disastrously Hilarious: The Misadventures of a Clumsy Chef',
    'production': 'USA',
    'year': '2023' 
    
    },
    {
    'id': 3,
    'title': 'Lunar Koala Adventures',
    'production': 'USA',
    'year': '2022' 
    },
    {
    'id': 4,
    'title': 'Frozen Trails in Otta',
    'production': 'South Korea',
    'year': '2023' 
    }
]

@app.route("/")
def baton():
    database = db.get_db()
    movies = database.execute('select * from movie_description')
    
    return render_template('home.html', 
                          movies=movies)

@app.route("/")
def hello_masha():
    
    return render_template('home.html', 
                          movies=MOVIES,
                          theater_location='Turku',) 

@app.route("/api/movies")
def list_movies():
    return jsonify(MOVIES)


# @app.route("/movie/{movie_id}")
# def 


@app.route("/calendar")
def calendar():
    calendar_entries = None

    database = db.get_db()

    calendar_entries = database.execute(
        "SELECT * FROM schedule"
    )

    return render_template(
        'calendar.html',
        calendar_entries=calendar_entries,
    )

@app.route("/movie_description/<movie_id>")
def info(movie_id: int):
    description = None

    database = db.get_db()

    description = database.execute(
        "SELECT * FROM movie_description WHERE id = ?",
        (movie_id)
    )
    return render_template(
        'movie_description.html',
        movie=dict(description.fetchone())
    )

@app.route('/submit', methods=['POST'])
def show_data():
    database = db.get_db()
    
    database.execute(
        "INSERT INTO schedule (movie_title, date, time, movie_link) VALUES (?, ?, ?, ?)",
        (request.form['fname'], request.form['date'], request.form['time'], request.form['link']),
    )
    database.commit()

    return render_template('home.html', 
                          movies=MOVIES,
                          theater_location='Turku',) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

