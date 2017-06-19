#!/usr/bin/env python3
luckNum = 19
inputNum = 0
guessCount = 0
while guessCount < 3:
    inputNum = int(input("input the guess num:"))

    if inputNum > luckNum:
        print("the real number is smaller.")
    elif inputNum < luckNum:
        print("the real number is big.")
    else:
        print("Bingo!")
        break
    guessCount += 1
else:
    print("too many times")
