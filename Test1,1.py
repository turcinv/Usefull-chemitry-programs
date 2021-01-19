print("Test")
marks = 0
questions = 0
question_1 = print("Question no.1: What particle is in the electron shell? \n A Electron  \n B Neutron \n C Pozitron \n D Proton\n")
answer_1 = input("Answer: ")
if answer_1 == (("A") or ("a")):
    print("Correct")
    marks = marks + 1
    questions = questions + 1

else:
    print("Bad")
    questions = questions + 1
    
question_2 = print("Question no.2: Which substance is polar? \n A Benzene \n B Pentane \n C Water \n D Ethylacetate \n")
answer_2 = input("Answer: ")
if answer_2 == (("C") or ("c")):
    print("Correct")
    marks = marks + 1
    questions = questions + 1

else:
    print("Bad")
    questions = questions + 1

result = marks / questions
print("Your result is:", result * 100, "%")
input("Press any keyboard to exit the program")