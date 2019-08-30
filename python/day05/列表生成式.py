#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

a = [1, 2, 3, 3, 4, 5, 6, 7, 8]

# for index, i in enumerate(a):
#     a[index] = i + 1
#
# print(a)

# 列表生成式
# a = [i+1 for i in a]
# a = [i*i if i > 5 else i for i in a]

# 生成器 generator
a = (i*i if i > 5 else i for i in a)
print(next(a))


# 角斗士
# 海上钢琴师
# 钢琴师
# 英国病人
# 放牛班的春天
# 西西里的美丽传说
# 中央车站
# 教父
# 西部世界
# 权力的游戏
# 上帝之城
"""
    焦土之城
    绝美之城
    战争之王
    华尔街之狼
    大空头
    霸王别姬
    盲井
    颐和园
"""