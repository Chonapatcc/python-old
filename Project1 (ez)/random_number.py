import random
# user guess computer's number
def guess(x):
    random_number=random.randint(1,x)
    guess = 0
    while random_number!=guess:
        guess=int(input(f"Guess your number between 1 and {x}:"))
        if guess > random_number:
            print("oh , its too high!, guess again!")
        elif guess < random_number:
            print("oh ,Its too low,Guess again!")
    print("wow correct!!!")
# computer guess user' number
def computerguess(x):
    low=1
    high=x
    feedback=""
    while feedback!="c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high(H),or too low(L),or correct(C) : ".lower())
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
    print(f"Your number is {guess}")
computerguess(100)