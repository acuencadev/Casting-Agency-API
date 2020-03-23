from typing import List, Optional

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
