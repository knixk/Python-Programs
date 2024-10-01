class QuizBrain:
    """Glue for the quiz"""
    def __init__(self, q_list = []):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        """Displays the next question"""
        ques = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q. {self.question_number}: {ques.text} (T/F)?")
        
        