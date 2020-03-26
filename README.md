# Casting Agency API

Just another portfolio Flask API.

## Getting Started

### About Casting Agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

#### Use Cases:

- Casting Assistant
    - Can view actors and movies
  
- Casting Director
    - All permissions a Casting Assistant has and...
    - Add or delete an actor from the database
    - Modify actors or movies
    - Can assign actors to movies
  
- Executive Producer
    - All permissions a Casting Director has and...
    - Add or delete a movie from the database

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

From within the project directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=api
export FLASK_ENV=development
export DATABASE_URL=DATABASE CONNECTION STRING
export SECRET_KEY=RANDOM STRING
export SQLALCHEMY_TRACK_MODIFICATIONS=False
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `api` directs flask to use the `api` directory and the `__init__.py` file to find the application.

Setting the `DATABASE_URL` to valid Postgres connection string allow the app to connect to the Database server.

## Database Setup

With Postgres running and the above vars configured, execute the following command in the app server:

```bash
python manage.py db upgrade
```

This will create the Database tables.

## Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "Bad request"
}
```

## Endpoints

- GET '/'
- GET '/movies'
- GET '/movies/movie_id'
- GET '/actors'
- GET '/actors/actor_id'
- POST '/movies'
- POST '/movies/movie_id'
- POST '/actors'
- PATCH '/movies/movie_id'
- PATCH '/actors/actor_id'
- DELETE '/movies/movie_id'
- DELETE '/actors/actor_id'

**GET /**

- General:
  - Publicly accessible health check
  - Request Arguments: None
  - Returns: API Version
- Sample: `curl http://localhost:5000/`

```
{
    "version": "1.0"
}
```

**GET /movies**

- General:
  - Fetches a list of movies
  - Request Arguments: None
  - Returns: Whether or not the request is successful, A list of movies, the movies count. 
- Sample: `curl http://localhost:5000/movies`

```
{
    "success": True,
    "movies": [
        {
            "id": 1,
            "title": "The Matrix",
            "release_date": "10/06/1999"
        },
        {
            "id": 2,
            "title": "Gladiator",
            "release_date": "05/05/2000"
        }
    ],
    "movies_count": 2
}
```

**GET /movies/movie_id**

- General:
  - Fetches a movie
  - Request Arguments: None
  - Returns: Whether or not the request is successful and the movie model. 
- Sample: `curl http://localhost:5000/movies/1`

```
{
    "success": True,
    "movie": {
        "id": 1,
        "title": "The Matrix",
        "release_date": "10/06/1999"
    }
}
```

**GET /actors**

- General:
  - Fetches a list of actors
  - Request Arguments: None
  - Returns: Whether or not the request is successful, A list of actors, the actors count. 
- Sample: `curl http://localhost:5000/movies`

```
{
    "success": True,
    "actors": [
        {
            "id": 1,
            "name": "Keanu Reeves",
            "age": 55,
            "gender": "M"
        },
        {
            "id": 2,
            "name": "Russell Crowe",
            "age": 60,
            "gender": "M"
        }
    ],
    "actors_count": 2
}
```

**GET /actors/actor_id**

- General:
  - Fetches an actor
  - Request Arguments: None
  - Returns: Whether or not the request is successful and the actor model. 
- Sample: `curl http://localhost:5000/movies/1`

```
{
    "success": True,
    "movie": {
        "id": 1,
        "title": "The Matrix",
        "release_date": "10/06/1999"
    }
}
```

**POST /movies**

- General:
  - Creates a new movie
  - Request Arguments: An JSON object containing the title and the release date.
  - Returns: Whether or not the request was completed and the movie model.
- Sample: `curl http://localhost:5000/movies -X POST -H "Content-Type: application/json" -d '{"title": "The Matrix Reloaded", "release_date": "16/05/2003" }'`

```
{
    "success": True,
    "movie": {
        "id": 3,
        "title": "The Matrix Reloaded",
        "release_date": "16/05/2003"
    }
}
```

**POST /actors**

- General:
  - Creates a new actor
  - Request Arguments: An JSON object containing the name, the age and the gender.
  - Returns: Whether or not the request was completed and the actor model.
- Sample: `curl http://localhost:5000/actors -X POST -H "Content-Type: application/json" -d '{"name": "Russell Crowe", "age": 60, "gender": "M" }'`

```
{
    "success": True,
    "movie": {
        "id": 3,
        "title": "The Matrix Reloaded",
        "release_date": "16/05/2003"
    }
}
```

**POST /movies/movie_id**

- General:
  - Assign an actor to a movie
  - Request Arguments: An JSON object containing the actor id.
  - Returns: Whether or not the request was completed.
- Sample: `curl http://localhost:5000/movies/1 -X POST -H "Content-Type: application/json" -d '{"actor_id": 3 }'`

```
{
    "success": True
}
```

**PATCH /movies/movie_id**

- General:
  - Update a movie attributes
  - Request Arguments: An JSON object containing the title and/or the release date.
  - Returns: Whether or not the request was completed and the movie model.
- Sample: `curl http://localhost:5000/movies/3 -X PATCH -H "Content-Type: application/json" -d '{ "release_date": "16/05/2020" }'`

```
{
    "success": True,
    "movie": {
        "id": 3,
        "title": "The Matrix Reloaded",
        "release_date": "16/05/2020"
    }
}
```

**PATCH /actors/actor_id**

- General:
  - Update an actor attributes
  - Request Arguments: An JSON object containing the name, the age and or the gender.
  - Returns: Whether or not the request was completed and the actor model.
- Sample: `curl http://localhost:5000/actors/3 -X PATCH -H "Content-Type: application/json" -d '{ "gender": "F" }'`

```
{
    "success": True,
    "movie": {
        "id": 3,
        "name": "Caitlyn Jenner",
        "age": 70,
        "gender": "F"
    }
}
```

**DELETE /movies/movie_id**

- General:
  - Delete a movie from the database.
  - Request Arguments: None.
  - Returns: Whether or not the movie was deleted.
- Sample: `curl http://localhost:5000/movies/1 -X DELETE`

```
{
    "success": True
}
```

**DELETE /actors/actor_id**

- General:
  - Delete an actor from the database.
  - Request Arguments: None.
  - Returns: Whether or not the actor was deleted.
- Sample: `curl http://localhost:5000/actors/1 -X DELETE`

```
{
    "success": True
}
```

## Testing

To run the tests, run
```bash
pytest test_api.py
```
