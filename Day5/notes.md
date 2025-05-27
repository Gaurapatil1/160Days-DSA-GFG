# Day 5 - Majority Element II (Boyer-Moore Voting Algorithm Extension)

## Problem Statement
Given an array of integers, return the elements that appear more than ⌊ n/3 ⌋ times.

---

## Step-by-step Explanation

### Step 1: Understanding the Problem
- At most, **two elements** can appear more than n/3 times.
- So we use two counters and two potential candidates.

---

### Step 2: Initialize Variables
```python
num1, num2 = 0, 0     # Potential candidates
c1, c2 = 0, 0         # Their respective counts

Step 3: First Pass - Candidate Selection

Loop through array and apply these rules:

If current element equals candidate 1, increment c1.

Else if equals candidate 2, increment c2.

Else if c1 is 0, assign current to num1 and c1 to 1.

Else if c2 is 0, assign current to num2 and c2 to 1.

Else decrement both c1 and c2.



---

Step 4: Second Pass - Count Candidates

Loop again to count actual occurrences of num1 and num2.


---

Step 5: Add to Result if Occurs > n//3

Append to result only if count is greater than n/3.


---

Step 6: Return Sorted Result

Return the list in sorted order.


---

Time and Space Complexity

Time Complexity: O(n)

Space Complexity: O(1)



---

Sample Input/Output

Input: [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]

Input: [1, 2, 3, 4, 5]
Output: []
