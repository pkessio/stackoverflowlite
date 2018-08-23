import os
import unittest import TestCase
import json
from app.models import questions
from app import create_app

class ApiTestCaseAnswers(unittest.TestCase):  
     def test_user_post_answer(self):
     
        response = self.app.post('/api/v1/answers/1/', data=json.dumps(self.answer), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], 'answer posted successfully!')
       

        response = self.app.post('/api/v1/answers/1/', data=json.dumps(
        self.answer_no_body), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Body is required')

     def test_view_answers(self):
   
        response = self.app.get('/api/v1/answers/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], "all answers found successfully")

 




    