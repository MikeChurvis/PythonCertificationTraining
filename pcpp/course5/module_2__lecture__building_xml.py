import xml.etree.ElementTree as ETree

root = ETree.Element('data')

movie_1 = ETree.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ETree.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})

ETree.dump(root)
