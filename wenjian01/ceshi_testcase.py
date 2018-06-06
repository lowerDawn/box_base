import unittest
from HTML_report.HTMLTestRunner import HTMLTestRunner
import time
discover=unittest.defaultTestLoader.discover('.')
if __name__ == '__main__':
    name='../Report'+time.strftime+'Report.html'
    with open(name,'wb') as f :
        HTMLTestRunner(stream=f,title='iwebshop自动化测试').run(discover)
