from selenium.webdriver.support.ui import Select
from selenium import webdriver
import unittest

class GetAttributeByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_getPageElementAttribute(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #找到搜索输入框元素
        searchBox = self.driver.find_element_by_id('kw')
        #获取搜索输入框页面元素的name的属性值
        print(searchBox.get_attribute("name"))

        #使用页面元素对象的value_of_css_property()方法获取的CSS属性值
        print("搜索输入框的高度是：",searchBox.value_of_css_property("height"))
        print("搜索输入框的宽度是：",searchBox.value_of_css_property("width"))
        font = searchBox.value_of_css_property("font-family")
        print("搜索输入框的字体是：", font)
        #断言搜索输入框字体是否是arial字体
        self.assertEqual(font, "arial")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
