import random
while True:
    compp=['r','p','s']
    user=input("rock(r), paper(p), scissor(s)").lower()
    while user not in compp:
        print("invalid input")
        user=input("rock(r), paper(p), scissor(s)").lower()
    comp=random.choice(compp)
    print(user,'vs',comp)
    if user==comp:print("Draw")
    elif user=='p' and comp == 'r':print("You win")
    elif user=='r' and comp == 's':print("You win")
    elif user=='s' and comp == 'p':print("You win")
    else:print("You Lose")
