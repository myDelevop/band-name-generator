from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data["results"]:
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    wrong_answers = question["incorrect_answers"]
    new_question = Question(question_text, correct_answer, wrong_answers)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz and your final score is {quiz.score}/{quiz.question_number}")
