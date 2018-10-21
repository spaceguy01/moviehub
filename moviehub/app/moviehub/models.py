from app import db
from datetime import datetime

class Studio(db.Model):
    __tablename__ = 'studio'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Studio name is {self.name}'


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False, index=True)
    director = db.Column(db.String(200))
    rating = db.Column(db.String(20))
    runtime = db.Column(db.Integer)
    cast = db.Column(db.String(250))
    genre = db.Column(db.String(250))
    year = db.Column(db.Integer)
    storyline = db.Column(db.Text)
    image = db.Column(db.String(200), unique=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship

    stud_id = db.Column(db.Integer, db.ForeignKey('studio.id'))

    def __init__(self, title, director, rating, runtime, cast, genre, year, storyline, poster, stud_id):

        self.title = title
        self.director = director
        self.rating = rating
        self.runtime = runtime
        self.cast = cast
        self.genre = genre
        self.year = year
        self.storyline = storyline
        self.poster = poster
        self.stud_id = stud_id

    def __repr__(self):
        return f'{self.title} directed by {self.director}'
