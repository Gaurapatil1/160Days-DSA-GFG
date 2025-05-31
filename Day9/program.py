import sys

class Solution:

    # 1️⃣ Smallest Positive Missing Number
    def missingNumber(self, arr):
        n = len(arr)
        shift = self.segregate(arr)
        return self.findMissingPositive(arr[shift:])

    def segregate(self, arr):
        j = 0
        for i in range(len(arr)):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        return j

    def findMissingPositive(self, arr):
        n = len(arr)
        for i in range(n):
            if abs(arr[i]) - 1 < n and arr[abs(arr[i]) - 1] > 0:
                arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        for i in range(n):
            if arr[i] > 0:
                return i + 1
        return n + 1

    # 2️⃣ Max Circular Subarray Sum
    def kadane(self, arr):
        max_so_far = float('-inf')
        max_ending_here = 0
        for x in arr:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def circularSubarraySum(self, arr):
        n = len(arr)
        max_kadane = self.kadane(arr)

        # Handle case where all elements are negative
        if max_kadane < 0:
            return max_kadane

        total_sum = sum(arr)
        inverted_arr = [-x for x in arr]
        max_wrap = total_sum + self.kadane(inverted_arr)

        return max(max_kadane, max_wrap)