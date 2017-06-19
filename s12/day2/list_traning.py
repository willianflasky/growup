#!/usr/bin/env python3



all_list=[55,56,56,66,68,69,70]
dic={}
for i in all_list:
        if i > 66:
            if 'k1' in dic.keys():
                dic['k1'].append(i)
            else:
                dic['k1']=[i,]
        else:
            if 'k2' in dic.keys():
                dic['k2'].append(i)
            else:
                dic['k2']=[i,]

print(dic)


