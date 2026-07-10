from typing import Optional
from fastapi import APIRouter, HTTPException, Query, status
from data import movies
from models import MessageResponse, Movie, MovieUpdate
router=APIRouter()
@router.post("/movies",response_model=Movie,status_code=status.HTTP_201_CREATED)
def add_movie(movie:Movie):
    """
    Add a new movie to the movie collection.

    Parameters:
        movie: Movie information provided in the request body.

    Returns:
        The newly added movie.
    """
    if movie.movie_id<=0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid Movie ID")
    for existing_movie in movies:
        if existing_movie.movie_id==movie.movie_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, 
                detail="Movie already exists")
    movies.append(movie)
    return movie 
@router.get("/movies",response_model=list[Movie],status_code=status.HTTP_200_OK)
def get_all_movies():
     """
    Retrieve all available movies.

    Returns:
        A list containing all movie records.
    """
     return movies
@router.get("/movies/search",response_model=list[Movie],status_code=status.HTTP_200_OK)
def search_movie(genre:Optional[str]=Query(default=None),language:Optional[str]=Query(default=None),rating:Optional[float]=Query(default=None,ge=0,le=10),release_year:Optional[int]=Query(default=None)):
     """
    Search movies using genre, language, rating, or release year.

    Parameters:
        genre: Genre of the movie.
        language: Language of the movie.
        rating: Rating of the movie.
        release_year: Release year of the movie.

    Returns:
        A list of matching movies or a message when no movies are found.
    """
     result=movies
     if genre is not None:
        result=[movie for movie in result if movie.genre.lower()==genre.lower()]
     if language is not None:
        result=[movie for movie in result if movie.language.lower()==language.lower()]
     if rating is not None:
        result=[movie for movie in result if movie.rating==rating]
     if release_year is not None:
        result=[movie for movie in result if movie.release_year==release_year]
     return result
@router.get("/movies/{movie_id}",response_model=Movie,status_code=status.HTTP_200_OK)
def get_movie_by_id(movie_id:int):
    """
    Retrieve a movie using its unique Movie ID.

    Parameters:
        movie_id: Unique ID of the movie.

    Returns:
        Movie details for the provided ID.
    """
    if movie_id<=0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Movie ID")
    for movie in movies:
        if movie.movie_id==movie_id:
            return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Movie not found")
@router.put("/movies/{movie_id}",response_model=Movie,status_code=status.HTTP_200_OK)
def update_movie(movie_id:int,updated_movie: MovieUpdate):
    """
    Update the details of an existing movie.

    Parameters:
        movie_id: Unique ID of the movie.
        updated_movie: Updated movie information.

    Returns:
        The updated movie record.
    """
    if movie_id<=0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Movie ID")
    for index,movie in enumerate(movies):
        if movie.movie_id==movie_id:
            movie_data=updated_movie.model_dump()
            movies[index]=Movie(
                movie_id=movie_id,
                **movie_data)
            return movies[index]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Movie not found")
@router.delete("/movies/{movie_id}",response_model=MessageResponse,status_code=status.HTTP_200_OK)
def delete_movie(movie_id:int):
    """
    Delete a movie using its unique Movie ID.

    Parameters:
        movie_id: Unique ID of the movie.

    Returns:
        A confirmation message after successful deletion.
    """
    if movie_id<=0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid Movie ID")
    for movie in movies:
        if movie.movie_id==movie_id:
            movies.remove(movie)
            return{"message":"Movie deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Movie not found")