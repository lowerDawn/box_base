import unittest
from selenium import webdriver
from time import sleep
from wenjian01.get_handle import Hand
class Handle(unittest.TestCase):
    def setUp(self):
      self.driver=webdriver.Firefox()
      driver=self.driver
      driver.get(r"E:\pycharm\webDay01\02_其他资料\注册实例.html")
      driver.maximize_window()
      driver.implicitly_wait(10)
    def ZhuCe(self):
        driver=self.driver
        current = driver.current_window_handle
        driver.find_element_by_link_text('注册A网页').click()
        driver.find_element_by_link_text('注册B网页').click()
        handles=driver.window_handles
        handle=Hand(current,handles,'注册B')
        driver.switch_to.window(handle)
        driver.find_element_by_css_selector("#userB").send_keys("admin")
        driver.find_element_by_css_selector("#passwordB").send_keys("admin")
        driver.find_element_by_css_selector("#telB").send_keys("18611111111")
        driver.find_element_by_css_selector("#emailB").send_keys("123-B@126.com")
        sleep(2)
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()