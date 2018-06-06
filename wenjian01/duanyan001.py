# import sys
# from selenium import webdriver
# import unittest,time
# class Iwe(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Firefox()
#         self.driver.get('http://ntlias-stu.boxuegu.com/')
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#     def test_login(self):
#         driver=self.driver
#         driver.find_element_by_link_text('登录').click()
#         driver.find_element_by_css_selector('[type="text"]').send_keys('111111')
#         driver.find_element_by_css_selector('[type="password"]').send_keys('123456')
#         driver.find_element_by_link_text('登录').click()
#         text = driver.find_element_by_css_selector('.loginfo').text
#         try:
#             self.assertIn('admin',text)
#         except ArithmeticError:
#             new=time.strftime('%Y-%m-%d %H-%M-%S')
#             driver.get_screenshot_as_file('../Image/%s--%S.jpg'%(new,sys.exc_info()[1]))
#             raise
#         driver.find_element_by_link_text('安全退出').click()
#     def tearDown(self):
#         self.driver.quit()
# if __name__ == '__main__':
#     unittest.main()