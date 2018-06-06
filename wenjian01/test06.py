import unittest
class Test06(unittest.TestCase):
    def setUp(self):
        print("Test06-->setUp被执行")
    def tearDown(self):
        print("Test06-->tearDown被执行")
    def test001(self):
        print("Test06-->test001被执行！")