# Day 2 - Move All Zeroes to End

class Solution:
    def pushZerosToEnd(self, arr):
        count = 0  # Count of non-zero elements

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1

# Example usage
if __name__ == "_main_":
    sol = Solution()
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    sol.pushZerosToEnd(arr)
    print("Output:", arr)  # Output: [1, 2, 4, 3, 5, 0, 0, 0]