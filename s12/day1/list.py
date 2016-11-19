#!/usr/bin/env python3

nameList=['tom','apple','cat','tom']
dir(nameList)
nameList.append('tom')
nameList.index('tom')
nameList.count('tom')
nameList.remove('tom')
nameList.sort()
nameList.reverse()
nameList.pop()
nameList.insert(2,'tom')
#nameList.clear()
#namelist[:]
#nameList.extend(otherList)
#if 'tom' in nameList:
#   print('ok')

for i in range(nameList.count('tom')):
    nameList.remove('tom')
