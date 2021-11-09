class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_index = 0
        self.score = 0

    def has_next_question(self):
        return self.question_index < len(self.question_list)

    def next_question(self):
        user_answer = input(f"Q.{self.question_index + 1}: {self.question_list[self.question_index].text} True/False? ")
        self.check_answer(user_answer)
        self.question_index += 1

        if not self.has_next_question():
            print("Quiz Over!")
            print(f"Your final score is {self.score} out of {self.question_index}!")

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_index].answer
        if correct_answer.lower() == 'true':
            correct_answer = ['true', 't', 'yes', 'y']
        else:
            correct_answer = ['false', 'f', 'no', 'n']

        if user_answer.strip().lower() in correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"Score: {self.score}/{self.question_index+1}\n")