#!/usr/bin/env python
# coding:utf8
__author__ = "willian"

goods = [
          {"name": "电脑", "price": 1999},
          {"name": "鼠标", "price": 10},
          {"name": "游艇", "price": 20},
          {"name": "美女", "price": 998},
        ]

while True:
    salary = input("请输入你的收入:").strip()
    if len(salary) == 0:
        continue
    if salary.isdigit():
        break
    else:
        print("请输入数字.")
        continue
salary = int(salary)
car = []
total = 0

# print list
for n, v in enumerate(goods, 1):
    print(n, v['name'], v['price'])

while True:
    choice = input("你想买点什么?").strip()
    if len(choice) == 0:
        continue

    if choice.isalpha():
        if choice == 'exit' or 'quit':
            for good in car:
                print("你购买了:\033[32;1m{0},{1}\033[0m".format(good['name'], good['price']))
                total += good['price']
            print("total:\033[31;1m{0}\033[0m".format(total))
            exit()
        else:
            continue

    elif choice.isdigit:
        if int(choice) < len(goods):
            good = goods[int(choice)-1]
            if salary > good['price']:
                salary = salary - good['price']
                print("您消费了:\033[31;1m{0}\033[0m".format(good['price']))
                car.append(good)
            else:
                print("你的钱不够,还差\033[31;0m{0}\033[0m".format(good['price'] - salary))

        else:
            print("\033[31;1m没有些商品.\033[0m")
            continue







