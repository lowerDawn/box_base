# import unittest
# from wenjian01.test01 import  Test01
# from wenjian01.test02 import Test02
# if __name__ == '__main__':
#     suite=unittest.TestCase()
#     suite.addTest(Test01("test001"))
#     suite.addTest(Test02('test002'))
#     suite.addTest(unittest.makesuite())
#     unittest.TextTestResult().run(suite)

# 第一种
# import unittest
# from Lx.test01 import Test01
# from Lx.test02 import Test22
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(Test01('test01'))
#     suite.addTest(Test02('test01'))
#     unittest.TextTestRunner().run(suite)  #执行测试用例


# 第二种

# import unittest
# from wenjian01.test01 import Test01wx
# from wenjian01.test02 import Test02
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(unittest.makeSuite(Test01))
#     suite.addTest(unittest.makeSuite(Test02))
#     unittest.TextTestRunner().run(suite)

# 第三种
# import unittest
# if __name__ == '__main__':
#     runner=unittest.TextTestResult()
#     discover=unittest.defaultTestLoader.discover('./', pattern='test*.py')
#     runner.run(discover)




import unittest
import time

from selenium import webdriver

from wenjian01.test01 import Test01
from wenjian01.test02 import Test02
class T_T(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest(Test01('test01'))
    # suite.addTest(Test02('test02'))
    suite.addTest(unittest.makeSuite(Test01))
    # discover=unittest.defaultTestLoader.discover('./', pattern='test*.py')
    # unittest.TextTestRunner().run(discover)
    # unittest.TextTestRunner().run(suite)
    unittest.main()
