from selenium import webdriver
import unittest

class GetInfoByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)

    def test_getBasicInfo(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #查找“地图”链接文本
        getElementInfo = self.driver.find_element_by_link_text("地图")
        #打印元素的大小标签名
        print("元素的size:", getElementInfo.size)
        print("元素的标签名:",getElementInfo.tag_name)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()