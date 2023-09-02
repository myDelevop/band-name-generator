class Question:
    def __init__(self, question: str, ok_answer: str, ko_answers):
        self.question = question
        self.correct_answer = ok_answer
        self.wrong_answers = ko_answers


# new_q = Question("2+5=7", "True")
# print(new_q.question + " " + str(new_q.answer))
