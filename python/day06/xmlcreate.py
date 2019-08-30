#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import xml.etree.ElementTree as ET

# root
new_xml = ET.Element("namelist")


name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
sex.text = '33'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'

# 生成文档对象
et = ET.ElementTree(new_xml)
et.write("test.xml", encoding="utf-8", xml_declaration=True)
