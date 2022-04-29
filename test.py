from questionflow import QuestionFlow, Question, Answer, MultipleAnswerQuestion, MultipleChoiceQuestion, Choice, \
    YesNoQuestion, YesNoAnswer, YesNo

question_list = [
    Question("What is your name?"),
    Question("What is your age?"),
    MultipleChoiceQuestion("What is your favorite color?", [Choice("Red"), Choice("Blue"), Choice("Green")]),
    YesNoQuestion("Do you like Python?"),
    MultipleAnswerQuestion("What are your favorite foods?")
]

flow = QuestionFlow(question_list)

while flow.has_more_questions:
    prompt = flow.ask_next_question()
    answer = input(prompt)
    flow.answer(answer)
    confirm_prompt = flow.ask_confirmation()
    confirm_answer = input(confirm_prompt)
    flow.answer_confirmation(confirm_answer)

question5 = flow.get_question_and_answer(question_number=5)
print(question5.answer)
