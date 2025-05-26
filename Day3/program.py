# Day 3 - Reverse an Array

class Solution:
    def reverseArray(self, arr):
        start, end = 0, len(arr) - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

# Example usage
if __name__ == "_main_":
    sol = Solution()
    arr = [1, 4, 3, 2, 6, 5]
    sol.reverseArray(arr)
    print("Output:", arr)  # Output: [5, 6, 2, 3, 4, 1]