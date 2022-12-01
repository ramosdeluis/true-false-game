from data import question_data
from question_model import Question


class QuestionBank:

    def __init__(self):
        self.questions = []

    def update_questions(self):
        for question in question_data:
            self.questions.append(Question(question['question'], question['correct_answer']))
