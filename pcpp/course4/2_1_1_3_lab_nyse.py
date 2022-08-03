import xml.etree.ElementTree

data = xml.etree.ElementTree.parse('nyse.xml').getroot().findall('quote')

if len(data) == 0:
    print("No data available.")
    exit(0)

example_node = data[0]

column_padding = 2

node_text_header = 'Company'
headers_and_column_widths = {
    label: len(label)
    for label in [node_text_header] + list(example_node.attrib.keys())
}

# Gather formatting info.
for node in data:
    headers_and_column_widths[node_text_header] = max(headers_and_column_widths[node_text_header], len(node.text))

    for attr in node.attrib:
        headers_and_column_widths[attr] = max(headers_and_column_widths[attr], len(str(node.attrib[attr])))

# Format and print the data.
header = ""
for column_header, column_width in headers_and_column_widths.items():
    column_header: str
    header += column_header.upper().ljust(column_width + column_padding)

header_content_separator = "-" * len(header)

content = []

for node in data:
    column_width = headers_and_column_widths[node_text_header] + column_padding
    formatted_node = node.text.ljust(column_width)

    for attr_label, attr_value in node.attrib.items():
        column_width = headers_and_column_widths[attr_label] + column_padding
        formatted_node += str(attr_value).ljust(column_width)

    content.append(formatted_node)

content.sort()

print(header)
print(header_content_separator)
print(*content, sep="\n")
