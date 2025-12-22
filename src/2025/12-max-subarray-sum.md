# Maximum Subarray Sum - Kadane's Algorithm


## How Kadane's Algorithm Works

The algorithm iterates through the array, maintaining two key variables:
- `max_so_far`: Stores the maximum sum found anywhere in the array up to the current point.
- `current_max`: tores the maximum sum of a subarray ending at the current position.
At each element, it decides whether to extend the `current_max` subarray by adding the current element or to start a new subarray from the current element (if the current element itself is greater than `current_max` + current element). If `current_max` becomes negative, it's reset to 0 (or the current element if all numbers are negative, depending on the variation). `max_so_far` is updated whenever `current_max` exceeds it


## Time Complexity

Kadane's Algorithm has a time complexity of $O(n)$, where '$n$' is the number of elements in the input array
