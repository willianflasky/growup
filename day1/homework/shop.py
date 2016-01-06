#!/usr/bin/env python3

memory=input("Input Your Momey:")

msg="""

    Welcome To 家乐福
"""

print(msg)

thing={
    'apple':5000,
    'coffee':30,
    'smoking':10
}
for i in thing.items():
    print(i[0], i[1])
basket=[]
while True:
    goods=input("\033[32;1mPlease buying:\033[0m")
    if goods =="":
        continue
    elif goods in thing.keys():
        memory = int(memory) - int(thing[goods])
        if memory < 0:
            print("您没有足够的钱购买商品。")

        else:
            print("您的余额：%s"%memory)
    else:
        print("没有此商量,不好意思!")

