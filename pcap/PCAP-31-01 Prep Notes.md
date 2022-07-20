# Module 1: Modules

**Decomposition**: the division of program code into modules.

**Module**: a modular unit of functionality. In Python specifically, a module is a source file containing python definitions and statements which can be imported and used by other modules.

If you use a module, you're a **user**. If you create a module, you're a **supplier**.

Modules are identified by **name**.

**Namespace**: a space in which names exist and do not conflict with each other. All names within a given namespace must be unique.

## `random`

`seed()` sets `random`'s' seed to the current UNIX timestamp. This happens once automatically when the module is first imported.
`seed(x: int)` sets `random`'s seed to a given integer value.

`randint(a, b)` is the same as `randrange(a, b+1)`

`choice(seq: list) -> int`
`sample(seq: list, n: int) -> list`
- `n >= len(seq)`

## `platform`

`platform(aliased: bool, terse: bool) -> str`

`machine()` gives just the processor family.

`processor()` gives the actual processor name, if available; defaults to `machine()`.

`system()` the OS name.

`version()` the OS version.

`python_implementation()`, `python_version_tuple()` info on the current python interpreter.

## Packages

`__pycache__/*.pyc` python bytecode.

Package imports require the root directory to be in `sys.path`.

Zip files can be added to `sys.path` as packages.

**PyPI**: Python Package Index.

## Module Quiz

Result: 100%

## Module Test

Result: 94%

The test itself contains an error that makes a score of 100% impossible:
> Question: What is true about the `pip search` command? (Select **three** answers)
> 
> Options:
> a. All its searches are limited to locally installed packages.
> b. It searches through all PyPI packages.
> c. It needs working Internet connection to work.
> d. It searches through package names only.
> 
> The test-taker is prompted to choose three options. However, only B and C are correct. A is wrong because the command searches PyPI, an online package index. D is wrong because, according to `pip help search`, the command searches for "packages whose name **or summary** contains" the given query.

# Module 2: Strings, Sequence Methods, & Exceptions

**I18N**: I{nternationalizatio}N

**Code point**: the numeric key of a character.

ASCII uses 8 bits, giving a 256 possible code points. However, only 128 of them are used natively. The remaining code points are set using a given **code page**.

**Unicode**: a long-term solution to the problem of non-universal code pages. Assigns over a million code points of unique characters. First 128 code points are ASCII. The next 128 are the ISO/IEC 8859-1 code page.

**UCS-4**: Universal Character Set. An encoding standard of Unicode that uses 4 bytes (32 bits) to represent a unicode code point. UCS-4 File starts with a **Byte Order Mark (BOM)** to announce the nature of the file's contents.

**UTF-8**: Unicode Transformation Format. An encoding standard of Unicode that uses the minimum number of bits to represent each code point. 
- Latin characters are 8 bits.
- Non-Latin characters are 16 bits.
- CJK (China-Japan-Korea) ideographs are 24 bits.

## Strings

Strings are immutable.

**Overloading**: the ability to use the same operator with different kinds of data.

`ord(char: str) -> int`
- a built-in function that returns the code point of a given character.
- `len(char) == 1`
- the inverse of `chr`. `x == ord(chr(x))`.

`chr(code_point: int) -> str`
- a built-in function that returns the character that maps to a given code point.
- `code_point in range(0x110000)`
- the inverse of `ord`. `x == chr(ord(x))`.

`str in str` can search for substrings too.

`min('aAbByYzZ') == sorted('aAbByYzZ', key=ord)[0]`

`'abc'.find('c') == 2`
`'abc'.find('z') == -1`
`str.find(term: str, start: int, end: int) -> int`
- For single-character searches, `str.find` is significantly slower than the `in` keyword.

String comparisons:
- upper-case < lower-case

## Module Quiz

Result: 90%

One of the questions is erroneous. It is a pick-two question; two options have a syntax error, but the other two are mutually exclusive and are stated ambiguously. I submitted a bug report for this question.

## Module Test

Result: 100%

# Module 3: Object-Oriented Programming

**Procedural Programming**: data and the functions that operate on it are entirely separate. 

**Object-Oriented Programming**: data and the functions that operate on it are grouped into units called classes.

Python is good for both  OOP and ProP.

The ability to protect select values against access is called encapsulation.

Leading dunder class members are not accessible (by name) outside their parent class. Python will raise an `AttributeError` if you attempt to do so.

## Instance Variables

Shown in an instance's `__dict__`.

Instance variables can be added to an object instance at any moment by anything.

Leading dunder variables added outside a class method will NOT be mangled.

## Class Variables

Class variables are not shown in an object's `__dict__`.

`ClassName.__name__ == 'ClassName'` 

```python
from random import randrange
randrange.__module__ == 'random'
```

```python
class ClassA: pass
class ClassB: pass
class ClassC(ClassA, ClassB): pass

ClassC.__bases__ == (ClassA, ClassB)
```

Default base class is `object`.

## Reflection and Introspection

**Reflection**: the ability to manipulate object members at runtime.

**Introspection**: the ability to examine object type and members at runtime.

## Inheritance

```python
class ClassA: pass
class ClassB(ClassA): pass

issubclass(ClassA, ClassA)
issubclass(ClassB, ClassA)
issubclass(ClassB, ClassB)

isinstance(ClassA(), ClassA)
isinstance(ClassB(), ClassA)
isinstance(ClassB(), ClassB)
```

Python seeks attributes in this order:
1. inside the instance
2. inside the class
3. inside each superclass in ascending order
Failure to match an attribute name in the above search raises an `AttributeError`.

Multiple inheritance searches attributes from left to right.

**Composition**: the creation of an object whose behavior is defined by other objects.

**Method Resolution Order (MRO)**: the strategy Python uses to scan a class hierarchy for a given method.

## Exception Handling

`try-except` blocks can have an `else` branch. This branch executes if and only if no exception occured in the `try` branch. This is what distinguishes it from `finally`, which executes no matter what.

## Module Quiz

Result: 100%

## Module Test

Result: 94%

Takeaways:
- s l o w   d o w n
- d o   n o t   s p e e d r u n   t h e   t e s t

# Module 4: Miscellaneous

## File Processing

(r)ead, (w)rite, (a)ppend, e(x)istify
(+) update
(b)inary, (t)ext

`IOError`: the base class of all stream-related exceptions. Has an `exc` attribute: an integer that corresponds to an error code in the `errno` module.

`errno`: the module that enumerates all error codes and their numbers.

`bytearray`: a class that can store amorphous data as a series of bytes.
- `len(bytearray(x)) == x`
- integer values only
- represented as `bytearray(b'\x00\x00...\x00')`

```python
# Fill a bytearray with file content until full or end of file.
data = bytearray(10)
with open(file, 'rb') as filehandle:
	filehandle.readinto(data)
```

```python
# Get whole file as bytearray.
with open(file, 'rb') as filehandle:
	data = bytearray(filehandle.read())
```

```python
# Get first n bytes of file as bytearray.
n = 10
with open(file, 'rb') as filehandle:
	data = bytearray(filehandle.read(n))
```

## Operating System Interface

`os.uname()` (only available on some unix distros)
- `systemname`:
- `nodename`: machine name on the network
- `release`
- `version`
- `machine`

Not recursive:
- `os.mkdir(path: str)`
- `os.rmdir(path: str)`
Recursive:
- `os.makedirs(path: str)`
- `os.removedirs(path: str)`

`os.system(cmd: str) -> int`: send the command to a shell instance and return its exit status.

## Module Quiz

Result: 94%

Takeaways:
- `list(map(func, *iterables)) == [func(*iterable_items) for iterable_items in zip(*iterables)]`

## Module Test

Result: 75%

Takeaways:
- Pay attention operations that happen before the `yield` statement in a generator.
- Familiarize yourself with `bytearray` presentation.
	- `bytearray(3) -> bytearray(b'\x00\x00\x00')`
- Familiarize yourself with `os.listdir()` output.
	- `os.listdir()` does NOT include current and parent directory pointers (`. and ..`).
- Memorize `datetime.strftime()` format notation.
	- Big letters give the full name, little letters give the abbreviation.
	- `%B|%b` is the month name.
	- `%m` is the month number.
	- `%A|%a` is weekday name.
	- `%w` is weekday number.
	- `%H` is 24-hour.
	- `%I` is 12-hour.
	- `%p` is AM/PM.
	- `%f` is microseconds.
	- `%z` is UTC offset.
	- `%j` is day number of year.
	- `%d` is day number of month.
	- `%W` is week number of year (monday == 0).
	- `%U` is week number of year (sunday == 0).

Retake result: 100%

# End-of-Course Test

Result: 88%

Takeaways:
- `open(file, 'r')` IS ITERABLE. It yields `.readline()`
- `timedelta`'s print representation will drop the days part if `days == 0`.
- `pip` and `pip3` are synonymous. 
- `pip version` is not a command; the ONLY ways to get pip's version is with `pip -v` or `pip --version`
- Instances DO NOT have their class as an attribute (`hasattr(Foo(), 'Foo') == False`). You misremembered the result of a module test that asked the same question. 

# Sample Practice Test

Result: 93%

Takeaways:
- I don't know whether `AssertionError` is a subclass of `RuntimeError`.
	- It is not. You got that question wrong.
	- Review Python's exception hierarchy.
- The test will trip you up on the distinction between function and method. Read VERY carefully. Pay attention to leading dots.\
- Two-answer questions always need two answers. Read the prompt subtext carefully.
- A constructor will raise a `TypeError` if it returns anything other than `None`.

# Final Practice Test

Result: 95%

Takeaways:
- You put one answer on a two-answer question AGAIN. WATCH IT.
- On top of that, you gave the TRUE answers to a question asking for the FALSE answers. READ MF, READ.