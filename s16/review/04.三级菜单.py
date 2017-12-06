#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

exit_flag = False
current_layer = menu
layers = [menu]

# 此时:menu和current_layer相等，layers列表中有一个menu

while not exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        # current_layer = layers[-1]  # 如果回到上层，弹出
        # layers.pop()  # 弹出
        current_layer = layers.pop()
    elif choice not in current_layer:
        continue
    else:
        layers.append(current_layer)  # 此时：layers=[menu, current_layer], current_layer=menu
        current_layer = current_layer[choice]  # 重新赋值,此时：current_layer['北京']即北京下面的所有数据，
