from selenium import webdriver
import unittest,time

class AssertByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)

    def test_assertText(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element_by_id("kw").send_keys("菜鸟教程")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        #断言页面是否存在某些关键字
        assert " - 学的不仅是技术,更是梦想!" in self.driver.page_source, "该页面不存在此关键字"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
