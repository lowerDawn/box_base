import unittest
class Test08(unittest.TestCase):
    def setUp(self):
        print("Test08-->setUp被执行")
    def tearDown(self):
        print("Test08-->tearDown被执行")
    def test001(self):
        print("Test08-->test001被执行！")