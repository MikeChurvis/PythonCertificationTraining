# Module 1

Instruction List (abbr. **IL**): a complete set of known commands

Machine languages are distinct from natural languages

All languages have these parts:
- Alphabet: symbols used to build words
- Lexis (a.k.a. dictionary): the set of words the language offers
- Syntax: the set of rules determining the validity of a string of words (i.e. "is this a legal arrangement of words")
- Semantics: the set of rules determining the soundness of a string of words (i.e. "does this string make sense")

The Instruction List is the alphabet of a machine language.

Source code: written by humans
Source file: file containing source code

Guido van Rossum (netherlands): creater of python

Python's direct competitor languages:
- Perl
- Ruby

## Python Variants

**Canonical Python** (the PSF versions) are implemented on top of C. These are called **CPython**.

**Cython** transpiles Python into C.

**Jython**: Python 2 written in Java.

**PyPy**: Python written in a restricted subset of python called **RPython**. PyPy is compiled into C. It's mainly a tool for people developing the Python language itself.

**IDLE** stands for Integrated Development and Learning Environment.

## Module 1 Quiz

Result: 100%

## Module 1 Test

Result: 90%

Takeaways:
- **Machine code** is a **low-level** language consisting of **binary** digits that the **computer reads** and understands

# Module 2

## Functions

Given `function_name(argument)`, python takes the following steps:
1. Checks the function name to see if it has been defined. If not, python aborts.
2. Checks the function signature for arguments. If the required argument count is not satisfied, python aborts.
3. Steps into the function and executes its contents.
4. Returns to the line of code following the function's invocation.

There cannot be more than one instruction (statement) in a line.
- (side note: this is technically incorrect for two reasons: 
	1. Semicolons are valid statement separators, but their use is strongly discouraged by the python community)
	2. Some statements are composed of multiple instructions, such as this: `a = 'foo' if CONDITION else 'bar'`. This is an assignment statement and a ternary conditional statement on the same line.

`print(*args, end="\n", sep=" ")`

## Literals

Integer literals may contain underscores, as of version 3.6

It is permissible, but redundant and unecessary, to put a leading plus sign on any number-type literal (e.g. `+12345`)

Floats can drop the trailing zero after the decimal. For instance, `a = 4.` is a valid statement.

`4e1` is also a float.

Integer division (`a // b`) is a.k.a. **floor division**.

Floor division does NOT truncate, it rounds down. 

## Operator Binding and Precedence

Exponentiation binds right. All others bind left.

Unary operators that follow exponentiation bind more strongly.

https://docs.python.org/3/reference/expressions.html#operator-precedence

## Variables

Variables names can include non-latin characters.

Variables names cannot 
- contain spaces or hyphens
- start with a number
- shadow a reserved keyword

PEP8 style guide:
- Variable and function names should be lowercase, with words separated by underscores.
- camelCase is legal, but should only be used to retain backwards compatibility with code authored prior to the PEP8 style guide publication.

Reserved kewords: `['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']`

## Input

`input(prompt: str|None) -> str`

## Module Quiz

Result: 100%

## Module Test

Result: 95%

Takeaways:
- Write down your scratch work or you'll mix up the order of things in your head.

# Module 3

In python, `2 == 2.0`

Syntactic sugar = syntactic candy = language features that are technically redundant but offer a simplified way of doing things.

## `while-else` and `for-else`

`while` and `for` can have an `else` clause. It is executed once, even on `return` or `raise`, but NOT on `break`.

## Logic Operators

`and` is a **conjunction**. 
`or` is a **disjunction**.
`not` is a **negation**.

`not` has the same priority as the other unary operators.

De Morgan's laws:
- The negation of a conjunction is the disjunction of the negations.
  `not (a and b) == (not a) or (not b)`
- The negation of a disjunction is the conjunction of the negations.
  `not (a or b) == (not a) and (not b)`

Evaluates the operands' truthiness.
Returns a boolean value.

## Bitwise Operators

`&` bitwise conjunction
`|` bitwise disjunction
`~` bitwise negation
`^` bitwise exclusive disjunction

The operator arguments must be integers.

Evaluates the operands' binary content.

Returns an integer.

## Lists

`list.insert(location: int, value: Any)`

## Module Quiz

Result: 100%

## Module Test

Result: 100%

Takeaways:
- Make sure you know the logical operator order of precedence.

# Module 4

**Shadowing** is when a variable takes the name of a variable that was defined outside of the current scope.

Reassigning a function argument raises a `TypeError`.

Positional args after keyword args raises a `SyntaxError`.

These three are equivalent:
```python
def func():
	print('ayy')

def func():
	print('ayy')
	return

def func():
	print('ayy')
	return None
```

## Functions and Scopes

```python
def func():
    print(var)
  
# func()  # NameError
var = 'foo'
func()  # foo
```

`global var`  declares that all uses of the name `var` within the current scope will affect the global scope.

## Dictionaries

Prior to Python 3.6, dictionary insertion order was not preserved; the order in which items appeared was meaningless. As of 3.6, dictionaries preserve their insertion order. HOWEVER, do not count on this remaining a feature; future python versions may remove this. **Program against dictionary keys as if they are unordered collections**.

## Module Quiz

Result: 92%

Takeaways:
- WATCH OUT FOR KEYWORDS WHERE THEY SHOULDN'T BE. That's twice they've thrown that curveball. You can bet they'll do it again.

## Module Test

Result: 91%

Takeaways:
- `global var` does not need `var` to be defined ahead of time.

# Summary Test

Result: 91%

Takeaways:
- `break` will raise a SyntaxError if used outside a loop.
- A bare `except` block MUST come last or it will raise a `SyntaxError`.
- `except` only catches RUNTIME errors.
- `SyntaxError` is NOT a runtime error. 
- `range(-1, -2)` is an EMPTY RESULT for the same reason `array[2:1]` is.