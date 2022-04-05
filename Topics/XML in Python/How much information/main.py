from lxml import etree

xml_str = etree.fromstring(input())
print(len(xml_str), len(xml_str.keys()))
