from datetime import datetime 
from pydantic import BaseModel, Field
class Movie(BaseModel):
    movie_id:int
    title:str
    genre:str
    language:str
    rating:float=Field(ge=0,le=10)
    release_year:int=Field(le=datetime.now().year)
    duration:int=Field(gt=0)
class MovieUpdate(BaseModel):
    title:str
    genre:str
    language:str
    rating:float=Field(ge=0,le=10)
    release_year:int=Field(le=datetime.now().year)
    duration:int=Field(gt=0)
class MessageResponse(BaseModel):
    message:str