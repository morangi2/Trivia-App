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

    # testcase 4: test retrieve_categories() == failed ***check status code
    def test_404_for_bad_url(self):
        response = self.client().get("/categories/100000")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["error"], 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()