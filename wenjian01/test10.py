import unittest
class Test10(unittest.TestCase):
    def setUp(self):
        print("Test10-->setUp被执行")
    def tearDown(self):
        print("Test10-->tearDown被执行")
    def test001(self):
        print("Test10-->test001被执行！")