from question_bank import QuestionBank


class QuizBrain:
    def __init__(self):
        self.question_number = 0
        bank = QuestionBank()
        bank.update_questions()
        self.question_list = bank.questions
        self.score = 0

    def still_has_questions(self):
        """ Check if we have more question at the question list."""
        return len(self.question_list) > self.question_number

    def make_question(self):
        """ Make the question for the user and go to check the answer."""
        corrent_question = self.question_list[self.question_number]
        correct_answer = corrent_question.answer
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {corrent_question.text} (True/False)? ').strip().title()
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        """ Check if the answer is correct or not and give the poit for the user."""
        if user_answer == correct_answer.strip().title():
            self.score += 1
            if self.score == 1 or self.score == 0:
                print(f'Yes, you are correct! You have got {self.score}/{self.question_number} point.')
            else:
                print(f'Yes, you are correct! You have got {self.score}/{self.question_number} points.')
        else:
            if self.score == 1 or self.score == 0:
                print(f'The answer is wrong. You keep {self.score}/{self.question_number} point.')
            else:
                print(f'The answer is wrong. You keep {self.score}/{self.question_number} points.')
        print('\n')

