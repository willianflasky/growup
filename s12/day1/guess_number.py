#!/usr/bin/env python3
luckNum=19
inputNum=0
while luckNum != inputNum :
    inputNum=int(input("input the guess num:"))
    # inputNum==luckNum:
        #break
    if inputNum > luckNum:
        print("the real number is smaller.")
    elif inputNum < luckNum:
        print("the real number is big.")

print("bingo")