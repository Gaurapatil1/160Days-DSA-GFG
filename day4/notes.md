Day 4 – Array Problems (Intermediate)

1. Rotate Array (Left Rotation)

Problem

Given an array arr[], rotate it to the left (counter-clockwise) by d positions in place.

Examples

Input: [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]

Input: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]

Input: [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
(Because 9 % 4 = 1, so it's 1 rotation)


Constraints

1 ≤ arr.length, d ≤ 10⁵

0 ≤ arr[i] ≤ 10⁵


Approach (Reversal Algorithm)

1. Reverse the first d elements


2. Reverse the remaining n - d elements


3. Reverse the entire array



Complexity

Time: O(n)

Space: O(1)



---

2. Next Permutation

Problem

Given an array arr[] representing a permutation, find the next lexicographically greater permutation.
If no such permutation exists (array is in descending order), return the lowest possible order (sorted in ascending order).

Examples

Input: [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]

Input: [3, 2, 1]
Output: [1, 2, 3] (last permutation → first)

Input: [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]


Constraints

1 ≤ arr.length ≤ 10⁵

0 ≤ arr[i] ≤ 10⁵


Approach

1. Find the largest index i from right where arr[i] < arr[i+1]


2. If no such index exists, reverse the whole array


3. Otherwise:

Find the next greater element than arr[i] from the end and swap

Reverse the subarray from i+1 to end




Complexity

Time: O(n)

Space: O(1)