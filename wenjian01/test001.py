from selenium import webdriver
from time import sleep
import unittest,sys,time
class BoXue_login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        driver=self.driver
        driver.get('http://ntlias-stu.boxuegu.com/#/login')
        driver.maximize_window()
        driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()
    def Xue_login(self):
        self.driver.find_elements_by_css_selector('.el-input__inner')[0].send_keys('A180300201')
        self.driver.find_elements_by_css_selector('.el-input__inner')[1].send_keys('qwzx6541456123')
        self.driver.find_element_by_css_selector('button').click()
        text=self.driver.find_element_by_css_selector('.span-name').text
        try:
            self.assertIn('蔡聪',text)
            # Equal 打印图片名称不能使用它 打印不出来

        except ArithmeticError:
            new_time=time.strftime('%Y_%m_%d %H_%M_%S')

            exc=sys.exc_info()[1]
            print(new_time, exc)
            # self.driver.get_screenshot_as_file('./%s--%s.jpg' % (new_time, exc))
            raise
        sleep(3)
        self.driver.close()
if __name__ == '__main__':
    unittest.main()