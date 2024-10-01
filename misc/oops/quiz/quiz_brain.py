class QuizBrain:
    """Glue for the quiz"""
    def __init__(self, q_list = []):
        self.question_number = 0
        self.question_list = q_list

    def check_answer(self, user_ans, correct_ans):
        """Checks the answer"""
        return user_ans == correct_ans

    def next_question(self):
        """Displays the next question"""
        ques = self.question_list[self.question_number]
        
        self.question_number += 1

        ans = input(f"Q. {self.question_number}: {ques.text} (T/F)?")
        # correct_ans = ques

        print(ques)

        if (self.check_answer(ans)):
            print("correct ans!")
        else: 
            print("wrong ans bud")

        print(ans)
    

    def still_has_questions(self):
        """Returns boolean whether we have more questions in the list"""

        n = len(self.question_list)
        if (self.question_number >= n):
            return False

        return True

        
        