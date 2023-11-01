import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(db_URI="", test_config=None):
    # create and configure the app
    app = Flask(__name__)
    if db_URI:
        setup_db(app, db_URI)
    else:
        setup_db(app)
    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS"
        )
        return response
    
    # test connection and local setup
    @app.route("/hello")
    def hello():
        return "Hello Mercy"

    """
    @TODO: == DONE
    Create an endpoint to handle GET requests
    for all available categories.

    Personal Notes
    - view is FormView.js, class is FormView(), componentDidMount()
    - curl test: curl http://127.0.0.1:5000/categories -X GET -H "Content-Type: application/json"
    """
    @app.route("/categories")
    def retrieve_categories():
        try:
            selection = Category.query.order_by(Category.id).all()
            categories = {}

            for one_category in selection:
                categories[one_category.id] = one_category.type

            return jsonify(
                {
                    "success": True,
                    "categories": categories,
                    "total_categories": len(selection)
                }
            )
        except:
            abort(404)

    """
    @TODO: == DONE
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.

    Personal Notes
    - view is QuestionView.js, method getQuestions()
    - curl test: curl http://127.0.0.1:5000/questions -X GET -H "Content-Type: application/json"
    - same output since pagination is implemented: http://127.0.0.1:5000/questions?page=1
    """

    @app.route("/questions")
    def retrieve_questions(category = "all"):
        try:
            selection_questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection_questions)

            if len(current_questions) == 0:
                abort(404)

            return jsonify(
                {
                    "questions": current_questions,
                    "total_questions": len(Question.query.all()),
                    "categories": retrieve_categories().json["categories"],
                    "current_category": category
                }
            )
        except:
            abort(404)


    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(
            {
                "success": False,
                "error": 404,
                "message": "resource not found"
            }
        )

    return app

