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
    def update_movie(id: int, title: str = None,
                     release_date: str = None) -> Optional[Movie]:
        movie = Movie.query.get(id)

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
    def delete_movie(id: int) -> bool:
        movie = Movie.query.get(id)

        if not movie:
            return False

        try:
            db.session.delete(movie)
            db.session.commit()
        except SQLAlchemyError:
            # TODO: Log DB error into log file.
            return False

        return True
