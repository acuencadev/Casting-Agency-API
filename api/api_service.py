from typing import List, Optional

from sqlalchemy.exc import SQLAlchemyError

from .extensions import db
from .models import Movie, Actor


class MoviesRepository:
    @staticmethod
    def get_all_movies() -> List[Movie]:
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]

        return formatted_movies

    @staticmethod
    def get_movie_by_id(movie_id: int) -> Optional[Movie]:
        movie = Movie.query.get(movie_id)

        if not movie:
            return None

        formatted_movie = movie.format()

        return formatted_movie

    @staticmethod
    def create_movie(title, release_date) -> Optional[Movie]:
        movie = Movie(title=title, release_date=release_date)

        try:
            db.session.add(movie)
            db.session.commit()
        except SQLAlchemyError as err:
            # TODO: Log DB error into log file.
            return None

        formatted_movie = movie.format()

        return formatted_movie

    @staticmethod
    def update_movie(movie_id: int, title: str = None,
                     release_date: str = None) -> Optional[Movie]:
        movie = Movie.query.get(movie_id)

        if not movie:
            return None

        if title:
            movie.title = title

        if release_date:
            movie.release_date = release_date

        db.session.commit()

        formatted_movie = movie.format()

        return formatted_movie

    @staticmethod
    def delete_movie(movie_id: int) -> bool:
        movie = Movie.query.get(movie_id)

        if not movie:
            return False

        try:
            db.session.delete(movie)
            db.session.commit()
        except SQLAlchemyError:
            # TODO: Log DB error into log file.
            return False

        return True

    @staticmethod
    def assign_actor(movie_id: int, actor_id: int) -> bool:
        movie = Movie.query.get(movie_id)
        actor = Actor.query.get(actor_id)

        if not actor or not movie:
            return False

        try:
            movie.actors.append(actor)

            db.session.commit()
        except SQLAlchemyError:
            return False

        return True


class ActorsRepository:

    @staticmethod
    def get_all_actors() -> List[Actor]:
        actors = Actor.query.all()
        formatted_actors = [actor.format() for actor in actors]

        return formatted_actors

    @staticmethod
    def get_actor_by_id(actor_id: int) -> Optional[Actor]:
        actor = Actor.query.get(actor_id)

        if not actor:
            return None

        formatted_actor = actor.format()

        return formatted_actor

    @staticmethod
    def create_actor(name: str, age: int, gender: str) -> Optional[Actor]:
        actor = Actor(name=name, age=age, gender=gender)

        try:
            db.session.add(actor)
            db.session.commit()
        except SQLAlchemyError as err:
            # TODO: Log DB error into log file.
            return None

        formatted_actor = actor.format()

        return formatted_actor

    @staticmethod
    def update_actor(actor_id: int, name: str = None, age: str = None,
                     gender: str = None) -> Optional[Actor]:
        actor = Actor.query.get(actor_id)

        if not actor:
            return None

        if name:
            actor.name = name

        if age:
            actor.age = age

        if gender:
            actor.gender = gender

        db.session.commit()

        formatted_actor = actor.format()

        return formatted_actor

    @staticmethod
    def delete_actor(actor_id: int) -> bool:
        actor = Actor.query.get(actor_id)

        if not actor:
            return False

        try:
            db.session.delete(actor)
            db.session.commit()
        except SQLAlchemyError:
            # TODO: Log DB error into log file.
            return False

        return True
