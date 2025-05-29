# Kadane's Algorithm - Notes

## Problem:
Given an integer array, find the maximum sum of a contiguous subarray.

## Algorithm:
1. Initialize:
   - max_ending_here = arr[0]
   - max_so_far = arr[0]

2. Traverse the array from index 1 to end:
   - max_ending_here = max(arr[i], max_ending_here + arr[i])
   - max_so_far = max(max_so_far, max_ending_here)

3. Return max_so_far.

## Time Complexity:
- O(n), where n = size of the array

## Space Complexity:
- O(1)

## Example:
Input: [2, 3, -8, 7, -1, 2, 3]
Output: 11