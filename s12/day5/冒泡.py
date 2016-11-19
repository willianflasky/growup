#!/usr/bin/env python3
"""
data=[10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
counter=0
for j in range(1,len(data)):
    for i in range(len(data)-j):        #j,为优化程序,1.解决out of range,2.解决没有必要循环
        if data[i] > data[i+1]:
            data[i],data[i+1]=data[i+1],data[i]
        counter +=1
    counter +=1
    print(data)
print("Count:",counter)
"""


from optparse import OptionParser


parser = OptionParser()

parser.add_option('-f',"--file",dest="filename",
                  help="write report to FILE",metavar='FILE')


parser.add_option('-q','--quiet',dest='verbose',default=True,
                  help="don't print status message to stdout")

(option,args) = parser.parse_args()




