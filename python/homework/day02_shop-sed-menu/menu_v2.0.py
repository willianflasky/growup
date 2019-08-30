#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

menu = {
    '北京': {'海淀': {'五道口': {'soho': {},
                                '网易': {},
                                'google': {},
                                },
                    '中关村': {'爱奇艺': {},
                                '汽车之家': {},
                                'youku': {}, },
                    },

            '昌平': {'沙河':   {'老男孩': {},
                                '北航': {},
                                '包子': {}, },
                    '天通苑': {'1区': {},
                              "2区": {},
                              "3区": {}},
                   },
           },

    "上海": {'普陀': {"东区": {'vipabc': {},
                            '永久自行车': {},
                            '老上海': {}},
                     "西区": {"东方明珠": {},
                                '上海滩': {},
                                "陆家嘴": {}}
                            },
           "浦东": {"南城": {"浦发银行": {},
                            "桥水": {},
                            "招商银行": {},
                           },
                    "北城": {"虹桥机场": {},
                          "火车站": {},
                          "自贸区": {}
                           }
                 }
           },

    "天津": {'滨海区': {"东区": {'天津港口': {},
                            '天津自行车': {},
                            '老天津人': {}},
                     "西区": {"东方天津": {},
                                '天津滩': {},
                                "陆家天津": {}}
                            },
           "武清": {"南城": {"天津银行": {},
                            "桥水天津": {},
                            "天津很行": {},
                           },
                    "北城": {"天津机场": {},
                          "天津火车站": {},
                          "天津自贸区": {}
                           }
                 }
           },
        "南京": {'玄武': {"东区": {'大屠杀': {},
                            '28自行车': {},
                            '老人': {}},
                     "西区": {"老人与海": {},
                                '什么': {},
                                "苦口良": {}}
                            },
           "江宁": {"南城": {"东陈轼": {},
                            "无所谓": {},
                            "南京银行": {},
                           },
                    "北城": {"南京机场": {},
                          "南京火车站": {},
                          "南京自贸区": {}
                           }
                 }
           }
    }


def main():
    """**this is main line!**"""

    while True:
        L1 = []
        # 第一层的数据加入到L1列表. L1 = ['上海', '北京']
        for key in menu.keys():
            L1.append(key)
        # show L1数据
        for show_index, show_L1 in enumerate(L1, 1):
            print(show_index, show_L1)
        # 处理空值
        choice1 = input("\033[32;1m>\033[0m请选择城市[按'b'反回上一级,按'q'则退出]:").strip()
        if len(choice1) == 0:
            continue
        # 主线
        else:
            # 主线判断输入是数据
            if choice1.isdigit():
                # 转成INT
                choice1 = int(choice1)
                if choice1-1 < len(L1):
                    get_city = L1[choice1-1]
                    while True:
                        # 主线第二层
                        L2 = []
                        menu2 = menu[get_city]
                        for key in menu2.keys():
                            L2.append(key)
                        for show_index2, show_L2 in enumerate(L2, 1):
                            print(show_index2, show_L2)
                        choice2 = input("\033[32;1m>>\033[0m请告诉地区[按'b'反回上一级,按'q'则退出]:")
                        if len(choice2) == 0:
                            continue
                        else:
                            if choice2.isdigit():
                                # 转成INT
                                choice2 = int(choice2)
                                if choice2-1 < len(L2):
                                    get_area = L2[choice2-1]
                                    while True:
                                        # 主线第三层
                                        L3 = []
                                        menu3 = menu2[get_area]
                                        for key in menu3.keys():
                                            L3.append(key)
                                        for show_index3, show_L3 in enumerate(L3, 1):
                                            print(show_index3, show_L3)
                                        choice3 = input("\033[32;1m>>>\033[0m请告诉县城[按'b'反回上一级,按'q'则退出]:")
                                        if len(choice3) == 0:
                                            continue
                                        else:
                                            if choice3.isdigit():
                                                # 转换INT
                                                choice3 = int(choice3)
                                                if choice3-1 < len(L3):
                                                    get_place = L3[choice3-1]
                                                    while True:
                                                        # end
                                                        menu4 = menu3[get_place]
                                                        for i in menu4:
                                                            print("\033[33;1m{0}\033[0m".format(i))

                                                        end = input("[按'b'反回上一级,按'q'则退出]").strip()
                                                        if len(end) == 0:
                                                            continue
                                                        else:
                                                            if end == 'b':
                                                                break
                                                            elif end == 'q':
                                                                exit()
                                                            else:
                                                                print("\033[31;1m不懂你的输入[按'b'反回上一级,按'q'则退出]!\033[0m")
                                                                continue
                                                else:
                                                    print("\033[31;1m超出范围!\033[0m")
                                                    continue
                                            else:
                                                if choice3 == 'b':
                                                    break
                                                elif choice3 == 'q' or choice3 == 'Q':
                                                    exit()
                                                else:
                                                    print("\033[31;1m不懂你的输入[按'b'反回上一级,按'q'则退出]!\033[0m")
                                                    continue
                                else:
                                    print("\033[31;1m超出范围!\033[0m")
                                    continue
                            else:
                                if choice2 == 'b':
                                    break
                                elif choice2 == 'q' or choice2 == 'Q':
                                    exit()
                                else:
                                    print("\033[31;1m不懂你的输入[按'b'反回上一级,按'q'则退出]!\033[0m")
                                    continue
                else:
                    print("\033[31;1m超出范围[按'b'反回上一级,按'q'则退出]!\033[0m")
                    continue

            # 处理b,q和其它乱七八槽.
            else:
                if choice1 == 'b':
                    print("\033[31;1m不能再返回了,按q退出!\033[0m")
                    continue
                elif choice1 == 'q' or choice1 == 'Q':
                    exit()
                else:
                    print("\033[31;1m不懂你的输入[按'b'反回上一级,按'q'则退出]!\033[0m")
                    continue

if __name__ == '__main__':
    main()
