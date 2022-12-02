from .models import Movie
from ariadne import convert_kwargs_to_snake_case

def resolve_movies(obj, info):
    try:
        movies = [movie.to_dict() for movie in Movie.query.all()]
        
        payload = {
            "success": True,
            "movies": movies
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def resolve_movie(obj, info, movie_id):
    try:
        movie = Movie.query.get(movie_id)
        print(movie)
        payload = {
            "success": True,
            "movie": movie.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Movie item matching id {movie_id} not found"]
        }

    return payload