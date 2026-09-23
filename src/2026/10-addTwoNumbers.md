# Add Two Numbers

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
```

```mermaid
swimlane-beta LR
    subgraph 342
        A3[3]
        A4[4]
        A2[2]
        A2 --> A4
        A4 --> A3
    end
    subgraph 465
        B4[4]
        B6[6]
        B5[5]
        B5 --> B6
        B6 --> B4
    end
    subgraph 807
        C8[3+4+1 = 8]
        C0[4+6 = 10]
        C7[2+5 = 7]
        C7 --> C0
        C0 --> C8
    end
```

$$ 342 + 465 = 807 $$
