from question_model import Question
from data import question_data

question_bank = []

question = Question(question_data[1]["text"], question_data[1]["answer"])

print(question.text)
print(question.answer)


for data in question_data:
  # Create a question
  new_question = Question(data["text"], data["answer"])
  question_bank.append(new_question)

print(question_bank)
