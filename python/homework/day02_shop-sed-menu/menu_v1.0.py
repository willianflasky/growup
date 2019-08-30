#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

zone = {
    '北京': {"朝阳区": ['大山子', '康营', '崔各庄'],
           "海淀区": ['中关村', '上地', '知春路'],
           "顺义": ['飞机场', '李桥', '后沙浴']},
    "安徽": {"合肥": ['肥东', '肥西', '瑶海'],
           "阜阳": ['临泉', '颖上', '阜南'],
           "亳州": ['华佗', '城父', '大杨']},
    "河北": {"廊坊": ['固安县', '永清县', '文安县'],
           "石家庄": ['长安区', '桥东区', '桥西区'],
           "承德": ['滦平', '兴隆县', '平泉县']},
}


while True:
    provence = zone.keys()
    provence = list(provence)
    while True:
        for k, v in enumerate(provence, 1):
            print(k, v)

        choice = input('\033[32;1m>\033[0m请选择省份:(按q退出)').strip()
        if len(choice) == 0:
            continue

        elif choice.isdigit():
            choice = int(choice)
            if choice-1 >= len(zone):
                print("\033[31;0m输入超过范围!\033[0m")
                continue
            get_provence = provence[choice-1]

            city = zone.get(get_provence)  # dict level 2
            for index, key in enumerate(city, 1):
                print(index, key)

            while True:
                city_choice = input("\033[32;1m>>\033[0m请选择城市:(按q退出,按b返回上级)").strip()
                if len(city_choice) == 0:
                    continue

                get_city = city.keys()
                get_city = list(get_city)

                if city_choice.isdigit():
                    city_choice = int(city_choice)
                    if city_choice-1 >= len(zone):
                        print("\033[31;1m输入超过范围!\033[0m")
                        continue
                    town = get_city[city_choice-1]
                    for i in city[town]:
                        print(i)

                else:
                    if city_choice == 'q' or city_choice == 'Q':
                        exit()
                    elif city_choice == 'b':
                        break
                    else:
                        print("\033[31;1m不懂你的输入!\033[0m")
                        continue
        else:
            if choice == 'q':
                exit()
            elif choice == 'b':
                print("\033[31;1m已经顶层!\033[0m")
                continue
            else:
                print("\033[31;1m不懂你的输入!\033[0m")
                continue
