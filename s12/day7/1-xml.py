#!/usr/bin/env python
#coding:utf8

from xml.etree import ElementTree as ET
"""
tree=ET.parse('xo.xml')

root=tree.getroot()

print(root)
print(root.tag)
print(root.attrib)
print(root.text)

for child in root:
    print(child.tag,child.attrib)
    for gradechild in child:
        print(gradechild.tag,gradechild.text)
"""

str_xml=open('xo.xml','r').read()

root=ET.XML(str_xml)
"""
for node in root.iter('year'):
    new_year=int(node.text)+1
    node.text=str(new_year)

    node.set('name','tom')
    node.set('age','18')
    del node.attrib['age']

tree = ET.ElementTree(root)
tree.write('newxo.xml',encoding='utf8')
"""
for country in root.findall('country'):
    rank=int(country.find('rank').text)

    if rank > 50:
        root.remove(country)

tree = ET.ElementTree(root)
tree.write('newxo.xml',encoding='utf8')
