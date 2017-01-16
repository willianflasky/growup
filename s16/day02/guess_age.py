#!/usr/bin/env python
#coding:utf8
#Author: willianflasky



AGE = 56

guess_num = int(input("your guess num:"))


if guess_num == AGE:
    print("congratulation ,you got it.")

elif guess_num > AGE:
    print("try smaller!")

else:
    print("try bigger..")