#!/usr/bin/env python3
#import sys,os,copy

dic={
    "cpu":[80,],
    "mem":[80,],
    "disk":[80,]
}
print("before:",dic)
new_dic=copy.deepcopy(dic)
new_dic['cpu'][0]=50
print(dic)
print(new_dic)
