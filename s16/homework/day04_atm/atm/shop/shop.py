#!/usr/bin/env python
# coding:utf8
__author__ = "willian"

def run():
    # dictionary
    shop_list = [
        ['iphone', 6500],
        ['mac', 12000],
        ['office', 30],
    ]

    welcome_message = """\033[31;0m
        欢迎来购物,祝您购物愉快!
        \033[0m
    """

    print(welcome_message)
    # variables
    while True:
        salary = input("请输入你的收入:").strip()
        if len(salary) == 0:
            continue
        elif salary.isalpha():
            print("请输入数字.")
            continue
        elif salary.isdigit():
            break

    car = []
    total = 0

    # print list
    for k, v in enumerate(shop_list, 1):
        print(k, v[0], v[1])

    while True:
        choice = input("你想买点什么?")
        if choice.isalpha():
            if choice == 'exit' or 'quit':
                for i in car:
                    print("你购买了:\033[32;1m{0},{1}\033[0m".format(i[0], i[1]))
                    total += i[1]
                print("total:\033[31;1m{0}\033[0m".format(total))
                exit()
            else:
                continue

        elif choice.isdigit:
            if int(choice) < len(shop_list):
                ret = shop_list[int(choice)-1]
                if salary > ret[1]:
                    salary = salary - ret[1]
                    print("您消费了:\033[31;1m{0}\033[0m".format(ret[1]))
                    car.append(ret)
                else:
                    print("你的钱不够,还差\033[31;0m{0}\033[0m".format(ret[1] - salary))

            else:
                print("\033[31;1m没有些商品.\033[0m")
                continue


if __name__ == '__main__':
    run()





