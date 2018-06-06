import unittest
class Test05(unittest.TestCase):
    def setUp(self):
        print("Test05-->setUp被执行")
    def tearDown(self):
        print("Test05-->tearDown被执行")
    def test001(self):
        print("Test05-->test001被执行！")