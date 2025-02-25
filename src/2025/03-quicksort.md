# QuickSort

## Key charateristics of QuickSort
- Time Complexity:
  - Average case: $ \mathcal{O}(n\log n) $
  - Worst case: $ \mathcal{O}(n^2) $  - rare with good pivot selection
  - Best case: $ \mathcal{O}(n\log n) $
- Space Complexity:
  - Average case:  $ \mathcal{O}(\log n) $ for the recursive call stack
  - Best Case: $ \mathcal{O}(\log n) $
  - Worst case: $ \mathcal{O}(n) $

## sorts in place (modifies in original array)
```python
def quicksort_inplace(arr, low, high):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1  # index of smaller element
        
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1  # increment index of smaller element
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        # pi is partitioning index
        pi = partition(low, high)
        
        # Separately sort elements before and after partition
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)

# Usage
arr = [7, 2, 1, 6, 8, 5, 3, 4]
quicksort_inplace(arr, 0, len(arr)-1)
```


# Calculate QuickSort's time complexity step by step.

## First, let's understand what happens at each partition step:
```python
def partition(arr,low,high):
    pivot = arr[high]  # @1 O(1) .$ \mathcal{O}(1)$
    i = low - 1 #  @1 O(1)

    for j in range(low,high):  # @2 O(n) .$ \mathcal{O}(n) $
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1] # @1 O(1)
    return i+1
```
- 1.$ \mathcal{O}(1)$
- 2.$ \mathcal{O}(n)$

## Let's analyze different cases:

### Best Case:
```
Initial array: [5,2,8,1,9,3]
Perfect partition each time:
Level 1:        [2,1,3] [5] [8,9]    → n comparisons
Level 2:        [1] [2] [3]  [8] [9]  → n/2 + n/2 comparisons
Depth: log n levels

Time Complexity = O(n log n)
```
- $ \mathcal{O}(n*\log_{10}{n}) $

### Average Case:

```
Each partition splits array into roughly equal parts:
T(n) = T(n/2) + T(n/2) + n  (partition cost)
     = 2T(n/2) + n

Using Master Theorem:
a = 2 (subproblems)
b = 2 (size reduction)
k = 1 (partition work)

Time Complexity = O(n log n)
```
- $ \mathcal{O}(n*\log_{10}{n}) $

### Worst Case:

```
Already sorted array: [1,2,3,4,5]
Uneven partitions each time:
Level 1: [] [1] [2,3,4,5]    → n comparisons
Level 2:    [] [2] [3,4,5]   → (n-1) comparisons
Level 3:       [] [3] [4,5]  → (n-2) comparisons

Sum = n + (n-1) + (n-2) + ... + 1
    = n(n+1)/2
Time Complexity = O(n²)
```
- $ \mathcal{O}(n^2) $

##  Mathematical Breakdown:

For average case:

```
T(n) = 2T(n/2) + n

Recursion tree:
Level 0:                n
Level 1:           n/2     n/2
Level 2:      n/4   n/4  n/4   n/4

Work at each level = n
Number of levels = log n
Total work = n * log n
```
- Work at each level $ = n $
- Number of levels $ = \log_{10}{n} $
- Total work $ = n *  \log_{10}{n} $

## Detailed breakdown of operations:

```python
def quicksort(arr, low, high):
    if low < high:
        # Partition operation: O(n)
        pivot_index = partition(arr, low, high)

        # Recursive calls
        quicksort(arr, low, pivot_index - 1)   # T(k)
```

Recurrence relation:
- Best/Average: $$ T(n) \quad = \quad 2*T(\frac{n}{2}) + \mathcal{O}(n) $$ 
- Worst: $$ T(n) \quad = \quad T(n-1) + \mathcal{O}(n) $$

# Factors affecting time complexity:

- Pivot selection strategy

```python
# Better pivot selection to avoid worst case
def get_pivot(arr, low, high):
    mid = (low + high) // 2
    pivot = median([arr[low], arr[mid], arr[high]])
    return pivot
```
- Data distribution
- Initial array ordering
- Handling of duplicate elements


# Chapter 1

Here is an inline example, $ \mathcal{O}(n\log n) $,

Here is an inline example, $ \pi(\theta) $,

an equation,

$$ \nabla f(x) \in \mathbb{R}^n, $$

and a regular \$ symbol.
