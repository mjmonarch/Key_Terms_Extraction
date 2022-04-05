from lxml import etree

file_path = "./data/dataset/input.txt"

tree = etree.parse(file_path)
root = tree.getroot()
members = [x.get('name') for x in root[0]]

# print(etree.dump(tree.getroot()))
print(*members)
