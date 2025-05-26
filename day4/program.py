# Day 4 - Program 1: Rotate Array

class Solution:
    # Function to rotate array by d elements to the left
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n  # handle cases where d > n
        arr[0:d] = reversed(arr[0:d])
        arr[d:n] = reversed(arr[d:n])
        arr[0:n] = reversed(arr[0:n])

# Day 4 - Program 2: Next Permutation

class Solution:
    def nextPermutation(self, arr):
        N = len(arr)
        ind = -1

        # Step 1: Find the rightmost index where arr[i] < arr[i+1]
        for i in range(N - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                ind = i
                break

        if ind == -1:
            # If no such index, reverse the whole array
            arr.reverse()
            return

        # Step 2: Find the element just larger than arr[ind] from right side
        for i in range(N - 1, ind, -1):
            if arr[i] > arr[ind]:
                arr[i], arr[ind] = arr[ind], arr[i]
                break

        # Step 3: Reverse the subarray after ind
        arr[ind + 1:] = reversed(arr[ind + 1:])

# Example usage
if __name__ == "_main_":
    sol = Solution()

    # Test Rotate Array
    arr1 = [1, 2, 3, 4, 5]
    sol.rotateArr(arr1, 2)
    print("Rotated Array:", arr1)  # [3, 4, 5, 1, 2]

    # Test Next Permutation
    arr2 = [2, 4, 1, 7, 5, 0]
    sol.nextPermutation(arr2)
    print("Next Permutation:", arr2)  # [2, 4, 5, 0, 1, 7]