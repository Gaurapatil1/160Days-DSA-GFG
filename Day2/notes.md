# Day 2 - Move All Zeroes to End

*Problem Statement*  
You are given an array arr[] of non-negative integers.  
Move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements.  
The operation must be performed *in-place* (no extra array).

---

*Examples*

Input: [1, 2, 0, 4, 3, 0, 5, 0]  
Output: [1, 2, 4, 3, 5, 0, 0, 0]

Input: [10, 20, 30]  
Output: [10, 20, 30]

Input: [0, 0]  
Output: [0, 0]

---

*Constraints*  
- 1 ≤ arr.size() ≤ 10⁵  
- 0 ≤ arr[i] ≤ 10⁵

---

*Approach*  
- Use a pointer count to track the position of the next non-zero element.  
- Traverse the array, and if the current element is not zero, swap it with arr[count] and increment count.

Time Complexity: O(n)  
Space Complexity: O(1)