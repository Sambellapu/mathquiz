import random
import time

score = 0


def question():
    global score
    num = random.randint(1, 500)
    num2 = random.randint(1, 500)
    operator = random.randint(1, 4)

    if operator == 1:
        check = num + num2
        print(num, "+", num2)
    elif operator == 2:
        check = num - num2
        print(num, "-", num2)
    elif operator == 3:
        check = num * num2
        print(num, "*", num2)
    else:
        check = num // num2
        print(num, "/", num2)

    while True:
        try:
            answer = int(input("Enter your answer :"))
            if check == answer:
                score += 1
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")


start = time.time()
for i in range(1, 11):
    print("Question", i, ":")
    question()

stop = time.time()
interval = round(stop - start)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Time taken :", interval // 60, "minutes and", interval % 60, "seconds")
print("Your Score is " + str(score) + " out of 10")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")