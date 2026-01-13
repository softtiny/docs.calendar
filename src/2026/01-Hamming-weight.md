# Hamming weight

- Hamming weight population count (popcount)

The Hamming weight of a string over a finite alphabet is defined as the number of positions in the string whose symbols differ from the zero symbol of the alphabet. In the binary case, which is the most common application, this corresponds to the number of 1s in the binary string. This concept originated in the context of error-detecting and error-correcting codes, where it measures the nonzero components in codewords.


### Examples

| String (Binary) | Hamming Weight | Explanation                               |
| :-------------- | :------------- | :---------------------------------------- |
| `0000`          | 0              | No '1's                                   |
| `0101`          | 2              | Two '1's at positions 1 and 3             |
| `1111`          | 4              | Four '1's                                 |
| `1000101`       | 3              | Three '1's at positions 0, 4, and 6       |
