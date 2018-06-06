import unittest
from selenium import webdriver
from time import sleep

class Handle(unittest.TestCase):
    def setUp(self):
      self.driver=webdriver.Firefox()
      driver=self.driver
      driver.get(r"E:\pycharm\webDay01\02_其他资料\注册实例.html")
      driver.maximize_window()
      driver.implicitly_wait(10)
    def ZhuCe(self):
        driver=self.driver
        driver.find_element_by_link_text('注册A网页').click()
        # driver.find_element_by_link_text('注册A网页').click()
        sleep(2)
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()