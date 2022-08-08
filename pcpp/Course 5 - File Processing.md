# Module 1 - SQLite 3

`sqlite3.connect(':memory:')` connects to a transient DB in RAM.

`for row in cursor.execute(...)` fetches rows one at a time. `cursor.fetchall()` reads the entire result set into a tuple. Because `cursor.execute(...)` implements the iterator protocol, `tuple(cursor.execute(...))`

`cursor.execute('SELECT field FROM table').fetchall()` normally returns a `tuple[tuple[type(field)]]`. However, `cursor.row_factory = lambda curs, row: row[0]` will make the aforementioned return value a `tuple[type(field)]` (it flattens the fetched row data).


