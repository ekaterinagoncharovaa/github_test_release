# mathops

A small Python library of simple math operations, with every public method
covered by pytest tests.

## Project layout

```
mathops/
├── pyproject.toml          # build + pytest configuration
├── README.md
├── requirements.txt
├── src/
│   └── mathops/
│       ├── __init__.py     # public API
│       └── operations.py   # the operations
└── tests/
    └── test_operations.py  # one test class per method
```

## Public methods

| Function | Description |
|----------|-------------|
| `add(a, b)` | sum of two numbers |
| `subtract(a, b)` | `a - b` |
| `multiply(a, b)` | product of two numbers |
| `divide(a, b)` | `a / b` (raises `ZeroDivisionError` on `b == 0`) |
| `power(base, exponent)` | `base ** exponent` |
| `modulo(a, b)` | remainder (raises `ZeroDivisionError` on `b == 0`) |
| `floor_divide(a, b)` | `a // b` (raises `ZeroDivisionError` on `b == 0`) |
| `absolute(a)` | absolute value |
| `negate(a)` | flips the sign |
| `average(values)` | mean of a sequence (raises `ValueError` if empty) |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -e ".[test]"
```

## Usage

```python
from mathops import add, divide, average

add(2, 3)            # 5
divide(10, 4)        # 2.5
average([2, 4, 6])   # 4.0
```

## Running the tests

```bash
pytest
```

Or without installing the package:

```bash
pip install pytest
pytest          # pythonpath=src is set in pyproject.toml
```
