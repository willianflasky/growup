#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

current_layer = menu
P_layer = []

while True:
    for k in current_layer:
        print(k)
    choice = input('>:').strip()
    if len(choice) == 0:
        continue
    elif choice in current_layer:
        P_layer.append(current_layer)           # 将上一层都记录下来,加到列表中.
        current_layer = current_layer[choice]   # 进入下一层.
    else:
        if choice == 'b':
            if len(P_layer) > 0:
                current_layer = P_layer.pop()   # 返回上一层时,就将数据POP出,赋值给current_layer.
        elif choice == 'q':
            exit("Bye!")



