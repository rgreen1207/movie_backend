# from ariadne import convert_kwargs_to_snake_case
# from api import db
# from api.models import Movie

# @convert_kwargs_to_snake_case
# def update_likes(obj, info, title, desc):
#     try:
#         movie = Movie.query.get(id)
#         if movie:
#             movie.title = title
#             movie.likes += 1
#         db.session.add(movie)
#         db.session.commit()
#         payload = {
#             "success": True,
#             "movie": movie.to_dict()
#         }
#     except Exception as error:
#         payload = {
#             "success": False,
#             "errors": [str(error)]
#         }
#     return payload