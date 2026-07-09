from datetime import datetime 
from pydantic import BaseModel, Field
class Movie(BaseModel):
    Movie_ID:int
    Title:str
    Genre:str
    Language:str
    Rating:float=Field(ge=0,le=10)
    Release_Year:int=Field(le=datetime.now().year)
    Duration:int=Field(gt=0)
class Movie_update(BaseModel):
    Title:str
    Genre:str
    Language:str
    Rating:float=Field(ge=0,le=10)
    Release_Year:int=Field(le=datetime.now().year)
    Duration:int=Field(gt=0)
class MessageResponse(BaseModel):
    message:str