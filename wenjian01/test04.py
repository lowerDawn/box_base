import unittest
class Test04(unittest.TestCase):
    def setUp(self):
        print("Test04-->setUp被执行")
    def tearDown(self):
        print("Test04-->tearDown被执行")
    def test001(self):
        print("Test04-->test001被执行！")