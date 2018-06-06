import unittest
class Test07(unittest.TestCase):
    def setUp(self):
        print("Test07-->setUp被执行")
    def tearDown(self):
        print("Test07-->tearDown被执行")
    def test001(self):
        print("Test07-->test001被执行！")