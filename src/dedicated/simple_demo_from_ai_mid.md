Let me show you a few more interesting algorithms.



1. Selection Sort
```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example
numbers = [64, 25, 12, 22, 11]
sorted_nums = selection_sort(numbers)  # Returns [11, 12, 22, 25, 64]
```
Selection sort finds the minimum element and puts it at the beginning, then repeats for the rest of the array.

2. Fibonacci Sequence (using Dynamic Programming)
```python
def fibonacci(n):
    if n <= 1:
        return n
    
    fib = [0] * (n + 1)
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]

# Example
result = fibonacci(6)  # Returns 8 (sequence: 0,1,1,2,3,5,8)
```
This demonstrates dynamic programming by storing previously calculated values.

3. Quick Sort (one of the most efficient sorting algorithms)
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Example
numbers = [3, 6, 8, 10, 1, 2, 1]
sorted_nums = quick_sort(numbers)  # Returns [1, 1, 2, 3, 6, 8, 10]
```
Quick sort uses a divide-and-conquer strategy by selecting a 'pivot' and partitioning the array around it.

4. Depth-First Search (for graphs/trees)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')  # Prints: A B D E F C
```
DFS explores as far as possible along each branch before backtracking.

These algorithms demonstrate different problem-solving strategies:
- Selection Sort shows simple iteration and swapping
- Fibonacci with DP shows how to optimize recursive problems
- Quick Sort demonstrates divide-and-conquer
- DFS shows graph traversal

Would you like me to explain any of these in more detail or show you some practical applications of these algorithms?
