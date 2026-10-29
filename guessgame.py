import random
number= random.randint(1,50)
attempts=0
while attempts < 5:
    guess=int(input("Guess a number between 1,50:  "))
    attempts +=1
    if guess < number:
        print("number is too high")
    elif guess > number:
        print("number is too low")
    else:
        print("congratulations! you guessed the correct number in", attempts, "attempts")
        
else:
    print("sorry, you used all your attempts, the number was", number)