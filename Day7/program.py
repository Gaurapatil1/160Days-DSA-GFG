class Solution:
    def maxSubArraySum(self, arr):
        max_so_far = arr[0]
        max_ending_here = arr[0]
        
        for i in range(1, len(arr)):
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far

# Test cases
if __name__ == "_main_":
    sol = Solution()
    print(sol.maxSubArraySum([2, 3, -8, 7, -1, 2, 3]))  # Output: 11
    print(sol.maxSubArraySum([-2, -4]))                 # Output: -2
    print(sol.maxSubArraySum([5, 4, 1, 7, 8]))          # Output: 25
    sol = Solution()
    print(sol.maxSubArraySum([2, 3, -8, 7, -1, 2, 3]))  # Output: 11
    print(sol.maxSubArraySum([-2, -4]))                 # Output: -2
    print(sol.maxSubArraySum([5, 4, 1, 7, 8]))          # Output: 25