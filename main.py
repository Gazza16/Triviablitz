from question_list import question_list
import questions




# Any questions that have been asked will be pushed into asked_questions_keys
asked_questions_keys = []
question_list_copy = question_list
random_question = questions.get_random_question(question_list_copy.keys(), asked_questions_keys)

QUESTION_COUNTER = 0
CORRECT_COUNTER = 0
INCORRECT_COUNTER = 0

while random_question:
    user_answer = " "
    asked_questions_keys.append(random_question)
    QUESTION_COUNTER += 1
    print(f"{random_question}")
    user_answer = input()
    if user_answer == question_list_copy[random_question]:
        print(f"{user_answer} is correct!")
        CORRECT_COUNTER += 1
    elif user_answer == "exit":
        print("Thank you for playing")
        print(f"""
        Total questions answered: {QUESTION_COUNTER}
        Correct answers: {CORRECT_COUNTER} 
        Incorrect answers: {INCORRECT_COUNTER}
        """)
        break

    elif user_answer == "status":
        print(f"""
        Total questions answered: {QUESTION_COUNTER}
        Correct answers: {CORRECT_COUNTER} 
        Incorrect answers: {INCORRECT_COUNTER}
        """)

    else:
        print(f"{user_answer} is incorrect, {question_list_copy[random_question]} is the correct answer.")
        INCORRECT_COUNTER += 1

  
    #This changes the questions IMPORTANT
    random_question = questions.get_random_question(question_list_copy.keys(), asked_questions_keys)

