import random
num=random.randint(1,20)
guess=int(input("Can u guess the number less than 20):"))
print(__name__)
while  num!=guess:
    if guess>num:
        print("The number you guess is higher")
    else:
        print("The number you guess is lower")
    guess=int(input("Guess again"))
print("You won")
