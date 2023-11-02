import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Question, Category

# Connect to the database
# declaring environment variables to use on the db URI below
DB_USER = os.getenv('DB_USER', 'student')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'student')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_NAME = os.getenv('DB_NAME', 'trivia_test')
DATABASE_PATH = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        
        self.database_name = DB_NAME
        self.database_path = DATABASE_PATH
        self.app = create_app(self.database_path)
        self.client = self.app.test_client
        #setup_db(self.app, self.database_path)

        #setup a new question json object to use in the testcases
        self.new_question = {"question":"Which year did the USA get its first African American president?","answer":"2008","difficulty":1,"category":4}

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # testcase 1: test retrieve_questions() == success
    def test_get_paginated_questions(self):
        pass
    
    # testcase 2: test retrieve_questions() == failed
    def test_404_requesting_beyond_valid_page(self):
        pass

    # testcase 3: test retrieve_categories() == success
    def test_get_all_categories(self):
        response = self.client().get("/categories")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_categories"])
        self.assertTrue(len(data["categories"]))

    # testcase 4: test retrieve_categories() == failed
    def test_404_for_bad_url(self):
        response = self.client().get("/categories/100000")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    # testcase 5: test delete_question() == success NB: Delete a different question in each test attempt
    def test_delete_question_by_id(self):
        response = self.client().delete("/questions/22")
        data = json.loads(response.data)
        #question = Question.query.filter(Question.id == 12).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True), 
        self.assertEqual(data["deleted_question"], 22),
        self.assertTrue(len(data["current_questions"])),
        self.assertTrue(data["total_questions"])
        #self.assertEqual(question, None)

    #testcase 6: test delete_question() == failed
    def test_422_unprocessable_entity_when_deleting_question(self):
        response = self.client().delete("/questions/2000")
        data = json.loads(response.data)

        self.assertEqual(data["error"], 422)
        self.assertEqual(data["message"], "Unprocessable Entity")
        self.assertEqual(data["success"], False)
        self.assertEqual(response.status_code, 200)

    #testcase 7: test add_new_question() == success
    def test_add_new_question(self):
        response = self.client().post("/questions", json=self.new_question)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertTrue(data["created_question_id"])

    #testcase 8: test add_new_question() == failed
    def test_400_if_adding_new_question_fails(self):
        response = self.client().post("/questions/4000", json=self.new_question) #wrong URL
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200) #processed via expected method
        self.assertEqual(data["error"], 405)
        self.assertEqual(data["message"], "Method Not Allowed")
        self.assertEqual(data["success"], False)

    #testcase 9: test searching for a question based on a search term in the question == success
    def test_questions_search_with_results(self):
        response = self.client().post("/questions", json={"searchTerm": "title"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), 2)
        self.assertTrue(data["total_questions"])

    #testcase 10: test searching for a non-existent search term
    def test_questions_search_with_no_results(self):
        response = self.client().post("/questions", json={"searchTerm": "toot"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), 0)
        self.assertEqual(data["total_questions"], 0)

    #testcase 11: test questions_by_category() == success
    def test_get_questions_by_category(self):
        response = self.client().get("/categories/6/questions")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), 2)
        self.assertEqual(data["current_category"],6)
        self.assertTrue(data["total_questions"])

    #testcase 12: additional test for questions_by_category() using non-existent category
    def test_get_questions_by_category(self):
        response = self.client().get("/categories/100/questions")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), 0)
        self.assertEqual(data["current_category"],100)
        self.assertEqual(data["total_questions"], 0)

    #testcase 13: test questions_by_category() == failure
    def test_404_wrong_url_get_questions_by_category(self):
        response = self.client().get("/categories/6/qs")
        data = json.loads(response.data)

        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
        self.assertEqual(data["error"], 404)

    #testcase 14: test get_quiz_questions() == success
    def test_get_quiz_questions_by_category_id(self):
        response = self.client().post("/quizzes", json={"quiz_category":{"type":"Science", "id":1}, "previous_questions":[]})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["question"]))
        self.assertTrue(len(data["category"]))

    #testcase 15: test get_quiz_questions() == failure == none existent category type
    def test_400_quiz_without_category_id(self):
        response = self.client().post("/quizzes", json={"quiz_category":{"type":"Nothing", "id":10}, "previous_questions":[]})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")
        self.assertEqual(data["error"], 400)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()