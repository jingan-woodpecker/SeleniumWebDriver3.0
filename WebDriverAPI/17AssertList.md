![断言列表](./picture/dropDownBox.png)

```py
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import unittest, time

class AssertSelectByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_checkSelectText(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        #最大化窗口
        self.driver.maximize_window()
        # 点击设置文本
        self.driver.find_element_by_link_text("设置").click()
        # 选择搜索设置
        self.driver.find_element_by_link_text("搜索设置").click()
        time.sleep(3)
        #获取select页面元素对象
        select_element = Select(self.driver.find_element_by_xpath("//select"))
        #获取所有选择项的页面元素对象
        all_options = select_element.options
        #将期望出现的文字内容，存储到一个list对象中
        expectOptionsList = ["每页显示10条","每页显示20条","每页显示50条"]
        #使用python的内置map()函数获取页面中下拉列表展示的选项内容组成的列表对象
        all_optionsList = (list(map(lambda option: option.text, all_options)))
        #断言期望列表对象和实际里诶包对象是否完全一致
        self.assertListEqual(expectOptionsList, all_optionsList)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    
```
	注意：map()内置函数的用法
	在Python3中map(lambda option: option.text, all_options)前面必须添加list才表示返回的是列表
	


