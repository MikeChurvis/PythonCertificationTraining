# Module 1 - SQLite 3

`sqlite3.connect(':memory:')` connects to a transient DB in RAM.

`for row in cursor.execute(...)` fetches rows one at a time. `cursor.fetchall()` reads the entire result set into a tuple. Because `cursor.execute(...)` implements the iterator protocol, `tuple(cursor.execute(...))`

`cursor.execute('SELECT field FROM table').fetchall()` normally returns a `tuple[tuple[type(field)]]`. However, `cursor.row_factory = lambda curs, row: row[0]` will make the aforementioned return value a `tuple[type(field)]` (it flattens the fetched row data).

# Module 2 - XML

`<?xml ... ?>` is the **prolog**, the optional first line of the document. 
- common attributes are `version` and `encoding`.

An XML document must have *exactly one* root element that contains all other elements.

## The `xml` Library

Noteworthy modules:
- `xml.etree.ElementTree`: Represents the XML tree as a structure of lists and dictionaries. Often considered the most "pythonic" implementation.
- `xml.dom.minidom`: Minimal implementation of the Document Object Model.
- `xml.sax`: Simple API for XML. Provides event-driven XML document analysis. More complex than the others; reserve its use for niche cases where it's needed.

This module uses the `xml.etree.ElementTree` module exclusively.

Add a prolog with `ElementTree(root).write(xml_declaration=True, ...)`

# Module 3 - CSV

You can use `DictReader` on .csv files without a header, but you must use `DictReader(file, fieldnames=[...])` to do so.
- Supplying more field names than there are columns in a row will fill the missing values of those columns with `None`.

`csv.writer(..., quotechar='"', quoting=csv.QUOTE_MINIMAL)`
- `csv.QUOTE_ALL` quotes all values.
- `csv.QUOTE_NONNUMERIC` quotes all non-number values.
- `csv.QUOTE_MINIMAL` only quotes values that contain special characters like delimiters.
- `csv.QUOTE_NONE` does not quote values. This will raise an error if the one of the values contains a special character.

# Module 4 - Logging

`logging.getLogger()` gets the root logger.
`logging.getLogger('hello')` creates a logger (child of root logger) named 'hello'.
`logging.getLogger('hello.world')` creates a logger (child of hello logger) named 'world'.
`logging.getLogger(__name__)` creates a logger idendified by the name of the current module. *This is the recommended practice.*

`logging.getLogger` is idempotent.

The default config (`logging.basicConfig()`) will not show `INFO` or `DEBUG` logs.