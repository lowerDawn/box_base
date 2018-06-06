import unittest
class Test01(unittest.TestCase):
    def setUp(self):
        print("Test01-->setUp被执行")
    def tearDown(self):
        print("Test01-->tearDown被执行")
    def test001(self):
        print("Test01-->test001被执行！")
    def test002(self):
        print("Test01-->test002被执行！")
if __name__ == '__main__':
    unittest.main()