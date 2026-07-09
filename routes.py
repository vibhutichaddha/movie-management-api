from typing import Optional
from fastapi import APIRouter, HTTPException, Query 
from data import movies
from models import MessageResponse, Movie, Movie_update
router=APIRouter()
@router.post("/movies",response_model=Movie,status_code=201)
def add_movie(movie:Movie):
    if movie.Movie_ID<=0:
        raise HTTPException(
            status_code=400, 
            detail="Invalid Movie ID")
    for existing_movie in movies:
        if existing_movie.Movie_ID==movie.Movie_ID:
            raise HTTPException(
                status_code=409, 
                detail="Movie already exists")
    movies.append(movie)
    return movie
@router.get("/movies",response_model=list[Movie])
def get_all_movies():
    return movies
@router.get("/movies/search",response_model=list[Movie])
def search_movie(Genre:Optional[str]=Query(default=None),Language:Optional[str]=Query(default=None),Rating:Optional[float]=Query(default=None,ge=0,le=10),Release_Year:Optional[int]=Query(default=None)):
    result=movies
    if Genre is not None:
        result=[movie for movie in result if movie.Genre.lower()==Genre.lower()]
    if Language is not None:
        result=[movie for movie in result if movie.Language.lower()==Language.lower()]
    if Rating is not None:
        result=[movie for movie in result if movie.Rating==Rating]
    if Release_Year is not None:
        result=[movie for movie in result if movie.Release_Year==Release_Year]
    return result
@router.get("/movies/{Movie_ID}",response_model=Movie)
def get_movie_by_id(Movie_ID:int):
    if Movie_ID<=0:
        raise HTTPException(status_code=400,detail="Invalid Movie ID")
    for movie in movies:
        if movie.Movie_ID==Movie_ID:
            return movie
    raise HTTPException(status_code=404,detail="Movie not found")
@router.put("/movies/{Movie_ID}",response_model=Movie)
def update_movie(Movie_ID:int,updated_movie: Movie_update):
    if Movie_ID<=0:
        raise HTTPException(status_code=400,detail="Invalid Movie ID")
    for index,movie in enumerate(movies):
        if movie.Movie_ID==Movie_ID:
            movie_data=updated_movie.model_dump()
            movies[index]=Movie(
                Movie_ID=Movie_ID,
                **movie_data)
            return movies[index]
    raise HTTPException(status_code=404,detail="Movie not found")
@router.delete("/movies/{Movie_ID}",response_model=MessageResponse)
def delete_movie(Movie_ID:int):
    if Movie_ID<=0:
        raise HTTPException(status_code=400,detail="Invalid Movie ID")
    for movie in movies:
        if movie.Movie_ID==Movie_ID:
            movies.remove(movie)
            return{"message":"Movie deleted successfully"}
    raise HTTPException(status_code=404,detail="Movie not found")