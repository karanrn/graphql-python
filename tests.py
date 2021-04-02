from graphene.test import Client
import unittest
from flask import current_app as app

from app.app import create_app
from app.schema import schema
from app.database import db_session

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()

    def setUp(self):
        with self.app.app_context():
            self.client =  app.test_client()
    
    def tearDown(self):
        with self.app.app_context():
            db_session.remove()

    def test_query_user(self):
        with self.app.app_context():
            client = Client(schema=schema)
            queryAllUsers = '''query{
    allUsers{
        username
        email
    }
    }'''
            expectedResp = {'data': {'allUsers': [{'username': 'Tony Stark', 'email': 'tony@StarkIndustries.com'}]}}

            executed = client.execute(queryAllUsers)
            self.assertEqual(executed, expectedResp)

    def test_mutate_user(self):
        with self.app.app_context():
            client = Client(schema=schema)
            addUser = '''mutation{
                addUser(username:"Steve Rogers", email:"steve.rogers@avengers.com"){
                    user {
                        username
                        email
                    }
                }
            }'''
            expectedResp = {'data': {'addUser': {'user': {'username': 'Steve Rogers', 'email': 'steve.rogers@avengers.com'}}}}
            
            executed = client.execute(addUser)
            self.assertEqual(executed, expectedResp)

if __name__ == '__main__':
    unittest.main()
