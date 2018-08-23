import unittest import TestCase
import os
import json
from app.models import Questions
from app import app



class ApiTestCase(unittest.TestCase):  
       def setUp(self):
        """  Initialize app."""
        #self.app = create_app(config_name="test")
        self.client = self.app.test_client()
        self.question = {"title": "No module found error",
                         "content": "What is the correct way to fix this ImportError error?"
                     }


     #test for specific question                
        def test_specific_question():
            def setUp(self):

              response = self.client.get("/api/v1/question/1",
              data=json.dumps(dict(question_id=1)),
              content_type="application/json")
              self.assertEqual(response.status_code, 200)
              response_msg = json.loads(response.data.decode("UTF-8"))
              self.assertIn("Question found", response_msg["message"])

#test to add a question
        def test__post_question(self):
            def setUp(self):
       
             res = self.client.post("/api/v1/question",
            data=json.dumps(dict(title="challenge 2",
            content="Most challenging")),
            content_type="application/json")
            self.assertEqual(response.status_code, 201)
            response_msg = json.loads(response.data.decode("UTF-8"))
            self.assertEqual("A Question has been saved", response_msg["message"])


    
        




