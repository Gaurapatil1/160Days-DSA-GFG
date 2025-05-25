# 160 Days of DSA – GeeksforGeeks (Python Track)

Welcome to my *160 Days of DSA Challenge* using *Python, based on the curated roadmap from **GeeksforGeeks. This journey is focused on mastering **Data Structures & Algorithms* to prepare for top internship and job opportunities.

---

## 📅 Structure

Each day consists of:
- program.py → Code for GFG problems solved that day.
- notes.py → Concepts learned, explanations, tips, and links.

---

## ✅ Goals

- Build strong fundamentals in DSA (Arrays to Graphs).
- Practice pattern-based problem solving.
- Maintain daily consistency with GitHub commits.
- Prepare for coding interviews and paid internships.

---

## 📌 Daily Progress

| Day | Topic | Folder | Status |
|-----|-------|--------|--------|
| 01  | Arrays Basics | [Day01](./Day01) | ✅ |
| 02  | Arrays Practice | [Day02](./Day02) | ✅ |
| ... | ... | ... | ... |

---

## 🛠 Tools & Platforms

- Python 3
- VS Code
- Git + GitHub
- GeeksforGeeks
- Unstop (weekly contests)
- LeetCode (after Day 80)

---

## ✨ After Day 80 Plan

- Switch to *LeetCode Daily Questions*
- Continue *Unstop Weekly Coding Contests*
- Build resume-ready GitHub profile
- Apply to *paid internships* (off-campus)

---

## 🔗 Connect With Me

- GitHub: [GauravPatil](https://github.com/Gaurapatil1)
- LinkedIn: [Gaurav Patil](https://www.linkedin.com/in/gaurav-patil-18b4682b2)
# DSA Day 2 - Push Zeros to End

## Problem Statement
Given an array of integers, push all the zeros to the end of the array while maintaining the relative order of the non-zero elements.

## Example
**Input:**  
`arr = [0, 1, 0, 3, 12]`  

**Output:**  
`[1, 3, 12, 0, 0]`

## Approach
- Initialize a pointer `count = 0` to track the position for the next non-zero element.
- Traverse the array:
  - If the current element is non-zero:
    - Swap it with the element at index `count`.
    - Increment `count`.
- This ensures all non-zero elements are moved to the front while keeping their order, and all zeros are moved to the end.

## Time Complexity
- **O(n)**, where n is the length of the array

## Space Complexity
- **O(1)**, in-place modification

## Python Code
```python
# User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr):
        # Pointer to track the position for next non-zero element
        count = 0

        # Traverse the array
        for i in range(len(arr)):
            # If the current element is non-zero
            if arr[i] != 0:
                # Swap the current element with the element at 'count'
                arr[i], arr[count] = arr[count], arr[i]
                # Move 'count' pointer to the next position
                count += 1

# Example usage
if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    Solution().pushZerosToEnd(arr)
    print("Array after pushing zeros to end:", arr)

Day 3: Reverse an Array

✅ Concept:

Reversing an array means changing the order of elements such that the first becomes last, second becomes second last, and so on.

Example:
Input: [1, 2, 3, 4]
Output: [4, 3, 2, 1]


---

✅ Approach: Two-Pointer (In-Place Swap)

Steps:

1. Initialize two pointers: i = 0, j = n-1


2. Swap elements at i and j


3. Move i forward and j backward


4. Repeat until i < j



Time Complexity: O(n)
Space Complexity: O(1)
