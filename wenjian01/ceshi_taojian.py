import unittest
from selenium import webdriver
from wenjian01.test01 import Test01
from wenjian01.test02 import Test02
# 定义一个类继承unittest框架，成为一个测试用例，（只有继承unittest才能使用unittest框架）
class TaoJian(unittest.TestCase):
    #定义一个初始化的方法
    def setUp(self):
        self.driver=webdriver.Firefox()
    # 定义name方法 确定执行代码
if __name__ == '__main__':
    # 定义一个嵌套的变量
    suite=unittest.TestSuite()
    # 往变量的嵌套里面塞方法
    suite.addTest(Test01('test01'))
    suite.addTest(Test02('test02'))
    # 往变量的嵌套里面塞类（类里面的所有方法【必须test开头】会被执行）
    suite.addTest(unittest.makeSuite(Test01))
    # 调用TextTestRunner()执行套件
    unittest.TextTestRunner().run(suite)
    unittest.main()

