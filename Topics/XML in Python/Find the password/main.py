from lxml import etree


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    return check_element(root)


def check_element(element):
    if element.get('password'):
        return element.get('password')
    if len(element) > 0:
        for child_element in element:
            if check_element(child_element):
                return check_element(child_element)
    return None