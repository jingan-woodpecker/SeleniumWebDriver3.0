from selenium import webdriver
import unittest

class GetSourceByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)

    def test_getPageSource(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #获取页面源代码
        pageSource = self.driver.page_source
        print(pageSource)
        #断言源代码中是否包含“地图”关键字
        self.assertTrue("地图" in pageSource, "页面不存在地图关键字")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    
   # 注意：断言关键字使用asserTrue()方法