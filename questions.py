import random

# This function takes a random question from the questions list. Any unasked questions are pushed into a new key (unasked questions)
def get_random_question(question_keys, asked_questions_keys):
    try: 
        unasked_questions = []
        for question in question_keys:
            if question not in asked_questions_keys:
                unasked_questions.append(question)
        return random.choice(unasked_questions)
    except:
        return None


