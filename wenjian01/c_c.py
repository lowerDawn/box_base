import unittest,sys,time
from selenium import webdriver
class IWeb01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost/iwebshop/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.quit()
    def test_01(self):
        driver = self.driver
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_css_selector('[type="text"]').send_keys('admin')
        driver.find_element_by_css_selector('[type="password"]').send_keys('123456')
        driver.find_element_by_css_selector('[type="submit" ]').click()
        text = driver.find_element_by_css_selector('.loginfo').text
        try:
            self.assertIn('admin',text)
        except:
            driver.get_screenshot_as_file('../图片/%s-%s.png'%(time.strftime('%Y%m%d-%H%M%S'),sys.exc_info()[1]))
            raise

if __name__ == '__main__':
    unittest.main()