import random
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {question.question}")
        options = question.wrong_answers
        options.append(question.correct_answer)
        random.shuffle(options)
        print("The option are: " + str(options))
        user_answer = input(f"What is your choice\n")
        self.check_answer(user_answer, question.correct_answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")
