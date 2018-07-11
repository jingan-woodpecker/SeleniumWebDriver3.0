from selenium import webdriver
import unittest,time

class GetElementTitleByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)

    def test_getElementTitle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        #定位百度首页“新闻”即id属性值为"ul"的div元素下的第一个链接元素，class='mnav'
        firstElement = self.driver.find_element_by_xpath("//*[@class='mnav'][1]")
        #通过找到链接元素对象的text属性获取到链接元素的文本内容
        first_text = firstElement.text
        self.assertEqual(first_text, "新闻", "不是该文本内容")

    def tearDown(self):
        #退出浏览器
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
