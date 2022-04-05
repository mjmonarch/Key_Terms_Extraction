from lxml import etree

root = etree.fromstring(input())

for element in root:
    print(element.text)
