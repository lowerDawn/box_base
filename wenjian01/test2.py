
import unittest
from time import sleep

from selenium import webdriver
class IWeb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost/iwebshop/index.php?controller=site&action=index')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def test_web(self):
        driver = self.driver
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_css_selector('[ type="text"]').send_keys('admin')
        driver.find_element_by_css_selector('[ type="password"]').send_keys('123456')
        driver.find_element_by_css_selector('[ type="submit"]').click()

        sleep(3)
        driver.find_element_by_link_text('安全退出').click()
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
