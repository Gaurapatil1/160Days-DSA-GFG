# Day 3 - Reverse an Array

*Problem Statement*  
You are given an array of integers arr[].  
Your task is to reverse the given array *in place*.

---

*Examples*

Input: [1, 4, 3, 2, 6, 5]  
Output: [5, 6, 2, 3, 4, 1]

Input: [4, 5, 2]  
Output: [2, 5, 4]

Input: [1]  
Output: [1]

---

*Constraints*  
- 1 ≤ arr.size() ≤ 10⁵  
- 0 ≤ arr[i] ≤ 10⁵

---

*Approach*  
- Use two pointers: start at the beginning and end at the end of the array.  
- Swap elements at start and end until the two pointers meet or cross.

Time Complexity: O(n)  
Space Complexity: O(1)