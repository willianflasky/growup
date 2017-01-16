#!/usr/bin/env python
# coding:utf8
# Author:willian

AGE = 56
count = 0
for i in range(10):
    if count == 3:
        user_confirm = input('do you want continue[y/n]?').strip()
        if user_confirm == "y" or 'Y':
            count = 0
        elif user_confirm == 'n' or 'N':
            exit()
        else:
            print("只允许[y/n]")
            break
    guess_num = input("your guess num:")
    try:
        guess_num = int(guess_num)
    except ValueError:
        print("请输入数字.")
        continue
    if guess_num == AGE:
        print("you got it!")
        break
    elif guess_num > AGE:
        print("try to smailler...")
    else:
        print("try to bigger...")
    count += 1
