#!/usr/bin/env python3
import os,sys
goodlist={'mac-pro':9000,
          'air':7000,
          'iphone6s':5000,
          'iphone5s':2500,
          'ipad':3000
          }
shopList=[]
money=""
#result=0
def show():
    for k,v in goodlist.items():
        print(k,v)

def shoppingExists(i):
    if i in goodlist.keys():
        return 0
    else:
        return 1
def getMoney():
    while True:
        money=input('你的卡里有多少钱>').strip()
        if money.isdigit():
            break
        else:
            print("只允许输入数字")
            continue
    global money

def cart(shopping):
    shopList.append(shopping)
    for x in shopList:
        print(x)


def main():
    getMoney()
    show()
    while True:
        choiceShoping=input("添加商品到购物车>\n \033[32;1m1(去结算) 2(退出不结算)\033[0m")
        if choiceShoping =='' or choiceShoping=='0':
            continue
        elif choiceShoping=='1':
            break
        elif choiceShoping=='2':
            sys.exit()
        elif shoppingExists(choiceShoping) == 1:
            print('不存在你要买的商品\t\033[31;1m{0}\033[0m'.format(choiceShoping))
        else:
            cart(choiceShoping)


if __name__=="__main__":
    main()
    changeMoney=[]
    result=0
    for shop in shopList:
        changeMoney.append(goodlist.get(shop))
    #print(changeMoney)
    for i in changeMoney:
        result =result + i
    #print(result)

    print('进行结算中....')

    if int(money) < result:
        print('钱不够本次结算')
        buyOrNot=input("\033[32;1m1(冲值) 2(放弃本购买)\033[0m").strip()
        if buyOrNot=='1':
            addmoney=input('>')
            money = int(money) + int(addmoney)
            print('余额:'.format(money))
        else:
            sys.exit('bye')
    else:
        money = int(money) - result
        print("欢迎下次光临!")
        print("余额:{0}".format(money))
