# Simple Demo

```python
import unittest

def IsA():
    return "A"

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        BaseTestCase.checkfn = getattr(BaseTestCase,'IsA',IsA)
    def test_ok(self):
        self.assertIs('A',BaseTestCase.checkfn())
def test(IsA_fn):
    import types
    newm = types.ModuleType("newm")
    if IsA_fn.__name__ not in ['IsA','IsA2']:
        raise Exception("IsA <----"+"not "+IsA_fn.__name__)
    BaseTestCase.IsA = IsA_fn
    newm.BaseTestCase = BaseTestCase
    unittest.main(newm)

def test2():
    @test
    def IsA():
        return "4"

if __name__ == "__main__":
    unittest.main()


```

then run code:

```sh
python tools.py -v
python -c "from tools import test2;test2()" -v
```
output ok:

```
test_ok (__main__.BaseTestCase.test_ok) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


```

output error:

```

======================================================================
FAIL: test_ok (tools.BaseTestCase.test_ok)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kali/.tmp/tools.py", line 10, in test_ok
    self.assertIs('A',BaseTestCase.checkfn())
AssertionError: 'A' is not '4'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)

```
