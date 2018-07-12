from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest, time

class AnalogButtonByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)

    def test_operateButton(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        kw = self.driver.find_element_by_id("kw")
        #通过webdriver实例发送一个F12键
        kw.send_keys(Keys.F12)
        time.sleep(3)
        #再次模拟发送一个F12键
        kw.send_keys(Keys.F12)
        #在搜索输入框输入“自动化测试”
        kw.send_keys("自动化测试")
        #模拟发送一个回车键
        kw.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
