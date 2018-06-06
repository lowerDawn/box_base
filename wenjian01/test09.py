import unittest
class Test09(unittest.TestCase):
    def setUp(self):
        print("Test09-->setUp被执行")
    def tearDown(self):
        print("Test09-->tearDown被执行")
    def test001(self):
        print("Test09-->test001被执行！")