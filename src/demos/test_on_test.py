import unittest
import types
import pdb
import os

class FailMsg:
    BASEANOTEQ = "BASEANOTEQ"


class BaseA:
    base_a="base_a"

class BaseANotEqual:
    base_a = "base_b_not_equal_base_a"



class SilentTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class BaseWrapTestCase(unittest.TestCase):
    def run_assert(self,_run_assert):
        _run_assert_method = getattr(self,_run_assert)
        def gogo(*arg,**args):
            try:
                _run_assert_method(*arg,**args)
            except Exception as err:
                self._run_assert=_run_assert
                self._run_assert_msg = FailMsg.BASEANOTEQ
                raise err
        setattr(self,_run_assert,gogo)
    def __init__(self,data):
        super().__init__(data)
        for runkey in dir(self):
            if runkey.startswith("assert"):
                self.run_assert(runkey)
                

class BaseATestCase(BaseWrapTestCase):
    def setUp(self):
        self._module = types.ModuleType("tmpa")
        self._module.main=BaseA
    def test_ok(self):
        main = self.get_result()
        self.assertEqual(main.base_a,"base_a",FailMsg.BASEANOTEQ)
    def get_result(self):
        module = self._module
        return module.main

class MainTestCase(unittest.TestCase):
    def setUp(self):
        devnull = open(os.devnull, 'w')
        self.stream = devnull
    def tearDown(self):
        self.stream.close()

    def go_unittest_main(self,runtime):
        #testRunner=SilentTestRunner(verbosity=0)
        progress = unittest.main(
                runtime,
                exit=False, 
                testRunner=SilentTestRunner(verbosity=0, stream=self.stream)
                )
        result = progress.result
        failures = result.failures
        if len(failures) > 0:
            runcase = failures[0][0]
            return runcase._run_assert_msg
    def test_catch_err(self):
        runtime = types.ModuleType("runtime")
        class BaseATestCaseRunTime(BaseATestCase):
            def setUp(self):
                self._module=runtime

        runtime.BaseATestCase=BaseATestCaseRunTime
        runtime.main = BaseA
        self.go_unittest_main(runtime)
        runtime.main = BaseANotEqual
        error_msg = self.go_unittest_main(runtime)
        self.assertEqual(error_msg,FailMsg.BASEANOTEQ)
    


if __name__ == "__main__":
    unittest.main()
