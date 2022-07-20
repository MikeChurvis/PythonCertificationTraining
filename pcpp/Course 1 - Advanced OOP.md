# Module 1: OOP Refresher

**Instance**: a single instantiation of a class that occupies memory and has data elements.

**Object**: everything in Python that you can operate on. All things in Python have an implicit base class of `object`.

**Attribute**: a piece of data within an object.

'Object' is more general than 'instance'. All instances are objects; not all objects are instances. However, in Python, the overwhelming majority of objects are instances. Thus, barring a few technical exceptions, the words 'object' and 'instance' are used interchangeably.

```python
class FooClass:
	def __init__(self):
		self.variable = 'a'
	
	def method(self):
		pass

foo_instance = FooClass()

FooClass.__class__
foo_instance.__class__
```

`Foo.__dict__` has class attributes only.
`Foo().__dict__` has instance attributes only.

## Class Attribute Shadowing

Modifying a class attribute from an instance will NOT alter the class attribute. It will instead **create an instance attribute that shadows the class attribute.**

```python
class Foo:  
    var = 0  
  
  
foo = Foo()  
print(f"{foo.var == Foo.var = }")  # True
  
Foo.var += 1  
print(f"{foo.var == Foo.var = }")  # True
  
foo.var += 1  
print(f"{foo.var == Foo.var = }")  # False
```

Thus, modification of a class attribute MUST be done via the class itself.

# Module 2: Python Core Syntax

## Why you shouldn't use multiple inheritence:

Ambiguous / Convoluted Method Resolution Order, illustrated here with the **Diamond Problem** (a.k.a.: "deadly diamond of death"):
```python
class A: pass

class B(A): pass
class C(A): pass

class D(B, C): pass  # This works, but B's attrs override C's.
class E(C, B): pass  # This works, but C's attrs override B's.

class F(A, C): pass  # This fails, as it creates an ambiguous MRO.
```

### Curiosities:

- [ ] Find out what `super()` does in the context of a multiply-inherited subclass.

## Inheritance and Polymorphism

**Duck Typing**: an object is as an object can do. The existence of certain attributes determines use, not type; type is little more than a contract for what attributes should exist on an object. However, given Python's boundless runtime mutability, not even type guarantees attribute existence. Thus, Python just looks for the attributes it needs on an object, and raises exceptions if it can't find them. Python does not care about type.

## Decorators

Functions have a `.__name__` attribute.

# Module 3: Advanced Exceptions

`UnicodeError` subclasses `ValueError`
- `.encoding`
- `.reason`
- `.object`
- `.start`
- `.end`

## Exception Chaining

`Exception().__context__`
- is a reference to another exception.
- exists when this exception occurs during the handling of another.
- this is **implicit chaining**.

`Exception().__cause__`
- is a reference to another exception.
- exists when this exception is raised using `raise ThisException from existing_exception`.
- this is **explicit chaining**.

`Exception().__traceback__`
- is a `traceback` object
- use the `traceback` module to interact with it
	- `traceback.format_tb(...) -> list[str]`
	- `traceback.print_tb(...) -> None`

# Module 4: Object Identity and Copy Operations

`id(x) -> int`
- Returns the identity of the object for which `x` is a label.
- Never checks object content, only reference identity.
- `a is b` if `id(a) == id(b)`

**Shallow copy**: create a new object with the same contents as an existing object, even if those contents are references to a shared object.

**Deep copy**: create a new object by recursively copying data from an existing object. If the object contains any references, the contents of each reference is recursively copied. The finished copy will never share references with the original article.
- Can copy arbitrary objects.
- Use `copy.deepcopy`

## Serialization and `pickle`

**Serialization**: the conversion of an object structure into a byte stream from which the original object may be reconstructed in full.

**Pickling**: a form of serialization specific to Python. Can serialize arbitrary data, including function names, but not their definitions. Use the `pickle` module.
- `pickle.load(stream) -> object`: deserialize a binary stream (such as a file opened with `mode='rb'`) into a Python object.
- `pickle.loads(bytes) -> object`: deserialize a pickled object's byte-string and return the resulting object.
- `pickle.dump(data, stream) -> None`: serialize an object and dump its bytes into a binary stream (such as a file opened with `mode='wb'`).
- `pickle.dumps(data) -> bytes`: serialize an object and return its byte-string.

`PicklingError` will be raised when pickling non-picklable objects or deserializing byte streams that do not represent pickled objects.

`RecursionError` is raised when a file has deeply nested references (default max depth = 499)

**Function and class definitions cannot be pickled**. Thus, the code that calls `pickle.load` or `pickle.loads` must know of the class/function definition. Otherwise, the deserialized function name will raise an `AttributeError` when invoked.

Pickling is specific to Python, other languages cannot consume pickled objects.

The `pickle` module is not secured against erroneous or maliciously constructed data. Never unpickle data received from an untrusted or unauthenticated source.

## `shelve`

The `shelve` module exposes a serialization dictionary where objects are pickled and associated with a string key (MUST be a string).

```python
import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
new_shelve.close()
```

| Flag | Meaning |
|:-:|-|
| r | Open shelve db in read-only mode |
| w | Open shelve db in read-write mode |
| c | Open or create a shelve db, then open it in read-write mode |
| n | Create a new, empty shelve db, then open it in read-write mode |

# Module 5: Metaprogramming

**Metaclass**: a class whose instance is a class.
- Whereas a class decorator is applied on top of class during instantiation, a metaclass alters the class's instantiation logic itself, as metaclasses are applied when a class *definition* is read.
- `type` is the default metaclass for creating classes.

Notable attributes:

| Attribute | On an instance | On a class |
| - | - | - |
| `__name__` | (doesn't exist) | Is the name of the class 
| `__class__` | Is a reference to the instantiating class | Is a reference to `type`
| `__bases__` | (doesn't exist) | Is a tuple containing the classes from which this class directly inherits
| `__dict__` | Is a dictionary of instance attributes | Is a dictionary of class attributes

## The `type` Function

One-arg invocation reads the class attribute:
`type(x) == x.__class__`

Three-arg invocation dynamically creates a new class:
`type(name: str, bases: tuple[type], dictionary: dict) -> type`
- `name` becomes `.__name__`
- `bases` becomes `.__bases__`
- `dictionary` becomes `.__dict__`

# Course Quiz

Result: 80%

Two answers labeled as correct on the quiz are demonstrably false. I have submitted bug reports.

Adjusted result: 90%

Takeaways:
- A decorator does not *have* to be a function that wraps another function. It can be a function that returns a function that can be called later. Watch out for hardline verbiage like "only" and "must", as they may invalidate an otherwise correct answer.
- `__dict()__`? Really? Read what you're doing, headass.
- `help(x)` lists x's methods and properties.