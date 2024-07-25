import random
print("welcome to guess the number")

def guessTheNo():
    ran = random.randrange(101)

    attempt = 0
    user_input = input("select a level 'easy' or 'hard'")
    if user_input == 'easy':
        attempt = 10
        print(f'you have {attempt} trials')
    elif user_input == 'hard':
        attempt = 5  
        print(f'you have {attempt} trials')  
    print("hello im the computer and im thinking a number from 1-100")
    while attempt != 0:
        guess = int(input("guess the number"))

        if guess == ran:
            attempt = 0
            print(f"{guess} is right")
        elif guess > ran :
            attempt -= 1
            print(f"Guess is too high. you have {attempt} trials left")
        elif guess < ran:
            attempt -= 1
            print(f"Guess is too low. you have {attempt} trials left")

        if attempt == 0:
            print("game over")
guessTheNo()