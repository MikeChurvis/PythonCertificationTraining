import xml.etree.ElementTree as ETree

shop = ETree.Element('shop')

category = ETree.SubElement(shop, 'category', {'name': 'Vegan Products'})

# name, product_type, producer, price, currency
products_list = [
    (
        "Good Morning Sunshine",
        "cereals",
        "OpenEDG Testing Service",
        "9.90",
        "USD"
    ),
    (
        "Spaghetti Veganietto",
        "pasta",
        "Programmers Eat Pasta",
        "15.49",
        "EUR"
    ),
    (
        "Fantastic Almond Milk",
        "beverages",
        "Drinks4Coders Inc.",
        "19.75",
        "USD"
    ),
]

for product_info in products_list:
    name, product_type, producer, price, currency = product_info

    product = ETree.SubElement(category, 'product', {'name': name})

    ETree.SubElement(product, 'type').text = product_type
    ETree.SubElement(product, 'producer').text = producer
    ETree.SubElement(product, 'price').text = price
    ETree.SubElement(product, 'currency').text = currency

ETree.ElementTree(shop).write('shop.xml', encoding='utf-8', xml_declaration=True)
