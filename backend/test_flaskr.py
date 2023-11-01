import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_name = "trivia_test"
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        self.database_path = "postgresql://{}:{}@{}/{}".format("student", "student", "localhost:5432", self.database_name)
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




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()