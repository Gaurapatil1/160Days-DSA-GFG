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