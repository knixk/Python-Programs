class QuizBrain:
    def __init__(self, q_list = []):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        """Returns the next question"""
        ques = self.question_list[self.question_number]
        print(ques['text'])
        ans = input('Enter your ans..')
        self.question_number += 1
        