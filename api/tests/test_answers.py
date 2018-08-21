import os
import unittest
from app import questions
from app import create_app

class ApiTestCaseAnswers(unittest.TestCase):  
    """Define test variables and initialize app."""
    self.app = create_app(config_name="testing")
    self.client = self.app.test_client()
    self.question = {"title": "Question id",
                         "content": "question body"
                     }
                     self.answer = {"question_id": "1",
                     "answer_body":"ggggggg",
                     }
    def test_post_answer(self):
       "test an answer is posted "
        response = self.client.post("/api/v1/answer/1",
                                    data=json.dumps(self.answer),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Answer added successfully", response_msg["Message"])