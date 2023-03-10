import os
import random
import time

highscore = 0

def number_game():
    if os.path.isfile("highscore"):
        f = open("highscore", "r")
        highscore = int(f.read())
        f.close()

    print("select game")
    game = input()
    game = game.lower()
    if game == ("number"):
        print("select gamemode Hardore = H | infinite = I | normal = N")
        gamemode = input()
        gamemode = gamemode.upper()
        if not (gamemode == "H" or gamemode == "I" or gamemode == "N"):
            print("invalid gamemode using default")
        print("select operator subtraction = S | addition = A | multiplication = M")
        operator = input()
        operator = operator.upper()
        if not (operator == "S" or operator == "A" or operator == "M"):
            print("invalid operator using default")

        start_time = 0
        end_time = 0
        counter = 0

        numberquestion = 5

        score = 0
        number1 = 0
        number2 = 0
        print("select difficulty 1, 2, 3, 4")

        difficult = int(input())
        if difficult > 4:
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

        if difficult == 4:
            number1 = -9999999
            number2 = 9999999

        start_time = time.time()
        if gamemode == ("I"):
            numberquestion = 9223372036854775807
        for X in range(numberquestion):
            random_number = random.randint(number1, number2)
            random_number1 = random.randint(number1, number2)
            if operator == ("S"):
                print("what is " + str(random_number1) + "-" + str(random_number))
            elif operator == ("A"):
                print("what is " + str(random_number1) + "+" + str(random_number))
            elif operator == ("M"):
                print("what is " + str(random_number1) + "x" + str(random_number))
            answer = input()
            answer = answer.upper()
            if answer == "X" or answer == "exit":
                print("exited")
                break
            if operator == ("S"):
                if int(answer) == (random_number1 - random_number):
                    score += 1
                else:
                    print("wrong answer")
                    if gamemode == "H" or gamemode == "I":
                        print("game ended")
                        break
            elif operator == ("A"):
                if int(answer) == (random_number1 + random_number):
                    score += 1
                else:
                    print("wrong answer")
                    if gamemode == "H" or gamemode == "I":
                        print("game ended")
                        break
            elif operator == ("M"):
                if int(answer) == (random_number1 * random_number):
                    score += 1
                else:
                    print("wrong answer")
                    if gamemode == "H" or gamemode == "I":
                        print("game ended")
                        break
        end_time = time.time() - start_time
        end_time = int(end_time)
        print("your score is " + str(score) + " you did it!" + " your time was " + str(end_time) + " seconds")
        if highscore < score:
            f = open("highscore", "w")
            f.write(str(score))
            f.close()
            print("new high score")
