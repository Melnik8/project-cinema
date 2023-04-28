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
    'title': 'Frozen Trails of Ottawa',
    'production': 'USA'
    
    },
    {
    'id': 3,
    'title': 'Frozen Trolls in Ottawaland',
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

LOL = [{'lol laugh'}]

@app.route("/")
def hello_masha():
    return render_template('home.html', 
                          movies=MOVIES,
                          theater_location='Turku',) 

@app.route("/api/movies")
def list_movies():
    return jsonify(MOVIES)

@app.route('/submit', methods=['POST', 'GET'])
def show_data():
    database = db.get_db()
    
    database.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)",
        (request.args['fname'], generate_password_hash(request.args['fname'])),
    )
    return jsonify({'fname': request.args['fname']})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

