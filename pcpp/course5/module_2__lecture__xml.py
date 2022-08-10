import xml.etree.ElementTree as et

tree = et.parse('books.xml')
root = tree.getroot()


def print_my_books():
    print("My books:")
    print()

    for book in root:
        print("Title: ", book.attrib['title'])
        print("Author:", book[0].text)
        print("Year:", book[1].text)
        print()


def print_authors():
    for author in root.iter('author'):
        print(author.text)


def print_title_of_first_book():
    print(root.find('book').get('title'))


if __name__ == '__main__':
    def main():
        # print_my_books()
        # print_authors()
        print_title_of_first_book()

    main()
