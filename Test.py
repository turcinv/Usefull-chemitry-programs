print("Test")
marks = 0
questions = 0
question_1 = print("Question 1: \n A \n B \n C \n D \n")
answer_1 = input("Answer:")
if answer_1 == ("A") or ("a"):
    print("Correct")
    marks = marks + 1
    questions = questions + 1

else:
    print("Bad")
    questions = questions + 1

result = marks / questions
print("Your result is: ", result * 100, "%")
input()
