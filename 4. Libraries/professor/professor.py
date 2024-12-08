import random


def main():
    level = get_level()

    i = 0
    score = 0
    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        n = 0
        while n < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    n += 1
            except:
                print("EEE")
                n += 1
        if n == 3:
            print(f"{x} + {y} = {x + y}")
            pass
        i += 1
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        ran_num = random.randint(0, 9)
    if level == 2:
        ran_num = random.randint(10, 99)
    if level == 3:
        ran_num = random.randint(100, 999)
    return ran_num


if __name__ == "__main__":
    main()
