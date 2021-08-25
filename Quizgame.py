def new_game():
    guess=[]
    correct_guess=0
    ques_nums=1
    for key in question:
        print("########################")
        print(key)
        for i in options[ques_nums-1]:
            print(i)
        gues=input("Enter A,B,C or D :")
        gues=gues.upper()
        guess.append(gues)
        correct_guess+=check(question.get(key),gues)
        ques_nums+=1
    display_score(correct_guess,guess)

def check(answer,gues):
    if answer==gues:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


 
def display_score(correct_guess,guess):
    print("-------------------------")
    print("Result")
    print("-------------------------")
    print("Answer: ")
    for i in question:
        print(question.get(i),end=" ")
    print()
    for i in guess:
        print(i,end=" ")
    score=int(correct_guess/(len(question)))*100
    print("Your score is ",score,"%")

def play_again():
    response=input("Do you want to try again ? Pls enter Yes or No :")
    response=response.lower()
    if response=="yes":
        return True
    if response=="no":
        return False


question = {
    "What is the velocity of sound":"B",
    "Is spiderman the most powerful Heroes ? ":"A",
    "What is the best language for the newbie ?":"D",
    "What is the most powerful Tool to solve a problem":"D",
}
options=[["A. 300km/h","B. 340m/s","C. 300km/s","D. 340km.h"],
         ["A. No, he is stupid","B. Yes","C. He has the same power as Iron man","D. In the future not now "],
         ["A. Java","B. C","C. Python","D. C++"],
         ["A. Inteligence","B. Hard work","C. Lucky","D. Both A, B and C"]]

new_game()

while play_again():
    new_game()

print("Byeeee")

