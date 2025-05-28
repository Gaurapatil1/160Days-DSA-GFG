class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        n = len(nums)
        num1, num2, c1, c2 = 0, 0, 0, 0
        res = []

        # First pass to find possible candidates
        for x in nums:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1
            elif c1 == 0:
                num1 = x
                c1 = 1
            elif c2 == 0:
                num2 = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        # Second pass to confirm the candidates
        c1, c2 = 0, 0
        for x in nums:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1

        # Collect valid candidates
        if c1 > n // 3:
            res.append(num1)
        if c2 > n // 3:
            res.append(num2)

        res.sort()
        return res

# Example usage:
sol = Solution()
print(sol.findMajority([2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]))  # Output: [5, 6]
print(sol.findMajority([1, 2, 3, 4, 5]))                  # Output: []
