

## StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers
## Endpoints

| Endpoint       | Description          |   HTTP-verb  |
| ------------- |:-------------:| -----:| 
| /api/v1/logout | Logout the user from the system      | POST   |
| /api/v1/users | Get all users |  GET |
| /api/v1/question | Post a question | POST|
| /api/v1/question/id | Get question by id | GET |
| /api/v1/questions | Get all questions | GET |
| /api/v1/answer/questionId | Post an answer | POST|
| /api/v1//answers/questionId | Get all answers for a question | GET |


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
A few requirements to install, run and test this project.

cd path/to/directory-your-directory
- git clone 
 -Install virtual environment 
- cd to StackOverflow-lite and execute the following commands:
    
    - $ virtualenv venv --python=python3
    - $ source venv/scripts/activate
    - $ pip install -r requirements.txt
    - $ pip install pytest
    
- To run tests, do:

    - $ pytests

- Then run the app by executing:
    - $ python run.py
    
- Install and open postman to test the various endpoints





