import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
current=driver.current_window_handle
driver.get(r"E:\pycharm\webDay01\02_其他资料\注册实例.html")
select=driver.find_element_by_css_selector('select')
Select(select).select_by_visible_text('广州')
Select(select).select_by_value('bj')
Select(select).select_by_index(3)
js='window.scrollTo(0,10000)'
js1='window.scrollTo(0,0)'
driver.execute_script(js)
driver.execute_script(js1)
driver.find_element_by_css_selector('#alert').click()
alert=driver.switch_to.alert
# alert.dismiss()
alert.accept()
driver.find_element_by_link_text('注册A网页').click()
driver.switch_to.frame('myframe1')
handles1=driver.window_handles
for handle in handles1:
    if handle!=current:
        driver.switch_to.window(handle)
        driver.refresh()
        driver.find_element_by_css_selector('#userA').send_keys('chenmiaocang')
        driver.find_element_by_css_selector('#passwordA').send_keys('33333333333')
        driver.close()
# driver.switch_to.default_content()
driver.switch_to.window(current)
driver.find_element_by_link_text('注册B网页').click()
driver.switch_to.frame('myframe2')
handles2=driver.window_handles
for handle in handles2:
    if handle!=current:
        driver.switch_to.window(handle)
        driver.refresh()
        driver.find_element_by_css_selector('#userB').send_keys('chenlei')
        driver.find_element_by_css_selector('#passwordB').send_keys('111111111111')
        driver.find_element_by_css_selector('#passwordB').clear()
        new=time.strftime('%Y_%m_%d %H_%M_%S')
        driver.get_screenshot_as_file('./Image/%s.jpg' % new)
        driver.quit()
sleep(2)
driver.quit()
