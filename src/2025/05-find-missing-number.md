# Find Missing Number

a list numbers which content from 1..xx, but it missing one number,find it


## SUM range( 1 - n )
$$
    1 + 2  + 3  + 4   + .. n \\
    n + (n-1) + (n-2) + (n-3) .. 1 \\
    (n+1) * n \\
    .\\
    .\\
    sum(1..n) = (n+1)*n / 2
$$

## table

|     |     |     |     |     |     |    |     |
|-----|-----|-----|-----|-----|-----|----|-----|
| 1   | 2   | 3   | 3   | 5   | 6   | .. | n   |
| n   | n-1 | n-2 | n-3 | n-4 | n-5 | .. | 1   |
| n+1 | n+1 | n+1 | n+1 | n+1 | n+1 |    | n+1 |
