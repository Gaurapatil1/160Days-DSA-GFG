# Day 9 – DSA Practice

## ✅ Program 1: Smallest Positive Missing Number
- Difficulty: Medium
- Problem: Given an array, find the smallest positive integer (≥ 1) that is missing.
- Key Concepts:
  - Ignore negative and zero values.
  - Segregate positive values and use index marking to find the missing one.
- Time Complexity: O(n)
- Space Complexity: O(1)

### Example:
- Input: [2, -3, 4, 1, 1, 7]
- Output: 3

---

## ✅ Program 2: Maximum Circular Subarray Sum
- Difficulty: Hard
- Problem: Given a circular array, find the maximum sum of any subarray.
- Key Concepts:
  - Use Kadane’s algorithm for normal max subarray.
  - Also calculate total sum - min subarray (via negation).
  - Final Answer = max(normal_sum, circular_sum)
- Edge Case: All elements negative → return max element
- Time Complexity: O(n)
- Space Complexity: O(1)

### Example:
- Input: [10, -3, -4, 7, 6, 5, -4, -1]
- Output: 23

---