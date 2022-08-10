import xml.etree.ElementTree as ETree

tree = ETree.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'

    child.remove(child.find('author'))
    child.remove(child.find('year'))

    child.set('rate', '5')

    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

tree.write('movies.xml', 'UTF-8', True)