# Python Base Conversion — Quick Cheat Sheet

## 1. Complete algorithm

```
from itertools import zip_longest# Binary → decimaldef converter(binary):    result = 0    for bit in binary.strip():        result = (result << 1) | (bit == "1")    return result# Read, compare, and write incorrect line numberswith open("binary.txt") as b, open("decimal.txt") as d, \     open("result.txt", "w") as out:    for i, (binary, decimal) in enumerate(zip_longest(b, d), 1):        if binary is None or decimal is None or converter(binary) != int(decimal):            out.write(f"{i}\n")
```

## 2. Binary conversion essentials

BINARY → DECIMAL

\\[ 10110_2=16+4+2=\boxed{22\_{10}} \\]

```
result = result * 2 + int(bit)
```

Or, using bitwise operations:

```
result = (result << 1) | (bit == "1")
```

`<< 1` means multiply by 2.

DECIMAL → BINARY

```
def to_binary(n):    if n == 0:        return "0"    result = ""    while n > 0:        result = str(n % 2) + result        n //= 2    return result
```

`% 2` gets the remainder; `// 2` divides without decimals.

## 3. Python syntax to memorize

| Concept            | Syntax               | Purpose                    |
| ------------------ | -------------------- | -------------------------- |
| Variables          | `x = 0`              | Store values               |
| Integer conversion | `int("12")`          | String → integer           |
| String conversion  | `str(12)`            | Integer → string           |
| Loop               | `for x in items:`    | Iterate                    |
| While              | `while n > 0:`       | Repeat conditionally       |
| Condition          | `if a != b:`         | Compare                    |
| Strip              | `line.strip()`       | Remove whitespace/newlines |
| Lists              | `a.append(x)`        | Add item                   |
| Length             | `len(a)`             | Number of elements         |
| Enumerate          | `enumerate(a, 1)`    | Start counting at 1        |
| F-string           | `f"{i}\n"`           | Format number with newline |
| File read          | `open("a.txt", "r")` | Read                       |
| File write         | `open("a.txt", "w")` | Write/overwrite            |

## 4. Important file operations

```
# Read all lines into a listwith open("binary.txt") as f:    numbers = [line.strip() for line in f]# Write a linewith open("result.txt", "w") as f:    f.write("3\n")
```

`zip(a, b)` stops at the shorter file. `zip_longest(a, b)` includes unmatched lines, using `None` for missing values.

## 5. Common mistakes

- `=` assigns; `==` compares; `!=` means not equal.
- `//` is integer division; `%` is remainder.
- `range(n)` starts at 0, not 1.
- `write()` requires a string, so use `str(x)` or an f-string.
- `\n` creates a new line.
- `int(binary, 2)` and `bin(decimal)` are not allowed for this assessment.
- Remember to convert lines from `decimal.txt` to integers before comparison.

Most important to memorize: the binary conversion loop, `with open()`, `enumerate()`, and `f.write()`.
