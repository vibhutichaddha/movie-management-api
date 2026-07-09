# Movie Management API

## Overview

The Movie Management API is a RESTful API developed using FastAPI for managing movie records. It allows users to add, view, update, delete, and search movies using HTTP requests.

The project demonstrates REST API development, request validation, response models, exception handling, and structured project organization using Python and FastAPI.

## Objective

The objective of this project is to develop a structured REST API for managing movie information while following REST principles and proper API development practices.

## Movie Information

Each movie record contains the following details:

* Movie ID
* Title
* Genre
* Language
* Rating
* Release Year
* Duration in minutes

## Features

### Add Movie

Allows a new movie record to be added to the system.

**Endpoint:** `POST /movies`

The Movie ID must be unique and the movie information must satisfy all validation rules.

### Get All Movies

Returns all movie records available in the system.

**Endpoint:** `GET /movies`

### Get Movie by ID

Returns the details of a specific movie using its Movie ID.

**Endpoint:** `GET /movies/{movie_id}`

If the requested movie does not exist, the API returns a `404 Not Found` response.

### Update Movie

Updates the information of an existing movie.

**Endpoint:** `PUT /movies/{movie_id}`

The API validates the updated movie information before modifying the record.

### Delete Movie

Deletes a movie record using its Movie ID.

**Endpoint:** `DELETE /movies/{movie_id}`

If the movie is not found, an appropriate error response is returned.

### Search Movies

Movies can be searched using different attributes such as:

* Genre
* Language
* Rating
* Release Year

**Endpoint:** `GET /movies/search`

Search parameters are passed using query parameters.

Example:

`GET /movies/search?genre=Action`

## Validation Rules

The API performs validation on movie data before storing or updating records.

* Movie ID must be unique.
* Rating must be between 0 and 10.
* Release Year cannot be greater than the current year.
* Invalid Movie IDs are handled appropriately.
* Required movie information must be provided.

## Exception Handling

The API handles common errors and returns appropriate HTTP responses.

Handled exceptions include:

* Invalid Movie ID
* Duplicate Movie ID
* Invalid Rating
* Movie Not Found
* Invalid movie data

Proper HTTP status codes and error messages are returned to clearly indicate the cause of an error.

## Response Models

Pydantic response models are used for API responses.

Response models help maintain a consistent response structure and ensure that the returned data follows the expected format.

## API Documentation and Testing

FastAPI automatically provides interactive API documentation.

### Swagger UI

`/docs`

Swagger UI can be used to test API endpoints directly from the browser.

### ReDoc

`/redoc`

ReDoc provides structured and readable API documentation.

## Project Structure

```
movie_management_api/
│
├── main.py
├── models.py
├── routes.py
├── data.py
├── exceptions.py
├── requirements.txt
├── README.md
└── .gitignore
```

### main.py

Initializes the FastAPI application and connects the application routes.

### models.py

Contains Pydantic models used for movie data validation and response structures.

### routes.py

Contains API routes and implements CRUD and search operations.

### data.py

Stores and manages movie records used by the API.

### exceptions.py

Contains custom exceptions and error handling logic.

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* REST API

# Author
Vibhuti Chaddha
