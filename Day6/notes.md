 # Day 6 - Stock and Height Adjustment Problems

---

## 🔸 Problem 1: Stock Buy and Sell – Max One Transaction

### 🔹 Problem Statement
Find the maximum profit you can make with one buy and one sell operation. Buy must be before sell.

### ✅ Approach
- Track the *minimum price* so far while iterating.
- Calculate profit: current_price - min_price
- Keep updating max_profit

### 🧠 Code Logic
```python
buy_price = prices[0]
max_profit = 0
for price in prices[1:]:
    max_profit = max(max_profit, price - buy_price)
    buy_price = min(buy_price, price)
 ⏱️ Time Complexity

O(n)



---

🔸 Problem 2: Minimize the Heights II

🔹 Problem Statement

Modify each height by either adding or subtracting K exactly once. Find the minimum difference between the tallest and shortest tower after modification. No tower should be negative.

✅ Approach

Sort the array.

Try different splits: lower group (add K), upper group (subtract K).

Track max and min values for each possible split.

Ensure non-negative after decrease.


🧠 Code Logic

arr.sort()
ans = arr[-1] - arr[0]
for i in range(1, len(arr)):
    if arr[i] - k < 0:
        continue
    mn = min(arr[0] + k, arr[i] - k)
    mx = max(arr[i - 1] + k, arr[-1] - k)
    ans = min(ans, mx - mn)

⏱️ Time Complexity

O(n log n) due to sorting



---

🧪 Sample Test Cases

🧾 Stock Profit

Input: [7, 10, 1, 3, 6, 9, 2] → Output: 8

Input: [1, 3, 6, 9, 11] → Output: 10

Input: [7, 6, 4, 3, 1] → Output: 0


🏰 Tower Heights

Input: k = 2, arr = [1, 5, 8, 10] → Output: 5

Input: k = 3, arr = [3, 9, 12, 16, 20] → Output: 11