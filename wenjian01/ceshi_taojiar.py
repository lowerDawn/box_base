import unittest
import time
import sys
from selenium import webdriver
class M_M(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        driver=self.driver
        driver.get('http://localhost/iwebshop/')
        driver.maximize_window()
        driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()
    def Test_login(self):
        driver=self.driver
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_css_selector('[name="login_info"]').send_keys('admin')
        driver.find_element_by_css_selector('[name="password"]').send_keys('123456')
        driver.find_element_by_css_selector('.submit_login').click()
        text=driver.find_element_by_css_selector(".loginfo").text
        try:
            self.assertIn('欢迎你',text)
        except ArithmeticError:
            new_time=time.steftime('%Y%m%d %H%M%S')
            EXC=sys.exc_info()[1]
            driver.get_screenshot_as_file('./s--s11.jpg')  #  %(new_time,EXC)
            raise
if __name__ == '__main__':
    # unittest.TextTestRunner().run(unittest.defaultTestLoader.discover('.',pattern='test*.py'))
    unittest.main()