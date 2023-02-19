import random
import time
start_time = 0
end_time = 0
counter = 0

score = 0
number1 = 0
number2 = 0
print("select difficulty 1, 2, 3")

difficult =int(input())
if difficult > 3:
    print("invalid difficulty")
    exit()

if difficult == 1:
    number1 = 0
    number2 = 10

if difficult == 2:
    number1 = 0
    number2 = 50

if difficult == 3:
    number1 = 0
    number2 = 100

start_time = time.time()
for X in range(5):
    random_number = random.randint(number1, number2)
    random_number1 = random.randint(number1, number2)
    print("what is " + str(random_number1) + "+" + str(random_number))
    answer = input()
    answer = answer.upper()
    if answer == "X" or answer == "exit":
        print("exited")
        break
    if int(answer) == (random_number1 + random_number):
        score += 1
    else:
        print("you are an idiot")
end_time = time.time() - start_time
end_time = int(end_time)
print("your score is " + str(score) + " you did it!" + " your time was " + str(end_time) + " seconds")