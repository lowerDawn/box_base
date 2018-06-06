from selenium import webdriver
driver=webdriver.Firefox()
driver.get(r"E:\pycharm\webDay01\02_其他资料\注册实例.html")
current=driver.current_window_handle
handles=driver.window_handles
def Hand(current,handles,titlename):
    for handle in handles:
        if handle !=current:
           driver.switch_to.window(handle)
           title=driver.title
        if title == titlename:
            return handle
# driver.find_element_by_link_text('注册A网页').click()
# driver.find_element_by_link_text('注册B网页').click()
# driver.switch_to.window(Hand(current,handles,'注册B'))
# driver.find_element_by_css_selector("#userB").send_keys("admin")
# driver.find_element_by_css_selector("#passwordB").send_keys("admin")
# driver.find_element_by_css_selector("#telB").send_keys("18611111111")
# driver.find_element_by_css_selector("#emailB").send_keys("123-B@126.com")
# driver.quit()

