import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except:
        pass

random_num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_num:
                print("Too small!")
            if guess > random_num:
                print("Too large!")
            if guess == random_num:
                print("Just right!")
                break
    except:
        pass
