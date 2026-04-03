# Josephus problem

```python
def josephus(n,k):
    arr=list(range(1,n+1))
    p=0
    while len(arr)>1:
        p=(p+k-1)%len(arr)
        arr.pop(p)
    return arr[0]
```


- `(p+k-1) % len(arr)` — pointer reset in **O(1)**, always one step
- `arr.pop(p)` — mid-array deletion in **O(n)**, shifts all elements after index `p`
- Outer `while` loop runs **n−1** times → **O(n)**

Combined: O(n) × O(n) = **$O(n^2)$** time, **O(n)** space.

