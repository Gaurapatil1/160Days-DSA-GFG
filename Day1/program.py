# Day 01 - Array Basics
# Topic: Introduction to Arrays
# Source: GeeksforGeeks - 160 Days DSA Challenge

# Example Problem: Find the largest element in an array

def find_largest(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Sample test
sample_array = [4, 9, 2, 1, 12, 5]
print("Largest element:", find_largest(sample_array))

def second_smallest(arr):
    if len(arr) < 2:
        return -1

    first = second = float('inf')

    for num in arr:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num

    return second if second != float('inf') else -1

# Test
print(second_smallest([4, 1, 2, 1, 3]))  # Output: 2