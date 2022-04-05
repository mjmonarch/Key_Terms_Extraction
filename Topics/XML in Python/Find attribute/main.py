from lxml import etree

root = etree.fromstring(input())
attr_name = input()

print(root.get(attr_name))

