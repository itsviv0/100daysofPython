from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a list of Question Objects
question_bank = []

# Add the questions and respective answers to the question_bank list from the data
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain object with the question_bank list of objects
quiz = QuizBrain(question_bank)

# Continue asking the all the questions to the user
while quiz.still_has_questions():
    quiz.next_question()

print(f"\nThanks for completing that!\nYour final score is: {quiz.score}/{quiz.question_number}")
