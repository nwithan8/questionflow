from questionflow import QuestionFlow, Question, Answer, MultipleChoiceQuestion, Choice, YesNoQuestion, YesNoAnswer, YesNo


question_list = [
    Question("What is your name?"),
    Question("What is your age?"),
    MultipleChoiceQuestion("What is your favorite color?", [Choice("Red"), Choice("Blue"), Choice("Green")]),
    YesNoQuestion("Do you like Python?"),
]

flow = QuestionFlow(question_list)

while flow.has_more_questions:
    prompt = flow.ask_next_question()
    answer = input(prompt)
    flow.answer(answer)
    confirm_prompt = flow.ask_confirmation()
    confirm_answer = input(confirm_prompt)
    flow.answer_confirmation(confirm_answer)

question2 = flow.get_question_and_answer(question_number=2)
print(question2.answer)
