Let me show you some more practical algorithms that solve interesting problems.

1. **Anagram Checker**
```python
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Count characters in both strings
    char_count = {}
    
    # Count characters in first string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract counts for second string
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return all(count == 0 for count in char_count.values())

# Examples
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "bello"))    # False
```

2. **Finding Maximum Subarray Sum** (Kadane's Algorithm)
```python
def max_subarray_sum(arr):
    if not arr:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend the existing subarray or start a new one
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(numbers)  # Returns 6 (subarray [4, -1, 2, 1])
```

3. **Prime Number Generator** (Sieve of Eratosthenes)
```python
def sieve_of_eratosthenes(n):
    # Create a boolean array and initialize all entries as True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    p = 2
    while p * p <= n:
        # If is_prime[p] is not changed, then it's a prime
        if is_prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

# Example
primes_up_to_30 = sieve_of_eratosthenes(30)
# Returns [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

4. **Caesar Cipher** (Simple Encryption)
```python
def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around if necessary
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

# Examples
encrypted = caesar_cipher("Hello World", 3)  # Returns "Khoor Zruog"
decrypted = caesar_cipher(encrypted, -3)     # Returns "Hello World"
```

5. **Finding Longest Common Subsequence**
```python
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    
    # Create a 2D array to store lengths of common subsequences
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the LCS
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return lcs

# Example
result = longest_common_subsequence("ABCDGH", "AEDFHR")  # Returns "ADH"
```

These algorithms showcase different techniques:
- **Character frequency analysis** (anagram checker)
- **Dynamic programming** (max subarray, LCS)
- **Mathematical optimization** (sieve of Eratosthenes)
- **Character manipulation** (Caesar cipher)
- **Greedy approach** (Kadane's algorithm)

Each solves a different type of problem you might encounter in real programming scenarios. Would you like me to explain any of these algorithms in more detail or show you how they work step by step?
