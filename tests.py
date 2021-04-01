from graphene.test import Client
import unittest

from app.schema import schema

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()

    def setUp(self):
        with self.app.app_context():
            self.client =  app.test_client()
            db.create_all()
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    def test_user(self):
        client = Client(schema=schema)
        queryAllUsers = '''query{
  allUsers{
    username
    email
  }
}'''

        executed = client.execute(queryAllUsers)
