# so guyz i am just a new python learner
# today i am trying to make a mcq interface using python fundamentals
# so lets begin with it horray!


#lets define a function
def quiz():
    score = 0  #starting score should be zero for addition purpose


    # first of all lets fill up the questions by defining a dictionary inside a list
    questions = [
        {
            "question": "what is capital of india?",
            "options":["A. New Delhi", "B. Mumbai", "C. Kolkata", "d. Chennai"],
            "answer": "A"
        },
        {
            "question": "what is capital of USA?",
            "options":["A. New York", "B. Washington DC", "C. Los Angeles", "D. Chicago"],
            "answer": "B"
        },
        {
            "question": "what is capital of UK?",
            "options":["A. Manchester", "B. Birmingham", "C. London", "D. Liverpool"],
            "answer": "C"
        },
        {
            "question": "what is capital of France?",
            "options":["A. Paris", "B. Lyon", "C. Marseille", "D. Nice"],
            "answer": "A"
        },
        {
            "question": "what is capital of Germany?",
            "options":["A. Berlin", "B. Munich", "C. Frankfurt", "D. Hamburg"],
            "answer": "A"
        }
    ]
    # so we are now done with data filling part for our quiz application for now we keep ir short
    # now we loop through question for displaying question and options simultaneously
    #fisrt intro to our quiz
    print("WELCOME TO THE MCQ QUIZ APPLICATION")
    print("-*100")
    for q in questions:
        print("\n"+ q["question"])
        for option in q["options"]:
            print(option)    #we loop through question options to print them one by one
        #now we take input from user for answer
        user_answer = input("enter your answer (A/B/C/D): ").upper()
        #now we check if user answer is correct or not by using conditions
        if user_answer == q["answer"]:
            print("Correct Answer!")
            score += 1
        else:
                print("wrong answer! The correct answer is", q["answer"])
print("\n your quiz is finished!")

print(f"your total score is : {score} out of {len(questions)}")  # len function gives total number of questions


run_quiz()