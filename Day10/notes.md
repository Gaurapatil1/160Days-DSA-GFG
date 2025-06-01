# Day 10 – Implement Atoi Function in Python (Without Built-in Functions)

## ✅ Problem Statement
Implement the `atoi()` function which converts a string to an integer.

### Rules:
1. Ignore leading whitespaces.
2. Check for a sign (`+` or `-`), default to positive.
3. Read digits until a non-digit is found.
4. Ignore leading zeroes.
5. Clamp the result to 32-bit signed integer range:
   - If less than -2³¹, return -2³¹
   - If more than 2³¹ - 1, return 2³¹ - 1

---

## ✅ Edge Cases Handled
- Empty or whitespace-only string → returns `0`
- No digits after sign → returns `0`
- Very large or very small numbers → clamp to `[-2^31, 2^31 - 1]`
- Mixed characters after digits → stop reading at first non-digit

---

## 🧠 Logic Explanation:
1. Skip whitespace.
2. Read optional '+' or '-' sign.
3. Read each digit (convert using `ord(char) - ord('0')`).
4. While reading, check for overflow:
   - `res > (2^31 - 1) // 10` means next digit will overflow
   - If true, return max/min value
5. Return result × sign.

---

## 🔢 Examples:

| Input                   | Output         | Reason                                                   |
|------------------------|----------------|----------------------------------------------------------|
| `"-123"`               | `-123`         | Valid negative number                                    |
| `"  -"`                | `0`            | No digits                                                |
| `" 1231231231311133"`  | `2147483647`   | Overflow → Clamped                                       |
| `"-999999999999"`      | `-2147483648`  | Underflow → Clamped                                      |
| `"  -0012gfg4"`        | `-12`          | Stops at non-digit (`g`)                                 |

---

## 🏁 Output Range:
- Minimum: `-2147483648`
- Maximum: ` 2147483647`

---

## 🔗 Related Topics:
- String Parsing
- ASCII Conversion
- Integer Overflow