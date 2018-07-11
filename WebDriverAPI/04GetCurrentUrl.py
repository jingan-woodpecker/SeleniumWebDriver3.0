from selenium import webdriver
import unittest

class GetCurrentPageUrlByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getCurrenPageUrl(self):
        url = "https://www.baidu.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        #获取当前页面的URL
        currentPageURL = self.driver.current_url
        print(currentPageURL)
        #断言当前网址是否为"https://www.baidu.com/"
        self.assertEqual(currentPageURL, "https://www.baidu.com/", "当前网址不正确")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    
  #注意：url 地址一定要填写完整，不然容易导致测试失败