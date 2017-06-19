#!/usr/bin/env python
#coding:utf8

from xml.etree import ElementTree as ET
from xml.dom import minidom
def prettify(elem):
    """将节点转换成字符串，并添加缩进。
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


root=ET.Element('famliy')


son1=ET.Element('son',{'name':'er1'})
son2=ET.Element('son',{'name':'er2'})


grandson1=ET.Element('son',{'name':'er11'})
grandson2=ET.Element('son',{'name':'er12'})

son1.append(grandson1)
son1.append(grandson2)

root.append(son1)
root.append(son2)

"""
tree=ET.ElementTree(root)
tree.write('xo2.xml',xml_declaration=True,encoding='utf8')
"""
raw_str=prettify(root)
f=open('xo2.xml','w',encoding='utf8')
f.write(raw_str)
f.close()