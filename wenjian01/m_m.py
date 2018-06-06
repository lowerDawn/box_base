# import unittest,time
# import sys
# from selenium import webdriver
# class M_M(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get('http://localhost/iwebshop/')
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#     def tearDown(self):
#         self.driver.quit()
#     def test_login(self):
#         driver=self.driver
#         driver.find_element_by_partial_link_text('登录').click()
#         driver.find_element_by_css_selector('[type="text"]').send_keys('admin')
#         driver.find_element_by_css_selector('[type="password"]').send_keys('123456')
#         driver.find_element_by_css_selector('.submit_login').click()
#         text=driver.find_element_by_css_selector('.loginfo').text
#         try:
#             self.assertIn('adeim',text)
#         except:
#             new_time=time.strftime('%Y%m%d %H%M%S')
#             driver.get_screenshot_as_file('./%s_%s.jpg'%(new_time,sys.exc_info()[1]))
#             raise
# if __name__ == '__main__':
#     unittest.main()