# Module 1: Python Enhancement Proposals

Three different types of PEP:
- **Standards Track**: describes new features and implementations.
- **Informational**: describe design issues, guidelines, or other information.
- **Process**: describe procedures relating to Python, like change proposals.

Notable PEPs:
- PEP 0: an index of all PEPs
- PEP 1 - PEP Purpose and Guidelines
	- Defines the five-member Steering Council who accept or reject PEPs, the volunteer group of Core Developers, and the Benevolent Dictator For Life.
- PEP 8 - Style guide
- PEP 20 - The Zen of Python
	- 19 aphorisms which reflect the philosophy behind Python.
	- Tim Peters

# Module 2: The Zen of Python

Beautiful is better than ugly.
- Follow the PEP 8 style guide.

Explicit is better than implicit.
- If a positional argument's name could have meaning, name it.

Simple is better than complex.
- Use fewer lines of code when possible.
- Use builtins wherever possible.
- Divide big problems into small parts.

Complex is better than complicated.
- Complex = consisting of many elements.
- Complicated = difficult to understand.

Flat is better than nested.
- Rule of thumb: nest levels greater than 3 should probably assessed for a refactor.

Sparse is better than dense.
- Don't try to do too much in one line.

Readability counts.
- "Code is read more often than it is written" - Guido Van Rossum
- Give meaningful names to things.
- Add comments where necessary.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

# Module 3: PEP 8

Code style guide.

Checkers:
- `pycodestyle` (fka `pep8`)
- `autopep8`

Indentation:
- 4 spaces per level
- spaces, not tabs, if possible.
- mixing spaces and tabs will raise `TabError`

Continuation lines:
- Hanging indent on definitions should be two levels deep.

79 characters per line max.
72 characters per line on comments/docstrings.

Line break before binary operators.

Use UTF-8 encoding in Python 3, ASCII in Python 2.

Use english word identifiers whenever feasible.

Imports of different namespaces should be on separate lines.

Imports of different members of the same namespace may be on the same line.

Absolute imports are encouraged.

Wildcard imports are discouraged.

Triple-quote strings should use the double-quote character to maintain consistency with the docstring convention in PEP 257.

In kwarg assignment, don't surround the `=` with spaces.

# Module 4: Documentation

Public exported modules, functions, classes, and methods should have docstrings.

> [!INFO]
> This is not on the test, but good to know. Here's how you resolve circular imports with type annotations:
```python
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from othermodule import OutsideType

def do_something_outside(outside: OutsideType) -> OutsideType:
	...
```

A docstring should *prescribe* an entity ("Do this thing"), not *describe* it ("It does this thing").

**Linter**: analyzes programming errors and stylistic anomalies against a set of pre-defined rules.
- Flake8
- Pylint
- Mypy
- Pycodestyle

**Fixer**: formats code to comply with adoped standards.
- Black
- YAPF
- autopep8

Docstrings become the `.__doc__` attribute.

