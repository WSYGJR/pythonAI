import random

random_number = random.randint(1,100)
while True:
    num = int(input("请猜数字"))
    if num == random_number:
        print("恭喜你猜对了，数字为",random_number)
        break
    elif num > random_number:
        print("猜大了")
    elif num < random_number:
        print("猜小了")
