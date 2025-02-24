I'll explain a few fundamental algorithms using practical examples that are easy to understand.



Let's look at three common algorithms:

1. Linear Search
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
numbers = [4, 2, 7, 1, 9, 5]
position = linear_search(numbers, 7)  # Returns 2
```
This is the simplest search algorithm - it checks each element one by one until it finds the target.

2. Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22]
sorted_numbers = bubble_sort(numbers)  # Returns [12, 22, 25, 34, 64]
```
Bubble sort repeatedly steps through the list, compares adjacent elements and swaps them if they're in the wrong order.

3. Binary Search (requires sorted array)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
sorted_numbers = [1, 3, 5, 7, 9, 11]
position = binary_search(sorted_numbers, 7)  # Returns 3
```
Binary search is much faster than linear search for sorted arrays. It repeatedly divides the search interval in half.

Would you like me to explain any of these algorithms in more detail or show you some other common algorithms?
