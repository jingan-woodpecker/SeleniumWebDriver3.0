#刷新当前页面
from selenium import webdriver
import unittest,time

class refreshPageByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\pycharm\chromedriver.exe')
        
    def test_refrshCurrentPage(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #刷新当前页面
        self.driver.refresh()
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()