from selenium import webdriver
import unittest,time

class VisitSoGouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'D:\pycharm\chromedriver.exe')

    def test_visitRecentURL(self):
        firstURL = "http://www.baidu.com"
        secondURL = "https://www.sina.com.cn"
        #访问百度首页
        self.driver.get(firstURL)
        #最大化窗口
        self.driver.maximize_window()
        #访问新浪首页
        self.driver.get(secondURL)

        #返回上一次访问过的百度首页
        self.driver.back()
        time.sleep(3)
        #再次回到新浪首页
        self.driver.forward()
        time.sleep(3)
    def tearDown(self):
        #退出浏览器
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()

