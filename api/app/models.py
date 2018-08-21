# Model class for the question
class Questions:
    def __init__(self, question_id, question):
        self.question_id = question_id
        self.question = question

    # method to enable us acess class attributes as items 
    def __getitem__(self,item):
        return getattr(self, item) 
    
    # method to enable us display class objects as dictionaries 
    def __repr__(self):
        return repr(self.__dict__)
        

# Model class for the answer
class Answer:
    def __init__(self, ans_id, answer, question_id):
        self.question_id = question_id
        self.answer = answer
        self.question_id = question_id

    # method to enable us acess class attributes as items 
    def __getitem__(self,item):
        return getattr(self, item) 
    
    # method to enable us display class objects as dictionaries 
    def __repr__(self):
        return repr(self.__dict__)