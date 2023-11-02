# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

```
### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

#### Quick take:
If running this in the middle of your project, here are the combined instructions:
```bash
dropdb trivia
createdb trivia
psql trivia < trivia.psql
flask run --reload

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Endpoints Documentation

Below is a detailed documentation of the API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### GET /categories

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Curl example: `curl http://127.0.0.1:5000/categories -X GET -H "Content-Type: application/json"`
- Failed query will return a 404 error. See Errors section below for more details of the `key:value` pairs returned.
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

### GET /questions

- Fetches a dictionary of all the questions, in a paginated format (in groups of 10).
- Request Arguments: None
- Curl example: `curl http://127.0.0.1:5000/questions -X GET -H "Content-Type: application/json"`
- Curl example (using pagination): `curl http://127.0.0.1:5000/questions?page=1 -X GET -H "Content-Type: application/json"`
- Failed query will return a 404 error. See Errors section below for more details of the `key:value` pairs returned.
- Returns: An object with the keys, `categories`, `current_category`, `questions`, and `total_questions` in the format below.

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": "all",
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ],
  "total_questions": 25
}
```

### DELETE /questions/<int:question_id>

- Deletes a question using a question ID
- Request Arguments: `question_id`
- Curl example: `curl http://127.0.0.1:5000/questions/10 -X DELETE`
- Failed query will return a 402 error. See Errors section below for more details of the `key:value` pairs returned.
- Returns: An object with the keys: `success`, `deleted_question` which returns the ID of the deleted question, `current_questions` and  `total_questions` in the format below:

```json
{
  "current_questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    }
  ],
  "deleted_question": 10,
  "success": true,
  "total_questions": 24
}
```


### POST /questions -- to post a new question

- Posts a new question using the form provided in the `Add` section
- Request Arguments: None
- Curl example: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Is this a curl test?","answer":"yes it is","difficulty":3,"category":2}'`
- Failed query will return a 400 error. See Errors section below for more details of the `key:value` pairs returned.
- Returns: An object with the keys: `created_question_id`, `success`, and `total_questions` in the format below: 

```json
{
  "created_question_id": 33,
  "success": true,
  "total_questions": 25
}
```


### POST /questions -- to search for a question in the `Searchbox`

- Searches for a question using the search term provided on the `Searchbox` in the homepage. The searched term is case in-sensitive and can be part of a word or a sentence on the question.
- Request Arguments: None
- Curl example: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"title"}'`
- Returns: An object with the keys: `current_category`, `questions` which is a list of questions with the provided search term, `success`, and `total_questions` from the search results.
- Below is an example of the returned object when the word `title` is searched for:

```json
{
  "current_category": "all",
  "questions": [
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

### GET /categories/<int:category_id>/questions

- Fetches a list of questions based on a category
- Request Arguments: `category_id`
- Curl example: `curl http://127.0.0.1:5000/categories/6/questions -X GET -H "Content-Type:application/json"`
- Failed query will return a 404 error. See Errors section below for more details of the `key:value` pairs returned.
- Returns: An object with the keys: `current_category`, `success`, `questions`, and `total_questions` in the format below.
- Below is an example of the returned object when category `6` is searched for:

```json
{
  "current_category": 6,
  "questions": [
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

### POST /quizzes

- Fetches list of questions, based on the Category selected, to play the quiz.
- Request Arguments: None
- Curl example: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":{"type":"Science", "id":1}, "previous_questions":[]}'`
- Failed query will return a 404 error. See Errors section below for more details of the `key:value` pairs returned.
- Returns: An object with the keys: `question` for a random question to appear on the quiz, `success` value, and `category` which is a category object with key:value pairs for `id` and `type` of category.
- Below is an example of the objects returned when you play the quiz with `Science` as the category. (NB: the questions are randomized, so might appear in a different order).

_First round playing the quiz_
```json
{
  "category": {
    "id": 1,
    "type": "Science"
  },
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
```
_Second round playing the quiz_
```json
{
  "category": {
    "id": 1,
    "type": "Science"
  },
  "question": {
    "answer": "Alexander Fleming",
    "category": 1,
    "difficulty": 3,
    "id": 21,
    "question": "Who discovered penicillin?"
  },
  "success": true
}
```

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, start your virtual environment, change directory to backend, then run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
## Errors
- I have handled specific errors throughout the API creation, namely: `404`, `422`, `400`, and `405`.
- All the errors return an object with the keys: `error`, `message`, and `success`.
- Below is an example of an 404 error object returned:
```json
{
  "success": False,
  "error": 404,
  "message": "resource not found"
}
```
