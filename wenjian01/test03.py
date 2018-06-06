import unittest
class Test03(unittest.TestCase):
    def setUp(self):
        print("Test03-->setUp被执行")
    def tearDown(self):
        print("Test03-->tearDown被执行")
    def test001(self):
        print("Test03-->test001被执行！")