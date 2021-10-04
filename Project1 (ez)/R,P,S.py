import random
# r>s ,s>p , p>r

def play():
    user=input("'r' for rock , 's' for scissors ,'p' for paper : ")
    com=random.choice(['r','s','p'])
    if user==com:
        return "tie"
    
    if is_win(user,com):
        return 'you win'
    
    return 'you lose'

def is_win(user,com):
    if (user=='r' and com=='s') or (user=='s' and com=='p') or (user=='p' and com=='r'):
        return True

print(play())