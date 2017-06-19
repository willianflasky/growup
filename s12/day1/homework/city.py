#!/usr/bin/env python3
import sys
L1={
    1:{"北京":{1:{"朝阳区":{1:"望京",2:"管庄"}},
               2:{"昌平区":{1:"回龙观",2:"上地"}},
                3:{"海定区":{1:"中关村",2:"黄庄"}}
             }
       },

    2:{"安徽":{1:{"合肥":{1:"肥东",2:"肥西"}},
             2:{"毫州":{1:"东",2:"西"}},
             3:{"阜阳":{1: "临泉", 2: "界首"}}
            }
       }
}
#function area
def show():
    for k1,v1 in L1.items():
        for k2,v2 in v1.items():
            print(k1,k2)

def once():
    d1=L1.get(int(option1))
    for a1,b1 in d1.items():
        global range2
        range2=b1.keys()
        for a2,b2 in b1.items():
            for a3,b3 in b2.items():
                print(a2,a3)

def twice():
    d2=L1.get(int(option1))
    for x1,y1 in d2.items():
        d3=y1.get(int(option2))
        for y2 in d3.values():
            for x3,y3 in y2.items():
                print(x3,y3)

#exec
show()
range=L1.keys()

while True:
    option1=input(">")
    if option1 == 'q':
        sys.exit('bye!')
    elif not option1.isdigit():
        print("请输入数字！")
        continue
    elif int(option1) not in range:
        print("超出范围！")
    else:
        once()
        while True:
            option2=input(">>")
            if option2=="q":
                break
            elif not option2.isdigit():
                print("请输入数字！")
                continue
            elif int(option2) not in range2:
                print("超出范围！")
            else:
                twice()
                while True:
                    option3=input(">>>")
                    if option3=='q':
                        break