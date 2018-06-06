
# 测试报告
import time
from HTML_report.HTMLTestRunner import HTMLTestRunner
import unittest
discover=unittest.defaultTestLoader.discover('./')
if __name__ == '__main__':
    file_name='../report'+time.strftme+'report.html'
    with open(file_name,'wd') as f:
        HTMLTestRunner(stram=f,title='web自动化第四版',description='win7系统').run(discover)













