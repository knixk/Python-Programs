from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

ques1 = Question("Biggest country?", "Russia")
print(ques1.text, ques1.ans)

question_bank = []

for item in question_data:
    ques = Question(item['text'], item['answer'])
    question_bank.append(ques)

# print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()
