from selenium.webdriver.support.ui import Select
from selenium import webdriver
import unittest,time

class SelectDropDownBoxByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_getElementTitle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #点击设置文本
        self.driver.find_element_by_link_text("设置").click()
        #选择搜索设置
        self.driver.find_element_by_link_text("搜索设置").click()
        time.sleep(3)
        #使用name属性值找到下拉列表
        selectText = self.driver.find_element_by_name("NR")
        allOptions = selectText.find_elements_by_tag_name("option")

        for option in allOptions:
            print("选项显示的文本：", option.text)
            print("选项值为：", option.get_attribute("value"))

    def tearDown(self):
        #退出浏览器
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
