#!/usr/bin/env python
# -*-coding:utf8-*-
__author__ = "willian"
import random

"""
快排算法
    1. 从左侧获取一个数存到tmp中
    2. 两个参数：
        left: 通常等于0
        right：通常数据的长度，len(data)-1
    3. 获取中间值mid
        a. 第一层循环
        b. 第二层循环，第一个
            从最右边取个值和tmp对比，如果比tmp大，则不变，指针向左移，如果小则移动到最左边的空位置。
        c. 第二层循环，第二个
            从最左边取个值和tmp对比，如果大tmp小，则不变，指针向右移，如果大则移动到最右边的空位置。
        d. 最后结束，把tmp放到中间
        e. return left或者right都可以，两个值相等了。
    4. 递归
"""


def partition(data, left, right):
    tmp = data[left]  # 拿到最左边的数值
    while left < right:  # 循环条件，只要左小于右
        while left < right and data[right] >= tmp:  # 从右边找， 和tmp比较如果右边大，就移动指针
            right -= 1  # 向左移动指针
        data[left] = data[right]  # 如果右边小，就移动左的空位置去

        while left < right and data[left] <= tmp:  # 右边找完了，该从左边找了，和tmp比较如果左边小，就移动指针
            left += 1  # 移动指针，什么也不做
        data[right] = data[left]  # 如果左边大，就把他移到右边空位置去
    data[left] = tmp  # 最后让tmp回到他应该呆的位置,即:mid
    return left  # 此时left or right是相等的即mid位置


def quick_sort_(data, left, right):
    if left < right:  # 递归定义:  1. 有结束条件  2. 自调
        mid = partition(data, left, right)  # 找到中间值
        quick_sort_(data, left, mid - 1)
        quick_sort_(data, mid + 1, right)


def quick_sort(data_list):  # 封闭下
    return quick_sort_(data, 0, len(data) - 1)


data = list(range(1000))
random.shuffle(data)

quick_sort(data)
print(data)
