```py
from selenium import webdriver
import unittest, time
def isElementPresent(self,css):
    s = self.driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print("元素未找到：%s"%css)
        return False
    elif len(s) == 1:
        return True
    else:
        print("找到%s个元素：%s"%(len(s),css))
        return  False

class ElementsExistByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_isElementPresent(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #判断页面上有无id为kw的元素
        if isElementPresent(self, "#kw"):
            self.driver.find_element_by_id("kw").send_keys("自动化测试")
            time.sleep(3)
            print("测试通过")
        #判断页面上有无标签为input元素
        if isElementPresent(self, "input"):
            self.driver.find_element_by_tag_name("input").send_keys("自动化测试")
        #判断页面上有无id为xxx的元素
        if isElementPresent(self, "xxx"):
            self.driver.find_element_by_id("xxx").send_keys("自动化测试")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    ```
	注意：self.driver.find_elements_by_css_selector(css_selector=css)其中的element加上`s`
	
	测试结果如下：
		测试通过
		找到18个元素：input
		元素未找到：xxx
		
	
