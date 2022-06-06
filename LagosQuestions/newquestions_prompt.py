from Questions_Lagos import Questions_Lagos

questions_prompt = [
    "Who is the current governor of Lagos state?\n (a) Babajide Sanwo-Olu\n (b) Fashola\n (c) Tinubu\n\n",
    "Was Lagos state the former capital of Nigeria?\n (a) Yes\n (b) No\n (c) Maybe\n\n",
    "Who is the current deputy governor of Lagos state?\n (a) Hamzat\n (b) Ambode\n (c) Adefulire\n\n",
    "Who is the first democratically elected governor of Lagos state?\n (a) Lateef Jakande\n (b) Bola Tinubu\n (c) Buba Marwa\n\n",
    "Which local government is the most populous in Lagos state?\n (a) Ikorodu\n (b) Surulere\n (c) Alimosho\n\n",
    "How many local governments/LCDAs are in Lagos state?\n (a) 20\n (b) 47\n (c) 77\n\n",
    "How many Federal Universities are in Lagos state?\n (a) 4\n (b) 2\n (c) 5\n\n",
    "The airport in Lagos state is located where?\n (a) Lekki\n (b) Oshodi\n (c) Ikeja\n\n",
    "When was Lagos state created?\n (a) 1990\n (b) 1969\n (c) 1967\n\n",
    "What is the full meaning of BRT?\n (a) Bus Rapid Transport\n (b) Babatunde Raji Transport\n (c) Bus Rapid Transit\n\n",

]

questions = [
    Questions_Lagos(questions_prompt[0],"a"),
    Questions_Lagos(questions_prompt[1], "a"),
    Questions_Lagos(questions_prompt[2], "a"),
    Questions_Lagos(questions_prompt[3], "a"),
    Questions_Lagos(questions_prompt[4], "c"),
    Questions_Lagos(questions_prompt[5], "c"),
    Questions_Lagos(questions_prompt[6], "a"),
    Questions_Lagos(questions_prompt[7], "c"),
    Questions_Lagos(questions_prompt[8], "c"),
    Questions_Lagos(questions_prompt[9], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions_prompt)) + " correct.")


run_test(questions)