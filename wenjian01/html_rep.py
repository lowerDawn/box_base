import unittest,time
from HTML_report.HTMLTestRunner import HTMLTestRunner
discover=unittest.defaultTestLoader.discover('./')
if __name__ == '__main__':
    file_name='../Report'+'%Y_%m_%d %H_%M_%S'+'Report.html'
    with open(file_name,'wb') as f :
        HTMLTestRunner(stream=f,title="niuniu",description="caocao").run(discover)
