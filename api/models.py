from .extensions import db


movies_actors = db.Table('movies_actors',
                         db.Column('movie_id', db.Integer, db.ForeignKey(
                             'movies.id'), primary_key=True),
                         db.Column('actor_id', db.Integer, db.ForeignKey(
                             'actors.id'), primary_key=True))


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)

    actors = db.relationship('Actor', secondary=movies_actors,
                             backref=db.backref('movies', lazy=True))

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }
