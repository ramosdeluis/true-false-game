from quiz_brain import QuizBrain

new_quiz = QuizBrain()

while new_quiz.still_has_questions():
    new_quiz.make_question()

print(f'You have completed the quiz.')
print(f'Your final score was: {new_quiz.score}/{new_quiz.question_number}')