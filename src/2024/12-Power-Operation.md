# Exponentiation operation - Power Operation - constant - varible term - coefficient

- see [SymPy](https://docs.sympy.org/latest/explanation/gotchas.html) 

```python
class Operation:
    def __init__(self,constant,varilbe_term,coefficient):
        pass
    def __pow__(self,*args):
        return x*n
    def 
A = Operation()
n = 1 or 2 or 3
A ** n
```
## Symbol(x)
- \_\_pow\_\_ methods: $ x^n $
- \_\_sub\_\_ methods: $ x - n$
- \_\_rsub\_\_ methods: $ n - x $
- \_\_neg\_\_ methods: $ -x $
- \_\_sub\_\_ methods: $ x + n $
- \_\_rsub\_\_ methods: $ n + x $
- \_\_mul\_\_ methods: $ x * n $
- \_\_rmul\_\_ methods: $ n * x $
