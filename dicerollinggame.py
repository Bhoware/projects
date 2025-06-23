import random

while True:
    print("roll the dice (y/n)?")
    a = str(input())
    if a == 'y':
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(x, y)
    elif a == 'n':
        print("thanks for playing")
        break
    else:
        print("Invalid choice")
        break